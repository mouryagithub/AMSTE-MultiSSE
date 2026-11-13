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
# Real Hardware PMU Measurements from putty_spinlock_uart.txt (RPi 4 Cortex-A72):
# (a) GetSpinlock: u->k (306), lock (498, +192), k->u (792, +294) -> Total: 792 cycles
# (b) ReleaseSpinlock: u->k (335), unlock (409, +74), k->u (756, +347) -> Total: 756 cycles
# Total Spinlock Pair Latency: 1,548 cycles
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
y2 = [335, 409, 756, 756]
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

ax2.text(0.4, 345, '335', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')
ax2.text(1.25, 420, '409\n(+74)', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')
ax2.text(2.25, 770, '756\n(+347)', color='#1f77b4', fontsize=9.5, ha='center', va='bottom')

fig.suptitle('Fig. 14 Amount of cycles needed for each phase of a spinlock (see Fig. 11)', fontsize=11, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.savefig(f"{out_dir}/Figure14_spinlock_phases.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 14 generated.")

# ==============================================================================
# FIGURE 12: AMOUNT OF CYCLES NEEDED FOR EACH PHASE OF SENDING (a) AND RECEIVING (b) AN IPI
# Real Hardware PMU Measurements from putty_uart.txt (RPi 4 Cortex-A72, 5 boots):
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))

# (a) Sender: Mean values and exact physical variance bands across 5 boots
xs = [0, 1, 2, 3, 4]
ys = [285, 328, 1588, 1921, 1921]
labels_s = [r'$\uparrow u \to k$', 'set task', 'wait', r'$\uparrow k \to u$']

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
# FIGURE 13: CACHE MISSES OF A DATA-INTENSIVE TASK AFTER AN IPI IS RECEIVED (Fig. 13)
# Real Hardware PMU Measurements from putty_cache_uart across 5 boots (RPi 4 Cortex-A72):
# (1) Cold: 16,387 misses (1MB / 64B cache line stride)
# (2) Warm: 71 misses (Settled post-warmup)
# (3) IPI occurred: 166 misses (L1 cache lines evicted by GIC interrupt handler)
# (4) Warm: 76 misses (Settled post-IPI)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.0, 4.4))

cats = ['(1)\nCache Cold', '(2)\nCache Warm', '(3)\nIPI occurred', '(4)\nCache Warm']
# Exact empirical averages from physical Pi 4 putty_cache_uart
misses = [16387, 71, 166, 76]
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
# FIGURE 15: OPTIMIZED EXECUTION TIME OF TASK T11 (Fig. 15)
# Combines measured Spinlock savings (1,548 cycles) and IPI savings (1,921 cycles)
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 4.6))

abbs = ['09+10\nGL(S1)', '11+12\nRL(S1)', '13+14\nAT(T02)', '15+16\nAT(T01)', '17+18\nAT(T21)']
x_indices = [0, 1, 2, 3, 4, 5]

y_noopt = [792, 1548, 3469, 5149, 7070, 7070]
y_opt = [68, 136, 2057, 2699, 4620, 4620]

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
ax.text(1.5, 1590, '+756', color='#1f77b4', fontsize=9, ha='center')
ax.text(2.5, 3520, '+1921', color='#1f77b4', fontsize=9, ha='center')
ax.text(3.5, 5200, '+1680', color='#1f77b4', fontsize=9, ha='center')
ax.text(4.5, 7120, '7070', color='#1f77b4', fontsize=9, ha='center', fontweight='bold')

ax.text(0.5, 100, '68', color='#ff7f0e', fontsize=9, ha='center')
ax.text(1.5, 175, '+68', color='#ff7f0e', fontsize=9, ha='center')
ax.text(2.5, 2110, '+1921', color='#ff7f0e', fontsize=9, ha='center')
ax.text(3.5, 2750, '+642 (IPI omitted)', color='#ff7f0e', fontsize=9, ha='center')
ax.text(4.5, 4675, '4620 (-34.6%)', color='#ff7f0e', fontsize=9, ha='center', fontweight='bold')

fig.suptitle('Fig. 15 Optimized execution time of the example application Task T11.\nThe execution time is reduced by Lock Elision in ABB10/12 and omitting the IPI in ABB16.\nThe BCET is subtracted on the y-axis to make the difference between the times more visible', fontsize=9.5, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.22)
plt.savefig(f"{out_dir}/Figure15_T11_optimization_speedup.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 15 generated.")
