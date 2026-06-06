import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

with open("experiment_results.json") as f:
    data = json.load(f)

budgets = list(data.keys())
labels_short = ["4 juta", "8 juta", "15 juta"]
algs = ["greedy", "bnb", "ga"]
alg_labels = ["Greedy", "Branch & Bound", "Genetic Algorithm"]
colors = ["#2196F3", "#F44336", "#4CAF50"]

# ============================================================
# FIGURE 1: Perbandingan Performance Score per Budget
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(budgets))
width = 0.25

for i, (alg, label, color) in enumerate(zip(algs, alg_labels, colors)):
    perfs = [data[b][alg]["perf"] for b in budgets]
    bars = ax.bar(x + i * width, perfs, width, label=label, color=color, alpha=0.85, edgecolor='white')
    for bar, val in zip(bars, perfs):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}', ha='center', va='bottom', fontsize=8.5, fontweight='bold')

ax.set_xlabel("Skenario Budget", fontsize=11)
ax.set_ylabel("Rata-rata Skor Performa", fontsize=11)
ax.set_title("Perbandingan Rata-rata Skor Performa Komponen\nper Skenario Budget dan Algoritma", fontsize=12, fontweight='bold')
ax.set_xticks(x + width)
ax.set_xticklabels(labels_short)
ax.set_ylim(0, 105)
ax.legend(loc='upper left', fontsize=9)
ax.grid(axis='y', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("fig1_performance_comparison.png", dpi=150, bbox_inches='tight')
plt.close()
print("Fig 1 saved")

# ============================================================
# FIGURE 2: Perbandingan Waktu Eksekusi (log scale)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
for i, (alg, label, color) in enumerate(zip(algs, alg_labels, colors)):
    times = [data[b][alg]["time_ms"] for b in budgets]
    ax.plot(labels_short, times, marker='o', label=label, color=color, linewidth=2.5,
            markersize=8, markeredgecolor='white', markeredgewidth=1.5)
    for j, (x_pt, t) in enumerate(zip(labels_short, times)):
        ax.annotate(f'{t:.2f}ms', (x_pt, t), textcoords="offset points",
                    xytext=(5, 5), fontsize=8.5, color=color)

ax.set_xlabel("Skenario Budget", fontsize=11)
ax.set_ylabel("Waktu Eksekusi (ms) — Skala Log", fontsize=11)
ax.set_title("Perbandingan Waktu Eksekusi Algoritma\nper Skenario Budget", fontsize=12, fontweight='bold')
ax.set_yscale('log')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("fig2_time_comparison.png", dpi=150, bbox_inches='tight')
plt.close()
print("Fig 2 saved")

# ============================================================
# FIGURE 3: Konvergensi Genetic Algorithm (budget 8 juta)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
conv_8 = data["Budget Sedang (8 juta)"]["ga"]["convergence"]
conv_4 = data["Budget Ketat (4 juta)"]["ga"]["convergence"]
conv_15 = data["Budget Longgar (15 juta)"]["ga"]["convergence"]
gens = list(range(1, len(conv_8) + 1))

for conv, label, color in [(conv_4, "Budget 4 juta", "#2196F3"),
                            (conv_8, "Budget 8 juta", "#FF9800"),
                            (conv_15, "Budget 15 juta", "#4CAF50")]:
    ax.plot(gens, conv, label=label, color=color, linewidth=2, alpha=0.85)

ax.set_xlabel("Generasi", fontsize=11)
ax.set_ylabel("Fitness Terbaik", fontsize=11)
ax.set_title("Kurva Konvergensi Genetic Algorithm\npada Tiga Skenario Budget", fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("fig3_ga_convergence.png", dpi=150, bbox_inches='tight')
plt.close()
print("Fig 3 saved")

# ============================================================
# FIGURE 4: Budget Utilized vs Budget Available
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
budget_vals = [4_000_000, 8_000_000, 15_000_000]

for i, (alg, label, color) in enumerate(zip(algs, alg_labels, colors)):
    costs = [data[b][alg]["cost"] for b in budgets]
    ratios = [c / bv * 100 for c, bv in zip(costs, budget_vals)]
    ax.plot(labels_short, ratios, marker='s', label=label, color=color, linewidth=2.5,
            markersize=8, markeredgecolor='white', markeredgewidth=1.5)

ax.axhline(y=100, color='gray', linestyle='--', linewidth=1.5, label='Batas Budget (100%)')
ax.set_xlabel("Skenario Budget", fontsize=11)
ax.set_ylabel("Persentase Budget Terpakai (%)", fontsize=11)
ax.set_title("Efisiensi Penggunaan Budget\nper Algoritma dan Skenario", fontsize=12, fontweight='bold')
ax.set_ylim(0, 130)
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("fig4_budget_utilization.png", dpi=150, bbox_inches='tight')
plt.close()
print("Fig 4 saved")
print("All figures generated!")
