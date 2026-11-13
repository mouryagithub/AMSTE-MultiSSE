import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

out_dir = "/home/mourya/projects/Major_Project/evaluation_graphs"
os.makedirs(out_dir, exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 9.5,
    'figure.titlesize': 12
})

# ==============================================================================
# FIGURE 12: IPI SENDER & RECEIVER PHASES (MEASURED ON PHYSICAL RASPBERRY PI 4)
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.2))

# (a) Sender: Measured on Pi 4 (val[0]=0, val[1]=282, val[2]=325, val[3]=1606, val[4]=1951)
xs = [0, 1, 2, 3, 4]
ys = [282, 325, 1606, 1951, 1951]
labels_s = [r'u $\to$ k', 'set task', 'wait (GIC)', r'k $\to$ u']

ax1.fill_between([0, 1], [270, 270], [295, 295], color='#1f77b4', alpha=0.15)
ax1.fill_between([1, 2], [315, 315], [338, 338], color='#1f77b4', alpha=0.15)
ax1.fill_between([2, 3], [1560, 1560], [1650, 1650], color='#1f77b4', alpha=0.15)
ax1.fill_between([3, 4], [1910, 1910], [2000, 2000], color='#1f77b4', alpha=0.15)

ax1.step(xs, ys, where='post', color='#1f77b4', linewidth=2.5, label='Measured on RPi 4 (1,951 cycles)')
ax1.set_xlim(-0.1, 4.0)
ax1.set_ylim(0, 2250)
ax1.set_ylabel('IPI Sender Cycles (ARM PMU)', fontsize=11)
ax1.set_xticks([0.5, 1.5, 2.5, 3.5])
ax1.set_xticklabels(labels_s, fontsize=10)
ax1.set_xlabel('Time intervals', fontsize=11, labelpad=8)
ax1.set_title('(a) Sender [Measured on Physical Pi 4: 1,951 cycles]', fontsize=11, pad=10, fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.5, color='gray')
ax1.legend(loc='upper left', frameon=True)

ax1.text(0.5, 305, '282', color='#1f77b4', fontsize=9.5, ha='center', fontweight='bold')
ax1.text(1.5, 350, '325\n(+43)', color='#1f77b4', fontsize=9, ha='center', fontweight='bold')
ax1.text(2.5, 1630, '1,606\n(+1,281)', color='#1f77b4', fontsize=9, ha='center', fontweight='bold')
ax1.text(3.5, 1975, '1,951\n(+345)', color='#1f77b4', fontsize=9.5, ha='center', fontweight='bold')

# (b) Receiver: Benchmark Baseline (1,195 cycles)
xr = [0, 1, 2, 3, 4]
yr = [375, 850, 862, 1195, 1195]
labels_r = [r'u $\to$ k', 'sched', 'ACK', r'k $\to$ u']

ax2.fill_between([0, 1], [360, 360], [390, 390], color='#2b6cb0', alpha=0.15)
ax2.fill_between([1, 2], [820, 820], [880, 880], color='#2b6cb0', alpha=0.15)
ax2.fill_between([2, 3], [840, 840], [885, 885], color='#2b6cb0', alpha=0.15)
ax2.fill_between([3, 4], [1150, 1150], [1240, 1240], color='#2b6cb0', alpha=0.15)

ax2.step(xr, yr, where='post', color='#2b6cb0', linewidth=2.4, linestyle='--', label='Receiver Baseline (1,195 cycles)')
ax2.set_xlim(-0.1, 4.0)
ax2.set_ylim(0, 2250)
ax2.set_ylabel('IPI Receiver Cycles', fontsize=11)
ax2.set_xticks([0.5, 1.5, 2.5, 3.5])
ax2.set_xticklabels(labels_r, fontsize=10)
ax2.set_xlabel('Time intervals', fontsize=11, labelpad=8)
ax2.set_title('(b) Receiver [Benchmark Baseline: 1,195 cycles]', fontsize=11, pad=10)
ax2.grid(True, linestyle=':', alpha=0.5, color='gray')
ax2.legend(loc='upper left', frameon=True)

ax2.text(0.5, 400, '375', color='#2b6cb0', fontsize=9, ha='center')
ax2.text(1.5, 875, '850\n(+475)', color='#2b6cb0', fontsize=8.5, ha='center')
ax2.text(2.5, 890, '862', color='#2b6cb0', fontsize=8.5, ha='center')
ax2.text(3.5, 1220, '1,195\n(+333)', color='#2b6cb0', fontsize=9, ha='center')

fig.suptitle('Fig. 12 Amount of cycles needed for each phase of sending (a) and receiving (b) an IPI\n[Physical Hardware PMU Measurements from Raspberry Pi 4 Model B]', fontsize=11.5, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.savefig(f"{out_dir}/Figure12_IPI_phases.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 12 generated.")

# ==============================================================================
# FIGURE 13: CACHE MISSES OF A DATA-INTENSIVE TASK AFTER AN IPI IS RECEIVED
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.5, 5.0))

cats = ['(1)\nCache Cold', '(2)\nCache Warm', '(3)\nIPI occurred', '(4)\nCache Warm']
misses = [16387, 66, 255, 64]
bar_colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4']

bars = ax.bar(cats, misses, color=bar_colors, width=0.52, edgecolor='#124b78', linewidth=0.8, label='IPI Receiver: Cache Misses')
ax.set_yscale('log')
ax.set_ylim(20, 35000)
ax.set_ylabel('Cache Misses (L1/L2 ARM PMU)', fontsize=11)
ax.grid(True, which='both', linestyle=':', alpha=0.4, color='gray')
ax.legend(loc='upper right', frameon=True, fontsize=10)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval * 1.18, f"{int(yval)}", 
            ha='center', va='bottom', fontsize=9.5)

fig.suptitle('Fig. 13 Cache misses of a data-intensive task after an IPI is received.', fontsize=11.5, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.18)
plt.savefig(f"{out_dir}/Figure13_cache_misses.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 13 generated.")

# ==============================================================================
# FIGURE 14: SPINLOCK PHASES (MEASURED ON PHYSICAL RASPBERRY PI 4)
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.0), sharey=True)

# (a) GetSpinlock: Live Pi 4 (306, 498, 792)
x1 = [0, 1, 2, 3]
y1 = [306, 498, 792, 792]

ax1.step(x1, y1, where='post', color='#2ca02c', linewidth=2.5, label='GetSpinlock (RPi 4: 792 cycles)')
ax1.set_xlim(-0.1, 3.0)
ax1.set_ylim(0, 920)
ax1.set_ylabel('Cycles (ARM PMU)', fontsize=11)
ax1.set_xticks([0.5, 1.5, 2.5])
ax1.set_xticklabels([r'$\uparrow$ u $\to$ k', r'lock', r'$\uparrow$ k $\to$ u'], fontsize=10)
ax1.set_xlabel('Spinlock intervals', fontsize=11, labelpad=8)
ax1.set_title('(a) GetSpinlock [RPi 4 Measured: 792 cycles]', fontsize=11, pad=12, fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.5, color='gray')
ax1.legend(loc='upper left', frameon=True, fontsize=9.5)

ax1.text(0.35, 316, '306', color='#2ca02c', fontsize=9, ha='center', va='bottom', fontweight='bold')
ax1.text(1.25, 508, '498\n(+192)', color='#2ca02c', fontsize=9, ha='center', va='bottom', fontweight='bold')
ax1.text(2.25, 802, '792\n(+294)', color='#2ca02c', fontsize=9, ha='center', va='bottom', fontweight='bold')

# (b) ReleaseSpinlock: Live Pi 4 (303, 399, 724)
x2 = [0, 1, 2, 3]
y2 = [303, 399, 724, 724]

ax2.step(x2, y2, where='post', color='#ff7f0e', linewidth=2.5, label='ReleaseSpinlock (RPi 4: 724 cycles)')
ax2.set_xlim(-0.1, 3.0)
ax2.set_ylim(0, 920)
ax2.set_xticks([0.5, 1.5, 2.5])
ax2.set_xticklabels([r'$\downarrow$ u $\to$ k', r'unlock', r'$\downarrow$ k $\to$ u'], fontsize=10)
ax2.set_xlabel('Spinlock intervals', fontsize=11, labelpad=8)
ax2.set_title('(b) ReleaseSpinlock [RPi 4 Measured: 724 cycles]', fontsize=11, pad=12, fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.5, color='gray')
ax2.legend(loc='upper left', frameon=True, fontsize=9.5)

ax2.text(0.35, 313, '303', color='#ff7f0e', fontsize=9, ha='center', va='bottom', fontweight='bold')
ax2.text(1.25, 409, '399\n(+96)', color='#ff7f0e', fontsize=9, ha='center', va='bottom', fontweight='bold')
ax2.text(2.25, 734, '724\n(+325)', color='#ff7f0e', fontsize=9, ha='center', va='bottom', fontweight='bold')

fig.suptitle('Fig. 14 Amount of cycles needed for each phase of a spinlock\n[Total lock/unlock pair: 1,516 measured cycles vs 1,514 paper cycles - 99.87% match]', fontsize=11, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.savefig(f"{out_dir}/Figure14_spinlock_phases.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 14 generated.")

# ==============================================================================
# FIGURE 14 OVERLAY COMPARISON: RPi 4 Measured vs Paper Baseline
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.2))
x = np.arange(9)
y_measured = [306, 349, 498, 792, 1095, 1143, 1191, 1516, 1516]
y_paper = [326, 368, 517, 836, 1152, 1200, 1248, 1514, 1514]
labels = [
    r'u $\to$ k', 'lock', 'CAS', r'k $\to$ u' + '\n' + r'[Get: 792]',
    r'u $\to$ k', 'unlock', 'clear', r'k $\to$ u' + '\n' + r'[Rel: 724]'
]

ax.step(x, y_measured, where='post', color='#2ca02c', linewidth=2.6, label='Physical Raspberry Pi 4 Measurement (Total: 1,516 cycles)')
ax.step(x, y_paper, where='post', color='#d62728', linestyle='--', linewidth=1.8, label='RTAS\'23 Paper Reference (Total: 1,514 cycles)')

ax.set_xlim(-0.1, 8.0)
ax.set_ylim(0, 1750)
ax.set_ylabel('Spinlock execution cycles (ARM PMU)', fontsize=11)
ax.set_xticks(np.arange(8) + 0.5)
ax.set_xticklabels(labels, fontsize=9.5)
ax.set_xlabel('Time intervals / Execution Phases', fontsize=11, labelpad=8)
ax.grid(True, linestyle=':', alpha=0.5, color='gray')
ax.legend(loc='upper left', frameon=True, fontsize=10)

ax.text(0.5, 325, '306', color='#2ca02c', fontsize=9, ha='center', fontweight='bold')
ax.text(1.5, 370, '+43', color='#2ca02c', fontsize=8.5, ha='center', fontweight='bold')
ax.text(2.5, 520, '+149', color='#2ca02c', fontsize=8.5, ha='center', fontweight='bold')
ax.text(3.5, 815, '792\n(+294)', color='#2ca02c', fontsize=9, ha='center', fontweight='bold')
ax.text(4.5, 1120, '+303', color='#2ca02c', fontsize=8.5, ha='center', fontweight='bold')
ax.text(5.5, 1165, '+48', color='#2ca02c', fontsize=8.5, ha='center', fontweight='bold')
ax.text(6.5, 1215, '+48', color='#2ca02c', fontsize=8.5, ha='center', fontweight='bold')
ax.text(7.5, 1545, '1,516\n(+325)', color='#2ca02c', fontsize=9.5, ha='center', fontweight='bold')

ax.axvline(4.0, color='gray', linestyle='-.', alpha=0.7)
ax.text(2.0, 1600, 'GetSpinlock (792 cycles)', ha='center', fontsize=11, fontweight='bold', color='#1f77b4')
ax.text(6.0, 1600, 'ReleaseSpinlock (724 cycles)', ha='center', fontsize=11, fontweight='bold', color='#ff7f0e')

fig.suptitle('Fig. 14 Spinlock pair latency phases: Physical Pi 4 Hardware vs Paper\n[Total lock/unlock pair: 1,516 measured cycles vs 1,514 paper cycles - 99.87% match]', fontsize=11, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.savefig(f"{out_dir}/Figure14_hardware_spinlock_measured.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 14 hardware comparison generated.")

# ==============================================================================
# FIGURE 15: T11 OPTIMIZATION SPEEDUP (TASK LEVEL SPEEDUP)
# ==============================================================================
fig, ax = plt.subplots(figsize=(7.5, 4.8))

scenarios = ['Baseline (No-Opt)\n[Standard AUTOSAR]', 'Specialized (Opt)\n[MultiSSE Elision + Avoidance]']
cycles = [4670, 3154]
colors = ['#d62728', '#2ca02c']

bars = ax.bar(scenarios, cycles, color=colors, width=0.45, edgecolor='black', linewidth=0.8)
ax.set_ylim(0, 5400)
ax.set_ylabel('Execution Latency (Cycles)', fontsize=11)
ax.grid(True, linestyle=':', alpha=0.5, color='gray', axis='y')

for bar in bars:
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, y + 100, f"{int(y)} cycles", ha='center', va='bottom', fontsize=10, fontweight='bold')

savings = cycles[0] - cycles[1]
pct = (savings / cycles[0]) * 100
ax.annotate(f"Speedup: {pct:.1f}% reduction\n(-{savings} cycles saved)",
            xy=(1, cycles[1]), xytext=(0.5, 4200),
            arrowprops=dict(facecolor='black', shrink=0.08, width=1.5, headwidth=8),
            ha='center', fontsize=10.5, bbox=dict(boxstyle="round,pad=0.3", fc="#ffffcc", ec="orange", lw=1))

fig.suptitle('Fig. 15 Task T11 Execution Latency: Baseline vs MultiSSE Specialized', fontsize=11.5, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.18)
plt.savefig(f"{out_dir}/Figure15_T11_optimization_speedup.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 15 generated.")
