#!/usr/bin/env python3
"""Generate the two charts for the SVX Software Industry Gap Analysis report.
SVX green palette family (hue ~150deg, cascade nature/monochrome). English labels.
Rules applied (charts.md): top/right spines deleted, no grid when values
are labeled directly, legend without frame, value labels collision-free,
horizontal bars for long category labels.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT_DIR = '/home/z/my-project/scripts/assets'
os.makedirs(OUT_DIR, exist_ok=True)

# SVX green family (single hue ~150deg, lightness variants only)
ACCENT = '#298959'
DARK = '#1f5e40'
LIGHT = '#a3d9bd'
BORDER = '#b7d3c5'
TEXT = '#1d2a24'
MUTED = '#5f7a6c'

plt.rcParams['font.size'] = 10
plt.rcParams['text.color'] = TEXT
plt.rcParams['axes.labelcolor'] = MUTED
plt.rcParams['xtick.color'] = MUTED
plt.rcParams['ytick.color'] = TEXT

# ----------------------------------------------------------------------------
# Chart 1 - Quantified pain (horizontal bar, % stats, values labeled -> no grid)
# ----------------------------------------------------------------------------
labels = [
    'Devs who do not fully trust AI-generated code\n(SonarSource, Jan 2026)',
    'Construction estimating still done in Excel\n(PremierCS, 2026)',
    'Opportunity data reps collect that never\nenters the CRM (DevRev, 2026)',
    'Employees who see no purpose in their intranet\n(Firstup, Jun 2024)',
    'Data practitioners spending >20% of time on\ndata-stack complexity (Modern Data Co., 2025)',
    'Devs who always verify AI-generated code\nbefore committing (SonarSource, Jan 2026)',
]
values = [96, 85, 79, 57, 63, 48]
# Same hue, lightness differentiation: the one "behavioral" stat (verify) lighter
colors = [ACCENT, ACCENT, ACCENT, ACCENT, ACCENT, LIGHT]

fig, ax = plt.subplots(figsize=(8.4, 3.6), constrained_layout=True)
y = range(len(labels))
bars = ax.barh(y, values, height=0.62, color=colors, edgecolor='none')
ax.set_yticks(list(y))
ax.set_yticklabels(labels, fontsize=8.6)
ax.invert_yaxis()
ax.set_xlim(0, 108)
ax.set_xlabel('Share of surveyed practitioners (%)', fontsize=9)

# Spines: delete top/right (mandatory), left optional -> hidden (categories labeled)
for side in ('top', 'right', 'left'):
    ax.spines[side].set_visible(False)
ax.spines['bottom'].set_color(BORDER)
ax.spines['bottom'].set_linewidth(0.8)
# Values labeled directly -> grid deleted entirely (charts.md rule)
ax.grid(False)
ax.tick_params(axis='y', length=0)
ax.tick_params(axis='x', labelsize=8.5)

for rect, v in zip(bars, values):
    ax.text(v + 1.5, rect.get_y() + rect.get_height() / 2,
            f'{v}%', va='center', ha='left', fontsize=9.5,
            color=TEXT, fontweight='bold')

fig.savefig(os.path.join(OUT_DIR, 'chart1_pain.png'), dpi=200)
plt.close(fig)

# ----------------------------------------------------------------------------
# Chart 2 - AI-era escalation (two panels, 2 bars each, values labeled -> no grid)
# ----------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.1), constrained_layout=True)

# Panel A: documented AI incidents
a_vals = [233, 362]
a_x = ['2024', '2025']
bars_a = ax1.bar(a_x, a_vals, width=0.5, color=[LIGHT, DARK], edgecolor='none')
ax1.set_ylabel('Documented AI incidents', fontsize=9)
ax1.set_ylim(0, 430)
for side in ('top', 'right'):
    ax1.spines[side].set_visible(False)
ax1.spines['left'].set_color(BORDER)
ax1.spines['bottom'].set_color(BORDER)
ax1.grid(False)
ax1.tick_params(labelsize=9)
for rect, v in zip(bars_a, a_vals):
    ax1.text(rect.get_x() + rect.get_width() / 2, v + 10, str(v),
             ha='center', va='bottom', fontsize=10, color=TEXT, fontweight='bold')

# Panel B: enterprise LLM API spend
b_vals = [3.5, 8.4]
bars_b = ax2.bar(a_x, b_vals, width=0.5, color=[LIGHT, DARK], edgecolor='none')
ax2.set_ylabel('Enterprise LLM API spend ($B)', fontsize=9)
ax2.set_ylim(0, 10.2)
for side in ('top', 'right'):
    ax2.spines[side].set_visible(False)
ax2.spines['left'].set_color(BORDER)
ax2.spines['bottom'].set_color(BORDER)
ax2.grid(False)
ax2.tick_params(labelsize=9)
for rect, v in zip(bars_b, b_vals):
    ax2.text(rect.get_x() + rect.get_width() / 2, v + 0.22, f'${v}B',
             ha='center', va='bottom', fontsize=10, color=TEXT, fontweight='bold')

fig.savefig(os.path.join(OUT_DIR, 'chart2_escalation.png'), dpi=200)
plt.close(fig)

print('charts written to', OUT_DIR)
for f in sorted(os.listdir(OUT_DIR)):
    print(' -', f, os.path.getsize(os.path.join(OUT_DIR, f)), 'bytes')
