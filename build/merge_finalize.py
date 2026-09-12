#!/usr/bin/env python3
"""Merge cover + body into the final SVX deliverable PDF, normalized to A4."""
from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = '/home/z/my-project/scripts/assets/cover.pdf'
BODY = '/home/z/my-project/scripts/assets/body.pdf'
OUT = '/home/z/my-project/download/SVX-Industry-Gap-Analysis-2025-2026.pdf'


def normalize_page_to_a4(page, force=False):
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if force or abs(w - A4_W) > 2 or abs(h - A4_H) > 2:
        page.scale_to(A4_W, A4_H)
    return page


writer = PdfWriter()
cover_page = PdfReader(COVER).pages[0]
writer.add_page(normalize_page_to_a4(cover_page, force=True))
for page in PdfReader(BODY).pages:
    writer.add_page(normalize_page_to_a4(page))
writer.add_metadata({
    '/Title': 'SVX Software Industry Gap Analysis 2025-2026',
    '/Author': 'SVX',
    '/Creator': 'SVX',
    '/Subject': 'SVX industry-wide gap analysis: missing tools, unbuilt links, and badly-built categories in the software industry',
})
with open(OUT, 'wb') as f:
    writer.write(f)

r = PdfReader(OUT)
sizes = {(round(float(p.mediabox.width)), round(float(p.mediabox.height))) for p in r.pages}
print('final pdf:', OUT)
print('pages:', len(r.pages), '| page sizes:', sizes)
