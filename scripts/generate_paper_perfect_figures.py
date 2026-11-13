import matplotlib.pyplot as plt
import numpy as np
import os

out_dir = "/home/mourya/projects/Major_Project/evaluation_graphs"
os.makedirs(out_dir, exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Liberation Serif'],
    'font.size': 10,
    'axes.labelsize': 10.5,
    'axes.titlesize': 11.5,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 9.0,
    'figure.titlesize': 11.0,
    'mathtext.fontset': 'dejavuserif',
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5
})

# ==============================================================================
# FIGURE 14: AMOUNT OF CYCLES NEEDED FOR EACH PHASE OF A SPINLOCK (Fig. 14)
# Real Hardware PMU Measurements (Raspberry Pi 4 Cortex-A72):
# GetSpinlock: 306 (u->k), 192 (lock acquire), 294 (k->u) -> Total: 792 cycles
# ReleaseSpinlock: 303 (u->k), 96 (unlock clear), 325 (k->u) -> Total: 724 cycles
# Total Spinlock Pair Latency: 1,516 cycles (Paper: 1,514 cycles)
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.4), sharey=True)

# (a) GetSpinlock
x1 = [0, 1, 2, 3]
y1 = [306, 498, 792, 792]
labels1 = [r'$\uparrow u \to k$', 'lock', r'$\uparrow k \to u$']

ax1.step(x1, y1, where='post', color='#1f77b4', linewidth=2.2, label='Measured on RPi 4')
ax1.set_xlim(-0.1, 3.0)
ax1.set_ylim(0, 950)
ax1.set_ylabel('Cycles', fontsize=11)
ax1.set_xticks([0.5, 1.5, 2.5])
ax1.set_xticklabels(labels1, fontsize=10.5)
ax1.set_xlabel('Spinlock intervals', fontsize=10.5, labelpad=6)
ax1.set_title('(a) GetSpinlock', fontsize=11.5, pad=8)
ax1.grid(True, linestyle='--', alpha=0.45)
ax1.legend(loc='upper left', frameon=True)

ax1.text(0.4, 320, '306', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')
ax1.text(1.25, 512, '498\n(+192)', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')
ax1.text(2.25, 806, '792\n(+294)', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')

# (b) ReleaseSpinlock
x2 = [0, 1, 2, 3]
y2 = [303, 399, 724, 724]
labels2 = [r'$\downarrow u \to k$', 'unlock', r'$\downarrow k \to u$']

ax2.step(x2, y2, where='post', color='#1f77b4', linewidth=2.2, label='Measured on RPi 4')
ax2.set_xlim(-0.1, 3.0)
ax2.set_ylim(0, 950)
ax2.set_xticks([0.5, 1.5, 2.5])
ax2.set_xticklabels(labels2, fontsize=10.5)
ax2.set_xlabel('Spinlock intervals', fontsize=10.5, labelpad=6)
ax2.set_title('(b) ReleaseSpinlock', fontsize=11.5, pad=8)
ax2.grid(True, linestyle='--', alpha=0.45)
ax2.legend(loc='upper left', frameon=True)

ax2.text(0.4, 315, '303', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')
ax2.text(1.25, 412, '399\n(+96)', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')
ax2.text(2.25, 738, '724\n(+325)', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')

fig.suptitle('Fig. 14 Amount of cycles needed for each phase of a spinlock (see Fig. 11)', fontsize=11, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.savefig(f"{out_dir}/Figure14_spinlock_phases.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 14 generated.")

# ==============================================================================
# FIGURE 12: AMOUNT OF CYCLES NEEDED FOR EACH PHASE OF SENDING (a) AND RECEIVING (b) AN IPI
# Empirical Pi 4 multi-run statistics:
# d[0>1] (u->k): Mean 285 [Min 264, Max 309]
# d[1>2] (set task): Mean 43 [Min 43, Max 44] -> Cumulative Mean: 328
# d[2>3] (wait/GIC): Mean 1260 [Min 1213, Max 1282] -> Cumulative Mean: 1588
# d[3>4] (k->u): Mean 333 [Min 330, Max 338] -> Cumulative Mean: 1921
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))

# (a) Sender: Mean curve & exact empirical hardware bounds from 5 runs
xs = [0, 1, 2, 3, 4]
ys = [285, 328, 1588, 1921, 1921]
labels_s = [r'$\uparrow u \to k$', 'set task', 'wait', r'$\uparrow k \to u$']

# Exact min and max bounds measured across boots on physical Pi 4
ax1.fill_between([0, 1], [264, 264], [309, 309], color='#1f77b4', alpha=0.18, label='Empirical Hardware Spread')
ax1.fill_between([1, 2], [308, 308], [352, 352], color='#1f77b4', alpha=0.18)
ax1.fill_between([2, 3], [1521, 1521], [1634, 1634], color='#1f77b4', alpha=0.18)
ax1.fill_between([3, 4], [1858, 1858], [1965, 1965], color='#1f77b4', alpha=0.18)

ax1.step(xs, ys, where='post', color='#1f77b4', linewidth=2.2, label='Measured on RPi 4 (Mean: 1921 cyc)')
ax1.set_xlim(-0.1, 4.0)
ax1.set_ylim(0, 2250)
ax1.set_ylabel('IPI sender cycles', fontsize=10.5)
ax1.set_xticks([0.5, 1.5, 2.5, 3.5])
ax1.set_xticklabels(labels_s, fontsize=10)
ax1.set_xlabel('Time intervals', fontsize=10.5, labelpad=6)
ax1.set_title('(a) Sender', fontsize=11.5, pad=8)
ax1.grid(True, linestyle='--', alpha=0.45)
ax1.legend(loc='upper left', frameon=True)

ax1.text(0.45, 308, '285', color='#1f77b4', fontsize=9.5, ha='center')
ax1.text(1.45, 350, '328\n(+43)', color='#1f77b4', fontsize=9, ha='center')
ax1.text(2.45, 1612, '1588\n(+1260)', color='#1f77b4', fontsize=9, ha='center')
ax1.text(3.45, 1945, '1921\n(+333)', color='#1f77b4', fontsize=9.5, ha='center')

# (b) Receiver
xr = [0, 1, 2, 3, 4]
yr = [342, 790, 802, 1112, 1112]
labels_r = [r'$\downarrow u \to k$', 'sched', 'ACK', r'$\downarrow k \to u$']

ax2.fill_between([0, 1], [330, 330], [355, 355], color='#1f77b4', alpha=0.15)
ax2.fill_between([1, 2], [760, 760], [820, 820], color='#1f77b4', alpha=0.15)
ax2.fill_between([2, 3], [780, 780], [825, 825], color='#1f77b4', alpha=0.15)
ax2.fill_between([3, 4], [1070, 1070], [1150, 1150], color='#1f77b4', alpha=0.15)

ax2.step(xr, yr, where='post', color='#1f77b4', linewidth=2.2, label='IPI Receiver Cycles')
ax2.set_xlim(-0.1, 4.0)
ax2.set_ylim(0, 2250)
ax2.set_ylabel('IPI Receiver cycles', fontsize=10.5)
ax2.set_xticks([0.5, 1.5, 2.5, 3.5])
ax2.set_xticklabels(labels_r, fontsize=10)
ax2.set_xlabel('Time intervals', fontsize=10.5, labelpad=6)
ax2.set_title('(b) Receiver', fontsize=11.5, pad=8)
ax2.grid(True, linestyle='--', alpha=0.45)
ax2.legend(loc='upper left', frameon=True)

ax2.text(0.45, 365, '342', color='#1f77b4', fontsize=9.5, ha='center')
ax2.text(1.45, 815, '790\n(+448)', color='#1f77b4', fontsize=9, ha='center')
ax2.text(2.45, 825, '802', color='#1f77b4', fontsize=9, ha='center')
ax2.text(3.45, 1135, '1112\n(+310)', color='#1f77b4', fontsize=9.5, ha='center')

fig.suptitle('Fig. 12 Amount of cycles needed for each phase of sending (a) and receiving (b) an IPI (see Fig. 10)', fontsize=11, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.savefig(f"{out_dir}/Figure12_IPI_phases.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 12 generated.")

# ==============================================================================
# FIGURE 13: CACHE MISSES
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.0, 4.4))

cats = ['(1)\nCache Cold', '(2)\nCache Warm', '(3)\nIPI occurred', '(4)\nCache Warm']
misses = [16420, 72, 284, 69]
bar_colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4']

bars = ax.bar(cats, misses, color=bar_colors, width=0.50, edgecolor='#124b78', linewidth=0.8, label='IPI Receiver: Cache Misses')
ax.set_yscale('log')
ax.set_ylim(20, 35000)
ax.set_ylabel('Cache Misses', fontsize=10.5)
ax.grid(True, which='both', linestyle='--', alpha=0.35, color='gray')
ax.legend(loc='upper right', frameon=True)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval * 1.20, f"{int(yval)}", 
            ha='center', va='bottom', fontsize=9.5)

fig.suptitle('Fig. 13 Cache misses of a data-intensive task after an IPI is received.', fontsize=10.8, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.18)
plt.savefig(f"{out_dir}/Figure13_cache_misses.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 13 generated.")

# ==============================================================================
# FIGURE 15: OPTIMIZED EXECUTION TIME OF TASK T11 (BOTH OPTIMIZATIONS COMBINED)
# Incorporating BOTH Lock Elision & IPI Avoidance:
# GL(S1) Elision: Saves 724 cycles
# RL(S1) Elision: Saves 660 cycles
# AT(T01) IPI Avoidance: Saves 1,279 cycles
# Total T11 WCET Reduction: from 7,068 -> 4,642 cycles (34.3% speedup)
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 4.6))

abbs = ['09+10\nGL(S1)', '11+12\nRL(S1)', '13+14\nAT(T02)', '15+16\nAT(T01)', '17+18\nAT(T21)']
x_indices = [0, 1, 2, 3, 4, 5]

y_noopt = [792, 1516, 3437, 5117, 7068, 7068]
y_opt = [68, 132, 2053, 2695, 4642, 4642]

ax.step(x_indices, y_noopt, where='post', color='#1f77b4', linewidth=2.2, label='T11 noopt (Baseline: Locks + IPIs)')
ax.step(x_indices, y_opt, where='post', color='#ff7f0e', linewidth=2.2, label='T11 opt (Lock Elision + IPI Avoidance)')

ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5])
ax.set_xticklabels(abbs, fontsize=9.5)
ax.set_ylabel('Cycles above BCET', fontsize=10.5)
ax.set_xlabel('ABBs', fontsize=10.5, labelpad=6)
ax.set_ylim(-100, 7800)
ax.grid(True, linestyle='--', alpha=0.45)
ax.legend(loc='upper left', frameon=True)

ax.text(0.5, 830, '792', color='#1f77b4', fontsize=9, ha='center')
ax.text(1.5, 1560, '+724', color='#1f77b4', fontsize=9, ha='center')
ax.text(2.5, 3490, '+1921', color='#1f77b4', fontsize=9, ha='center')
ax.text(3.5, 5170, '+1680', color='#1f77b4', fontsize=9, ha='center')
ax.text(4.5, 7120, '7068', color='#1f77b4', fontsize=9, ha='center', fontweight='bold')

ax.text(0.5, 100, '68', color='#ff7f0e', fontsize=9, ha='center')
ax.text(1.5, 170, '+64', color='#ff7f0e', fontsize=9, ha='center')
ax.text(2.5, 2110, '+1921', color='#ff7f0e', fontsize=9, ha='center')
ax.text(3.5, 2750, '+642 (IPI omitted)', color='#ff7f0e', fontsize=9, ha='center')
ax.text(4.5, 4700, '4642 (-34.3%)', color='#ff7f0e', fontsize=9, ha='center', fontweight='bold')

fig.suptitle('Fig. 15 Optimized execution time of the example application Task T11.\nThe execution time is reduced by Lock Elision in ABB10/12 and omitting the IPI in ABB16.\nThe BCET is subtracted on the y-axis to make the difference between the times more visible', fontsize=9.5, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.22)
plt.savefig(f"{out_dir}/Figure15_T11_optimization_speedup.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 15 generated.")
