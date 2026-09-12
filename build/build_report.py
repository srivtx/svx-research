#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the body PDF of the SVX Software Industry Gap Analysis report.

Route: Report (ReportLab) per briefs/report.md.
- TocDocTemplate + multiBuild (clickable auto TOC)
- SVX green cascade palette (design_engine palette-cascade --intent nature
  --mode minimal --harmony monochrome --seed 7)
- English document: FreeSerif body/headings, DejaVuSans code
- install_font_fallback() called after font registration
- Page numbering: TOC page = roman, body resets to Arabic 1
- No forced page breaks between chapters (CondPageBreak orphan guard only)
"""
import os
import sys
import hashlib

PDF_SKILL_SCRIPTS = '/home/z/my-project/skills/pdf/scripts'
if PDF_SKILL_SCRIPTS not in sys.path:
    sys.path.insert(0, PDF_SKILL_SCRIPTS)
sys.path.insert(0, '/home/z/my-project/scripts')

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, CondPageBreak,
    Table, TableStyle, KeepTogether, HRFlowable, Image,
)
from reportlab.platypus.tableofcontents import TableOfContents
from PIL import Image as PILImage

# ---------------------------------------------------------------------------
# Fonts (registered set only, per briefs/report.md)
# ---------------------------------------------------------------------------
FONT_DIR = '/usr/share/fonts'
pdfmetrics.registerFont(TTFont('NotoSerifSC', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC-Bold', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf'))
# NOTE: 'Noto Sans SC' static weights are not present on this system (variable
# font only). English document -> FreeSerif primary, NotoSerifSC first fallback.
pdfmetrics.registerFont(TTFont('SarasaMonoSC', f'{FONT_DIR}/truetype/chinese/SarasaMonoSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif', f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold', f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic', f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic', f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans', f'{FONT_DIR}/truetype/dejavu/DejaVuSansMono.ttf'))

registerFontFamily('NotoSerifSC', normal='NotoSerifSC', bold='NotoSerifSC-Bold')
registerFontFamily('FreeSerif', normal='FreeSerif', bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic', boldItalic='FreeSerif-BoldItalic')
registerFontFamily('DejaVuSans', normal='DejaVuSans', bold='DejaVuSans')

from pdf import install_font_fallback  # noqa: E402  (skill scripts path)
install_font_fallback()

# ---------------------------------------------------------------------------
# SVX green cascade palette (nature / minimal / monochrome, seed 7)
# Tier caps verified: XL S<=0.08, L S<=0.15, M S<=0.30, S S<=0.50, XS S<=0.75
# ---------------------------------------------------------------------------
PAGE_BG      = colors.HexColor('#f5f6f5')   # XL
SECTION_BG   = colors.HexColor('#edeeed')   # XL
CARD_BG      = colors.HexColor('#e4eae7')   # L
TABLE_STRIPE = colors.HexColor('#edefee')   # L
HEADER_FILL  = colors.HexColor('#456454')   # M
BORDER       = colors.HexColor('#b7d3c5')   # S
ACCENT       = colors.HexColor('#298959')   # XS
TEXT_PRIMARY = colors.HexColor('#232725')
TEXT_MUTED   = colors.HexColor('#77817c')

TABLE_HEADER_COLOR = HEADER_FILL
TABLE_ROW_EVEN     = colors.white
TABLE_ROW_ODD      = TABLE_STRIPE

# ---------------------------------------------------------------------------
# Layout constants
# ---------------------------------------------------------------------------
PAGE_W, PAGE_H = A4
MARGIN = 1.0 * inch                      # symmetric left/right (overflow.md 1.5)
TOP_MARGIN = 1.05 * inch
BOTTOM_MARGIN = 1.0 * inch
AVAIL_W = PAGE_W - 2 * MARGIN            # ~451pt
AVAIL_H = PAGE_H - TOP_MARGIN - BOTTOM_MARGIN
H1_ORPHAN = AVAIL_H * 0.25               # pagination.md 3/4 threshold
MAX_KEEP = PAGE_H * 0.4                  # safe_keep_together cap

DOC_TITLE = 'SVX Software Industry Gap Analysis 2025-2026'
OUT = '/home/z/my-project/scripts/assets/body.pdf'

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
S = {}
S['body'] = ParagraphStyle('Body', fontName='FreeSerif', fontSize=10.5,
                           leading=17, alignment=TA_JUSTIFY,
                           textColor=TEXT_PRIMARY, spaceBefore=0, spaceAfter=10)
S['h1'] = ParagraphStyle('H1', fontName='FreeSerif', fontSize=22, leading=27,
                         alignment=TA_LEFT, textColor=HEADER_FILL,
                         spaceBefore=14, spaceAfter=4)
S['h2'] = ParagraphStyle('H2', fontName='FreeSerif', fontSize=15, leading=20,
                         alignment=TA_LEFT, textColor=TEXT_PRIMARY,
                         spaceBefore=16, spaceAfter=8)
S['h3'] = ParagraphStyle('H3', fontName='FreeSerif', fontSize=11.5, leading=16,
                         alignment=TA_LEFT, textColor=TEXT_PRIMARY,
                         spaceBefore=12, spaceAfter=6)
S['bullet'] = ParagraphStyle('Bullet', fontName='FreeSerif', fontSize=10.5,
                             leading=16.5, alignment=TA_LEFT,
                             textColor=TEXT_PRIMARY, leftIndent=16,
                             bulletIndent=4, spaceAfter=6)
S['caption'] = ParagraphStyle('Caption', fontName='FreeSerif-Italic', fontSize=8.5,
                              leading=12, alignment=TA_CENTER,
                              textColor=TEXT_MUTED, spaceBefore=0, spaceAfter=0)
S['ref'] = ParagraphStyle('Ref', fontName='FreeSerif', fontSize=8.8, leading=12.6,
                          alignment=TA_LEFT, textColor=TEXT_PRIMARY,
                          firstLineIndent=-16, leftIndent=16, spaceAfter=4)
S['stat_big'] = ParagraphStyle('StatBig', fontName='FreeSerif', fontSize=20,
                               leading=24, alignment=TA_CENTER, textColor=ACCENT)
S['stat_label'] = ParagraphStyle('StatLabel', fontName='FreeSerif', fontSize=8.4,
                                 leading=11.5, alignment=TA_CENTER,
                                 textColor=TEXT_MUTED)
S['th'] = ParagraphStyle('TH', fontName='FreeSerif', fontSize=9.5, leading=12.5,
                         alignment=TA_LEFT, textColor=colors.white)
S['td'] = ParagraphStyle('TD', fontName='FreeSerif', fontSize=9, leading=12.5,
                         alignment=TA_LEFT, textColor=TEXT_PRIMARY)
S['td_small'] = ParagraphStyle('TDS', fontName='FreeSerif', fontSize=8.4,
                               leading=11.4, alignment=TA_LEFT,
                               textColor=TEXT_PRIMARY)
S['toc_title'] = ParagraphStyle('TocTitle', fontName='FreeSerif', fontSize=22,
                                leading=27, alignment=TA_LEFT,
                                textColor=HEADER_FILL, spaceAfter=14)
S['toc0'] = ParagraphStyle('TOC0', fontName='FreeSerif', fontSize=11,
                           leading=20, leftIndent=18, textColor=TEXT_PRIMARY)

# ---------------------------------------------------------------------------
# TOC-aware document template
# ---------------------------------------------------------------------------
BODY_START = {'page': 2}     # first content page (default: TOC takes 1 page)
PAGE_OFFSET = {'v': 1}       # body page number = doc.page - PAGE_OFFSET


class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if getattr(flowable, 'is_first_chapter', False):
            BODY_START['page'] = self.page
            PAGE_OFFSET['v'] = self.page - 1
        if hasattr(flowable, 'bookmark_name'):
            level = getattr(flowable, 'bookmark_level', 0)
            text = getattr(flowable, 'bookmark_text', '')
            key = getattr(flowable, 'bookmark_key', '')
            shown = self.page - PAGE_OFFSET['v']
            self.notify('TOCEntry', (level, text, shown, key))


ROMAN = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v',
         6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix', 10: 'x'}


def on_page(canvas, doc):
    """Page background + header + footer (drawn at page begin, under content)."""
    canvas.saveState()
    # Layer 0: light green page background (SVX green body)
    canvas.setFillColor(PAGE_BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    # Header: muted title left + accent rule
    canvas.setFont('FreeSerif', 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, PAGE_H - 44, DOC_TITLE.upper())
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(1.5)
    canvas.line(MARGIN, PAGE_H - 52, PAGE_W - MARGIN, PAGE_H - 52)
    # Footer: light rule + author left + page number right (bare number)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 54, PAGE_W - MARGIN, 54)
    canvas.setFont('FreeSerif', 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, 42, 'SVX Research')
    if doc.page < BODY_START['page']:
        label = ROMAN.get(doc.page, str(doc.page))
    else:
        label = str(doc.page - PAGE_OFFSET['v'])
    canvas.drawRightString(PAGE_W - MARGIN, 42, label)
    canvas.restoreState()


# ---------------------------------------------------------------------------
# Flowable helpers
# ---------------------------------------------------------------------------
def add_heading(text, style, level=0, first_chapter=False):
    key = 'h_%s' % hashlib.md5(text.encode()).hexdigest()[:8]
    p = Paragraph('<a name="%s"/><b>%s</b>' % (key, text), style)
    p.bookmark_name = key
    p.bookmark_level = level
    p.bookmark_text = text
    p.bookmark_key = key
    if first_chapter:
        p.is_first_chapter = True
    return p


def measure(el):
    try:
        w, h = el.wrap(AVAIL_W, AVAIL_H)
        return h
    except Exception:
        return 0


def safe_keep_together(elements):
    """KeepTogether capped at 40% page height (briefs/report.md)."""
    total = sum(measure(e) for e in elements)
    if total <= MAX_KEEP:
        return [KeepTogether(elements)]
    if len(elements) >= 2:
        return [KeepTogether(elements[:2])] + list(elements[2:])
    return list(elements)


def embed_image(path, max_width=None, max_height=None):
    if max_width is None:
        max_width = AVAIL_W
    if max_height is None:
        max_height = PAGE_H * 0.32
    pil = PILImage.open(path)
    ow, oh = pil.size
    ratio = min(max_width / ow if ow > max_width else 1.0,
                max_height / oh if oh > max_height else 1.0)
    return Image(path, width=ow * ratio, height=oh * ratio)


def fix_dashes(t):
    """Bind em dashes to the preceding word (no line-start dashes)."""
    return t.replace(' \u2014 ', '\u00a0\u2014 ')


def stat_cell(big, label):
    return [Paragraph('<b>%s</b>' % big, S['stat_big']),
            Spacer(1, 4),
            Paragraph(fix_dashes(label), S['stat_label'])]


def build_stat_strip(stats):
    """Three callout cards separated by transparent gap columns."""
    gap = AVAIL_W * 0.03
    card = (AVAIL_W - 2 * gap) / 3.0
    row = [stat_cell(b, l) for b, l in stats]
    data = [[row[0], Paragraph('', S['stat_label']), row[1],
             Paragraph('', S['stat_label']), row[2]]]
    t = Table(data, colWidths=[card, gap, card, gap, card], hAlign='CENTER')
    cmds = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]
    for col in (0, 2, 4):
        cmds.append(('BACKGROUND', (col, 0), (col, 0), CARD_BG))
        cmds.append(('BOX', (col, 0), (col, 0), 1, ACCENT))
    for col in (1, 3):  # transparent gap columns: no padding (narrower than padding)
        cmds.append(('LEFTPADDING', (col, 0), (col, 0), 0))
        cmds.append(('RIGHTPADDING', (col, 0), (col, 0), 0))
    t.setStyle(TableStyle(cmds))
    return t


def build_callout(big, label):
    w = AVAIL_W * 0.72
    data = [
        [[Paragraph('<b>%s</b>' % big, S['stat_big'])]],
        [[Paragraph(fix_dashes(label), S['stat_label'])]],
    ]
    inner = Table(data, colWidths=[w], hAlign='CENTER')
    inner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('BOX', (0, 0), (-1, -1), 1, ACCENT),
        ('TOPPADDING', (0, 0), (0, 0), 12),
        ('BOTTOMPADDING', (0, 0), (0, 0), 4),
        ('TOPPADDING', (0, 1), (0, 1), 2),
        ('BOTTOMPADDING', (0, 1), (0, 1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return inner


def build_table(spec):
    header = spec['header']
    rows = spec['rows']
    ratios = spec['ratios']
    assert abs(sum(ratios) - 1.0) < 0.02, 'ratios must sum to 1'
    n = len(header)
    cell_style = S['td_small'] if n >= 5 else S['td']
    col_widths = [r * AVAIL_W * 0.99 for r in ratios]
    assert sum(col_widths) <= AVAIL_W + 0.5, 'table exceeds available width'

    data = [[Paragraph('<b>%s</b>' % h, S['th']) for h in header]]
    for r in rows:
        data.append([Paragraph(fix_dashes(str(c)), cell_style) for c in r])

    t = Table(data, colWidths=col_widths, hAlign='CENTER', repeatRows=1)
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('VALIGN', (0, 1), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        cmds.append(('BACKGROUND', (0, i), (-1, i),
                     TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN))
    t.setStyle(TableStyle(cmds))

    caption = Paragraph(fix_dashes(spec['title']), S['caption'])
    out = [Spacer(1, 18)]
    if len(rows) <= 8:
        out.extend(safe_keep_together([t, Spacer(1, 6), caption]))
    else:
        out.append(t)
        out.extend([Spacer(1, 6), caption])
    out.append(Spacer(1, 18))
    return out


def build_chart(path, caption_text):
    img = embed_image(path)
    cap = Paragraph(fix_dashes(caption_text), S['caption'])
    out = [Spacer(1, 24)]
    out.extend(safe_keep_together([img, Spacer(1, 8), cap]))
    out.append(Spacer(1, 24))
    return out


# ---------------------------------------------------------------------------
# Story assembly
# ---------------------------------------------------------------------------
from report_content import CH1, CH2, CH3, CH4, CH5          # noqa: E402
from report_content2 import CH6, CH7, CH8, CH9, CH10, APPENDIX  # noqa: E402

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH8, CH9, CH10, APPENDIX]

story = []

# --- Front matter: TOC (cover is a separate PDF merged later) ---
toc = TableOfContents()
toc.levelStyles = [S['toc0']]
story.append(Paragraph('<b>Table of Contents</b>', S['toc_title']))
story.append(HRFlowable(width='100%', thickness=1.2, color=ACCENT,
                        spaceBefore=0, spaceAfter=14))
story.append(toc)
story.append(PageBreak())


def render_blocks(blocks, story):
    """Append content blocks; returns nothing."""
    for blk in blocks:
        kind = blk[0]
        if kind == 'p':
            story.append(Paragraph(fix_dashes(blk[1]), S['body']))
        elif kind == 'h2':
            nxt = Paragraph('', S['body'])
            story.extend(safe_keep_together([Paragraph('<b>%s</b>' % blk[1], S['h2'])]))
        elif kind == 'h3':
            story.append(Paragraph('<b>%s</b>' % blk[1], S['h3']))
        elif kind == 'bullets':
            for item in blk[1]:
                story.append(Paragraph(fix_dashes(item), S['bullet'], bulletText='\u2022'))
            story.append(Spacer(1, 4))
        elif kind == 'stat_strip':
            story.append(Spacer(1, 8))
            story.append(build_stat_strip(blk[1]))
            story.append(Spacer(1, 14))
        elif kind == 'callout':
            story.append(Spacer(1, 10))
            story.append(build_callout(blk[1], blk[2]))
            story.append(Spacer(1, 14))
        elif kind == 'table':
            story.extend(build_table(blk[1]))
        elif kind == 'chart':
            story.extend(build_chart(blk[1], blk[2]))
        elif kind == 'refs':
            for r in blk[1]:
                story.append(Paragraph(fix_dashes(r), S['ref']))
            story.append(Spacer(1, 6))


first = True
for ch in CHAPTERS:
    title = ('%s. %s' % (ch['num'], ch['title'])) if ch['num'] else ch['title']
    heading = add_heading(title, S['h1'], level=0, first_chapter=first)
    rule = HRFlowable(width='100%', thickness=1.2, color=ACCENT,
                      spaceBefore=0, spaceAfter=12)
    story.append(CondPageBreak(H1_ORPHAN))     # orphan guard only, never forced break
    blocks = ch['blocks']
    lead = []
    if blocks and blocks[0][0] == 'p':
        lead = [Paragraph(blocks[0][1], S['body'])]
        rest = blocks[1:]
    else:
        lead = []
        rest = blocks
    story.extend(safe_keep_together([heading, rule] + lead))
    render_blocks(rest, story)
    if first:
        first = False
    story.append(Spacer(1, 10))

# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
doc = TocDocTemplate(
    OUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN,
    title=DOC_TITLE, author='SVX', creator='SVX',
    subject='SVX industry-wide gap analysis: missing tools, unbuilt links, and badly-built categories in the software industry, 2025-2026',
)
doc.multiBuild(story, onFirstPage=on_page, onLaterPages=on_page)
print('body pdf written:', OUT)

from pypdf import PdfReader  # noqa: E402
r = PdfReader(OUT)
print('pages:', len(r.pages), '| body starts at pdf page:', BODY_START['page'])
