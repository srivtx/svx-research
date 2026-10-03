#!/usr/bin/env python3
"""svxsearch — the hardened SVX research search driver.

Encodes every degradation lesson from research passes R1-R15, V1-V5
(see tools/SEARCH-PLAYBOOK.md for the full map). Standard usage:

    python3 tools/svxsearch.py research/raw-search-results/<run>/ qNN "query text"

What it does beyond the raw z-ai CLI:
  1. Query manifest — every call's text, timestamp, outcome, and grade
     are appended to <run-dir>/manifest.json (fixes R8's lost-argv
     problem: sub-topic attribution no longer depends on memory).
  2. Junk detection — screens results against the known junk-artifact
     classes (rfp.wiki/Scribd noise, the OSRS artifact, JBoss/Apache
     dictionary pages, empty-title sets) and grades the set
     USABLE / THIN / JUNK / FAILED.
  3. Retry discipline — on junk/empty results it suggests the b-suffix
     rephrase convention; on 429/timeout it sleeps and retries once.
  4. Sleep pacing — enforces the inter-call sleep so agents stop
     burning quota in bursts (a documented 429 trigger).

Std-lib only (house rule). Raw result files remain immutable once
written; the manifest is append-only.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

INTER_CALL_SLEEP = 25          # seconds between searches (pacing)
RETRY_SLEEP = 35               # seconds before a 429 retry
THIN_THRESHOLD = 3             # fewer usable results than this = THIN
JUNK_TITLE_MARKERS = (
    "zoberetimifid",           # the recurring OSRS artifact (R7/R9/R12/R13a/V3)
    "Old School RuneScape", "OSRS",
    "JBoss", "Apache JBoss",
    "ISFP",                    # recurring book/list noise (R8)
)
META_MARKER = "svxsearch-meta"


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_manifest(run_dir: str) -> list:
    path = os.path.join(run_dir, "manifest.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    return []


def append_manifest(run_dir: str, entry: dict) -> None:
    path = os.path.join(run_dir, "manifest.json")
    manifest = load_manifest(run_dir)
    manifest.append(entry)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


def grade_results(payload: list) -> tuple[str, list[str]]:
    """Grade a result set: (USABLE | THIN | JUNK, reasons)."""
    if not isinstance(payload, list) or not payload:
        return "JUNK", ["empty or non-list payload"]
    reasons: list[str] = []
    usable = 0
    empty_titles = 0
    junk_hits = 0
    for r in payload:
        if not isinstance(r, dict):
            continue
        title = (r.get("title") or "").strip()
        snip = (r.get("snippet") or r.get("description") or "").strip()
        blob = f"{title} {snip}"
        if not title:
            empty_titles += 1
        if any(m.lower() in blob.lower() for m in JUNK_TITLE_MARKERS):
            junk_hits += 1
        if title and not any(m.lower() in blob.lower() for m in JUNK_TITLE_MARKERS):
            usable += 1
    if junk_hits:
        reasons.append(f"{junk_hits} known-artifact hits")
    if empty_titles:
        reasons.append(f"{empty_titles} empty-title rows (V4 quirk)")
    if junk_hits >= max(2, len(payload) // 2):
        return "JUNK", reasons
    if usable == 0:
        return "JUNK", reasons or ["no usable rows"]
    if usable < THIN_THRESHOLD:
        return "THIN", reasons or [f"only {usable} usable rows"]
    return "USABLE", reasons or [f"{usable} usable rows"]


def run_search(out_path: str, query: str) -> tuple[bool, str]:
    """Invoke the z-ai CLI. Returns (ok, detail)."""
    try:
        proc = subprocess.run(
            ["z-ai", "function", "-n", "web_search",
             "-a", json.dumps({"query": query, "num": 10}),
             "-o", out_path],
            capture_output=True, text=True, timeout=95,
        )
    except subprocess.TimeoutExpired:
        return False, "CLI timeout (95s)"
    if not os.path.exists(out_path):
        return False, f"no file; rc={proc.returncode}; {proc.stderr[:160]}"
    try:
        with open(out_path, encoding="utf-8") as fh:
            payload = json.load(fh)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        return False, f"bad JSON: {exc}"
    if not isinstance(payload, list):
        return False, f"non-list payload: {type(payload).__name__}"
    return True, f"{len(payload)} rows"


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        print("usage: svxsearch.py <run-dir> <file-stem-qNN> <query text>")
        return 2
    run_dir, stem, query = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(run_dir, exist_ok=True)
    out_path = os.path.join(run_dir, f"{stem}.json")

    entry = {
        META_MARKER: True,
        "file": f"{stem}.json",
        "query": query,
        "utc": now(),
        "attempts": [],
    }

    ok, detail = run_search(out_path, query)
    entry["attempts"].append({"try": 1, "ok": ok, "detail": detail})
    if not ok and ("429" in detail or "timeout" in detail):
        print(f"[svxsearch] {detail} — sleeping {RETRY_SLEEP}s, one retry")
        time.sleep(RETRY_SLEEP)
        ok, detail = run_search(out_path, query)
        entry["attempts"].append({"try": 2, "ok": ok, "detail": detail})

    grade, reasons = "FAILED", ["search failed"]
    if ok:
        with open(out_path, encoding="utf-8") as fh:
            grade, reasons = grade_results(json.load(fh))
    entry["grade"] = grade
    entry["reasons"] = reasons
    append_manifest(run_dir, entry)

    print(f"[svxsearch] {stem} -> {grade}: {'; '.join(reasons)}")
    if grade == "JUNK":
        print(f"[svxsearch] convention: rephrase once as {stem}b; if that is junk too, "
              "retire the phrasing (3-strike rule) and switch to direct reads")
    if grade in ("USABLE", "THIN"):
        print(f"[svxsearch] pace: sleep {INTER_CALL_SLEEP}s before the next call")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
