#!/usr/bin/env python3
"""R8 search driver: runs one query via z-ai CLI, saves JSON, prints result count.
Usage: python3 run_search.py <outfile> <query>
"""
import json
import subprocess
import sys
import os

def main():
    out, query = sys.argv[1], sys.argv[2]
    try:
        r = subprocess.run(
            ["z-ai", "function", "-n", "web_search",
             "-a", json.dumps({"query": query, "num": 10}),
             "-o", out],
            capture_output=True, text=True, timeout=95)
        if not os.path.exists(out):
            print(f"{out} -> NOFILE rc={r.returncode} err={r.stderr[:200]}")
            return
        try:
            d = json.load(open(out))
            if isinstance(d, list):
                print(f"{out} -> {len(d)} results | q: {query[:60]}")
            else:
                print(f"{out} -> NONLIST type={type(d).__name__} | q: {query[:60]}")
        except Exception as e:
            sz = os.path.getsize(out)
            print(f"{out} -> BADJSON size={sz} ({str(e)[:80]}) | q: {query[:60]}")
    except subprocess.TimeoutExpired:
        print(f"{out} -> TIMEOUT | q: {query[:60]}")

if __name__ == "__main__":
    main()
