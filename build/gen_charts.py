#!/usr/bin/env python3
"""Generate the seven charts for the SVX Software Industry Gap Analysis report.

SVX light-green cascade palette (design_engine palette-cascade
--intent nature --mode light --harmony monochrome --seed 77).
Hue family ~150deg. English labels, Carlito font (clean humanist sans).

Rules applied (typesetting/charts.md):
- top/right spines deleted unconditionally; bottom/left thin + muted
- grid deleted entirely when values are labeled directly (all charts here)
- legend (where used): no frame, small markers
- donut instead of pie (hole 0.65, center metric)
- horizontal bars for long category labels (auto-rotate rule)
- value labels placed collision-free (inside if tall, outside if short)
- line/area charts: smooth-ish, area fill gradient, first/last/max/min labels
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

# Carlito for a modern humanist sans look (DejaVu fallback for symbols)
fm.fontManager.addfont('/usr/share/fonts/truetype/english/Carlito-Regular.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/english/Carlito-Bold.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')

OUT_DIR = '/home/z/my-project/scripts/assets'
os.makedirs(OUT_DIR, exist_ok=True)

# SVX light-green cascade (seed 77)
ACCENT   = '#1d9459'   # XS  emerald
ACCENT_2 = '#40c884'   # XS  mint (series 2)
DARK     = '#2f5140'   # M   deep forest
ICON     = '#388860'   # S   mid green
LIGHT    = '#b4cfc2'   # S   sage border
CARD     = '#e4e9e6'   # L   light sage surface
TEXT     = '#181b1a'
MUTED    = '#747d78'

plt.rcParams['font.sans-serif'] = ['Carlito', 'DejaVu Sans']
plt.rcParams['font.size'] = 10
plt.rcParams['text.color'] = TEXT
plt.rcParams['axes.labelcolor'] = MUTED
plt.rcParams['xtick.color'] = MUTED
plt.rcParams['ytick.color'] = TEXT
plt.rcParams['axes.unicode_minus'] = False

DPI = 200


def strip_spines(ax, keep_left=False):
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    ax.spines['left'].set_visible(keep_left)
    if keep_left:
        ax.spines['left'].set_color(LIGHT)
        ax.spines['left'].set_linewidth(0.8)
    ax.spines['bottom'].set_color(LIGHT)
    ax.spines['bottom'].set_linewidth(0.8)


# ---------------------------------------------------------------------------
# Chart 1 - Quantified pain (horizontal bar, values labeled -> no grid)
# ---------------------------------------------------------------------------
labels = [
    'Devs who do not fully trust AI-generated code\n(SonarSource, Jan 2026)',
    'Construction estimating still done in Excel\n(PremierCS, 2026)',
    'Opportunity data reps collect that never\nenters the CRM (DevRev, 2026)',
    'Data practitioners spending >20% of time on\ndata-stack complexity (Modern Data Co., 2025)',
    'Employees who see no purpose in their intranet\n(Firstup, Jun 2024)',
    'Devs who always verify AI-generated code\nbefore committing (SonarSource, Jan 2026)',
]
values = [96, 85, 79, 63, 57, 48]
colors = [ACCENT, ACCENT, ACCENT, ICON, ICON, ACCENT_2]

fig, ax = plt.subplots(figsize=(8.4, 3.6), constrained_layout=True)
y = range(len(labels))
bars = ax.barh(y, values, height=0.62, color=colors, edgecolor='none')
ax.set_yticks(list(y))
ax.set_yticklabels(labels, fontsize=8.6)
ax.invert_yaxis()
ax.set_xlim(0, 108)
ax.set_xlabel('Share of surveyed practitioners (%)', fontsize=9)
strip_spines(ax)
ax.grid(False)
ax.tick_params(axis='y', length=0)
ax.tick_params(axis='x', labelsize=8.5)
for rect, v in zip(bars, values):
    ax.text(v + 1.5, rect.get_y() + rect.get_height() / 2,
            f'{v}%', va='center', ha='left', fontsize=9.5,
            color=TEXT, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'chart1_pain.png'), dpi=DPI)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 2 - AI-era escalation (two panels, values labeled -> no grid)
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.1), constrained_layout=True)

a_vals, a_x = [233, 362], ['2024', '2025']
bars_a = ax1.bar(a_x, a_vals, width=0.5, color=[LIGHT, DARK], edgecolor='none')
ax1.set_ylabel('Documented AI incidents', fontsize=9)
ax1.set_ylim(0, 430)
strip_spines(ax1, keep_left=True)
ax1.grid(False)
ax1.tick_params(labelsize=9)
for rect, v in zip(bars_a, a_vals):
    ax1.text(rect.get_x() + rect.get_width() / 2, v + 10, str(v),
             ha='center', va='bottom', fontsize=10, color=TEXT, fontweight='bold')
ax1.annotate('+55%', xy=(1, 362), xytext=(0.42, 380), fontsize=9.5,
             color=ACCENT, fontweight='bold')

b_vals = [3.5, 8.4]
bars_b = ax2.bar(a_x, b_vals, width=0.5, color=[LIGHT, DARK], edgecolor='none')
ax2.set_ylabel('Enterprise LLM API spend ($B)', fontsize=9)
ax2.set_ylim(0, 10.2)
strip_spines(ax2, keep_left=True)
ax2.grid(False)
ax2.tick_params(labelsize=9)
for rect, v in zip(bars_b, b_vals):
    ax2.text(rect.get_x() + rect.get_width() / 2, v + 0.22, f'${v}B',
             ha='center', va='bottom', fontsize=10, color=TEXT, fontweight='bold')
ax2.annotate('2.4x in 6 months', xy=(1, 8.4), xytext=(0.28, 8.9), fontsize=9.5,
             color=ACCENT, fontweight='bold')

fig.savefig(os.path.join(OUT_DIR, 'chart2_escalation.png'), dpi=DPI)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 3 - The verification gap (paired horizontal bars, NEW)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.4, 3.3), constrained_layout=True)
pairs = [
    (('Devs using or planning to use AI tools\n(Stack Overflow, 2025)', 84),
     ('Devs who trust the accuracy of AI output\n(Stack Overflow, 2025)', 29)),
    (('Devs who do not fully trust AI-generated code\n(SonarSource, Jan 2026)', 96),
     ('Devs who always verify it before committing\n(SonarSource, Jan 2026)', 48)),
]
rows, yticks, yvals, ycols = [], [], [], []
ypos = 0
gaps = []
for top, bot in pairs:
    rows.append((ypos, top))
    rows.append((ypos - 0.42, bot))
    gaps.append((ypos - 0.21, top[1] - bot[1]))
    ypos -= 1.35
for r, (yy, (lab, val)) in enumerate(rows):
    yticks.append(yy)
    yvals.append(val)
    ycols.append(ACCENT if r % 2 == 0 else LIGHT)
bars = ax.barh([yt for yt in yticks], yvals, height=0.46, color=ycols, edgecolor='none')
ax.set_yticks(yticks)
ax.set_yticklabels([rows[i][1][0] for i in range(len(rows))], fontsize=8.4)
ax.invert_yaxis()
ax.set_xlim(0, 112)
ax.set_xlabel('Share of surveyed developers (%)', fontsize=9)
strip_spines(ax)
ax.grid(False)
ax.tick_params(axis='y', length=0)
ax.tick_params(axis='x', labelsize=8.5)
for rect, v in zip(bars, yvals):
    ax.text(v + 1.5, rect.get_y() + rect.get_height() / 2, f'{v}%',
            va='center', ha='left', fontsize=9.5, color=TEXT, fontweight='bold')
for gy, g in gaps:
    ax.text(106, gy, f'gap: {g} pts', va='center', ha='right',
            fontsize=9.5, color=DARK, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.28', fc=CARD, ec=LIGHT, lw=0.8))
fig.savefig(os.path.join(OUT_DIR, 'chart3_trust.png'), dpi=DPI)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 4 - The unwatched wiring wave + CRM blindness (2 panels, NEW)
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.3), constrained_layout=True,
                               gridspec_kw={'width_ratios': [1, 1.05]})

# Panel A: agent integration share (slope-style bars)
v = [5, 40]
bars_a = ax1.bar(['2025', '2026\n(projected)'], v, width=0.46,
                 color=[LIGHT, ACCENT], edgecolor='none')
ax1.set_ylabel('Enterprise apps integrated with\ntask-specific AI agents (%)', fontsize=8.6)
ax1.set_ylim(0, 50)
strip_spines(ax1, keep_left=True)
ax1.grid(False)
ax1.tick_params(labelsize=9)
ax1.text(0, v[0] + 1.5, '<5%', ha='center', va='bottom', fontsize=10,
         color=TEXT, fontweight='bold')
ax1.text(1, v[1] + 1.5, '40%', ha='center', va='bottom', fontsize=10,
         color=TEXT, fontweight='bold')
ax1.annotate('', xy=(1, 38), xytext=(0, 7),
             arrowprops=dict(arrowstyle='->', color=DARK, lw=1.4,
                             connectionstyle='arc3,rad=-0.25'))
ax1.set_title('Agent wiring, unwatched\n(Gabe Veach, Apr 2026)', fontsize=9,
              color=MUTED, loc='left', pad=8)

# Panel B: donut - CRM blindness
wedge_vals = [79, 21]
wedges, _ = ax2.pie(wedge_vals, colors=[ACCENT, CARD], startangle=90,
                    counterclock=False,
                    wedgeprops=dict(width=0.35, edgecolor='white', linewidth=1.5))
ax2.text(0, 0.08, '79%', ha='center', va='center', fontsize=22,
         color=DARK, fontweight='bold')
ax2.text(0, -0.24, 'never enters\nthe CRM', ha='center', va='center', fontsize=9,
         color=MUTED)
ax2.set_title('Opportunity data reps collect\n(DevRev, 2026)', fontsize=9,
              color=MUTED, loc='left', pad=8)
ax2.set(aspect='equal')

fig.savefig(os.path.join(OUT_DIR, 'chart4_agents.png'), dpi=DPI)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 5 - What unowned plumbing costs (horizontal bar, $K, NEW)
# ---------------------------------------------------------------------------
c_labels = [
    'Average healthcare breach-cost premium when\nunmanaged data sits in spreadsheets (blueBriX, 2026)',
    'Average vendor lock-in cost per enterprise\nmigration (Kong, Jun 2026)',
    'Annual cost of stale feature flags per\norganization (Flagshark, 2025)',
    'Average cost to process one expense report\n(Corpay, Mar 2026)',
]
c_vals = [670, 315, 125, 58]
c_cols = [DARK, ACCENT, ICON, LIGHT]

fig, ax = plt.subplots(figsize=(8.4, 3.2), constrained_layout=True)
bars = ax.barh(range(len(c_labels)), c_vals, height=0.6, color=c_cols, edgecolor='none')
ax.set_yticks(range(len(c_labels)))
ax.set_yticklabels(c_labels, fontsize=8.6)
ax.invert_yaxis()
ax.set_xlim(0, 790)
ax.set_xlabel('Cost (thousand USD)', fontsize=9)
strip_spines(ax)
ax.grid(False)
ax.tick_params(axis='y', length=0)
ax.tick_params(axis='x', labelsize=8.5)
fmt = ['$670K', '$315K', '$125K', '$58']
for rect, lab in zip(bars, fmt):
    ax.text(rect.get_width() + 12, rect.get_y() + rect.get_height() / 2,
            lab, va='center', ha='left', fontsize=9.5, color=TEXT, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'chart5_costs.png'), dpi=DPI)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 6 - The review bottleneck (two panels, hours, NEW)
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.1), constrained_layout=True)

# Panel A: where the week goes (horizontal)
r_labels = ['Median hours to merge\none PR (State of Code\nReview 2024)',
            'Hours per week spent\nreviewing code\n(Microsoft Research)']
r_vals = [13, 6]
bars_a = ax1.barh([0, 1], r_vals, height=0.5, color=[DARK, ACCENT], edgecolor='none')
ax1.set_yticks([0, 1])
ax1.set_yticklabels(r_labels, fontsize=8.3)
ax1.invert_yaxis()
ax1.set_xlim(0, 15.5)
ax1.set_xlabel('Hours', fontsize=9)
strip_spines(ax1)
ax1.grid(False)
ax1.tick_params(axis='y', length=0)
ax1.tick_params(axis='x', labelsize=8.5)
for rect, v in zip(bars_a, r_vals):
    ax1.text(v + 0.25, rect.get_y() + rect.get_height() / 2, f'{v}h',
             va='center', ha='left', fontsize=10, color=TEXT, fontweight='bold')

# Panel B: what review bots did (before/after)
b_vals = [5.87, 8.33]
bars_b = ax2.bar(['Before\nautomation', 'After adopting\nreview bots'], b_vals,
                 width=0.5, color=[LIGHT, DARK], edgecolor='none')
ax2.set_ylabel('Avg PR closure duration (hours)', fontsize=8.8)
ax2.set_ylim(0, 10.4)
strip_spines(ax2, keep_left=True)
ax2.grid(False)
ax2.tick_params(labelsize=8.8)
for rect, v in zip(bars_b, b_vals):
    hh, mm = int(v), int(round((v - int(v)) * 60))
    ax2.text(rect.get_x() + rect.get_width() / 2, v + 0.2, f'{hh}h{mm:02d}m',
             ha='center', va='bottom', fontsize=10, color=TEXT, fontweight='bold')
ax2.annotate('+2h 28m', xy=(1, 8.33), xytext=(0.32, 9.3), fontsize=9.5,
             color=ACCENT, fontweight='bold')
ax2.set_title('(arXiv, Dec 2024)', fontsize=9, color=MUTED, loc='left', pad=6)

fig.savefig(os.path.join(OUT_DIR, 'chart6_review.png'), dpi=DPI)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 7 - Validated gap deep-dives per research lens (horizontal bar, NEW)
# ---------------------------------------------------------------------------
l_labels = [
    'Plumbing: integration, data and exit (Ch. 5)',
    'Missing links between ecosystems (Ch. 6)',
    'Developer tooling (Ch. 4)',
    'Badly-built categories (Ch. 7)',
    'Frontier: AI infra and unsexy industries (Ch. 8)',
]
l_vals = [8, 8, 7, 5, 4]

fig, ax = plt.subplots(figsize=(8.4, 2.9), constrained_layout=True)
bars = ax.barh(range(len(l_labels)), l_vals, height=0.58,
               color=[ACCENT, ACCENT, ICON, ICON, LIGHT], edgecolor='none')
ax.set_yticks(range(len(l_labels)))
ax.set_yticklabels(l_labels, fontsize=8.8)
ax.invert_yaxis()
ax.set_xlim(0, 9.6)
ax.set_xlabel('Validated gap deep-dives that survived incumbent screening', fontsize=9)
strip_spines(ax)
ax.grid(False)
ax.tick_params(axis='y', length=0)
ax.tick_params(axis='x', labelsize=8.5)
for rect, v in zip(bars, l_vals):
    ax.text(v + 0.12, rect.get_y() + rect.get_height() / 2, str(v),
            va='center', ha='left', fontsize=10, color=TEXT, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'chart7_lens.png'), dpi=DPI)
plt.close(fig)

print('charts written to', OUT_DIR)
for f in sorted(os.listdir(OUT_DIR)):
    if f.endswith('.png'):
        print(' -', f, os.path.getsize(os.path.join(OUT_DIR, f)), 'bytes')
