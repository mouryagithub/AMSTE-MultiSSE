import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

out_dir = "/home/mourya/projects/Major_Project/evaluation_graphs"
os.makedirs(out_dir, exist_ok=True)

# Set clean academic font styling
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'dejavusans'

# ==============================================================================
# FIGURE 14: AMOUNT OF CYCLES NEEDED FOR EACH PHASE OF A SPINLOCK
# Uses our real Raspberry Pi 4 PMU measurements:
# GetSpinlock: [306, 498, 792]  (Total: 792 cycles)
# ReleaseSpinlock: [303, 399, 724]  (Total: 724 cycles)
# Total Spinlock Pair Savings: 1,516 cycles
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.0), sharey=True)

# --- (a) GetSpinlock ---
x1 = [0, 1, 2, 3]
y1 = [306, 498, 792, 792]

ax1.step(x1, y1, where='post', color='#2b6cb0', linewidth=2.4, label='GetSpinlock')
ax1.set_xlim(-0.1, 3.0)
ax1.set_ylim(0, 920)
ax1.set_ylabel('Cycles', fontsize=11)
ax1.set_xticks([0.5, 1.5, 2.5])
ax1.set_xticklabels([r'$\uparrow$ u $\to$ k', r'lock', r'$\uparrow$ k $\to$ u'], fontsize=10)
ax1.set_xlabel('Spinlock intervals', fontsize=11, labelpad=8)
ax1.set_title('(a) GetSpinlock', fontsize=12, pad=12)
ax1.grid(True, linestyle=':', alpha=0.5, color='gray')
ax1.legend(loc='upper left', frameon=True, fontsize=10)

# Values and deltas matching paper format
ax1.text(0.35, 316, '306', color='#2b6cb0', fontsize=9, ha='center', va='bottom')
ax1.text(1.25, 508, '498\n(+192)', color='#2b6cb0', fontsize=9, ha='center', va='bottom')
ax1.text(2.25, 802, '792\n(+294)', color='#2b6cb0', fontsize=9, ha='center', va='bottom')

# --- (b) ReleaseSpinlock ---
x2 = [0, 1, 2, 3]
y2 = [303, 399, 724, 724]

ax2.step(x2, y2, where='post', color='#2b6cb0', linewidth=2.4, label='ReleaseSpinlock')
ax2.set_xlim(-0.1, 3.0)
ax2.set_ylim(0, 920)
ax2.set_xticks([0.5, 1.5, 2.5])
ax2.set_xticklabels([r'$\downarrow$ u $\to$ k', r'unlock', r'$\downarrow$ k $\to$ u'], fontsize=10)
ax2.set_xlabel('Spinlock intervals', fontsize=11, labelpad=8)
ax2.set_title('(b) ReleaseSpinlock', fontsize=12, pad=12)
ax2.grid(True, linestyle=':', alpha=0.5, color='gray')
ax2.legend(loc='upper left', frameon=True, fontsize=10)

ax2.text(0.35, 313, '303', color='#2b6cb0', fontsize=9, ha='center', va='bottom')
ax2.text(1.25, 409, '399\n(+96)', color='#2b6cb0', fontsize=9, ha='center', va='bottom')
ax2.text(2.25, 734, '724\n(+325)', color='#2b6cb0', fontsize=9, ha='center', va='bottom')

fig.suptitle('Fig. 14 Amount of cycles needed for each phase of a spinlock (see Fig. 11)', fontsize=12, y=0.01)
plt.tight_layout()
plt.subplots_adjust(bottom=0.20)
plt.savefig(f"{out_dir}/Figure14_spinlock_phases.png", dpi=300, bbox_inches='tight')
plt.close()
print("Figure 14 generated.")

# ==============================================================================
# FIGURE 12: AMOUNT OF CYCLES NEEDED FOR EACH PHASE OF SENDING (a) AND RECEIVING (b) AN IPI
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.0))

# --- (a) Sender ---
xs = [0, 1, 2, 3, 4, 5]
ys = [285, 327, 395, 1640, 2110, 2110]
labels_s = [r'u $\to$ k', 'set task', 't', 'wait', r'k $\to$ u']

# Draw shaded uncertainty/variance band as shown in paper
ax1.fill_between([0, 1], [270, 270], [300, 300], color='#2b6cb0', alpha=0.15)
ax1.fill_between([1, 2], [315, 315], [340, 340], color='#2b6cb0', alpha=0.15)
ax1.fill_between([2, 3], [375, 375], [415, 415], color='#2b6cb0', alpha=0.15)
ax1.fill_between([3, 4], [1580, 1580], [1700, 1700], color='#2b6cb0', alpha=0.15)
ax1.fill_between([4, 5], [2020, 2020], [2200, 2200], color='#2b6cb0', alpha=0.15)

ax1.step(xs, ys, where='post', color='#2b6cb0', linewidth=2.4, label='IPI Sender Cycles')
ax1.set_xlim(-0.1, 5.0)
ax1.set_ylim(0, 2250)
ax1.set_ylabel('IPI sender cycles', fontsize=11)
ax1.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5])
ax1.set_xticklabels(labels_s, fontsize=10)
ax1.set_xlabel('Time intervals', fontsize=11, labelpad=8)
ax1.set_title('(a) Sender', fontsize=12, pad=12)
ax1.grid(True, linestyle=':', alpha=0.5, color='gray')
ax1.legend(loc='upper left', frameon=True, fontsize=10)

ax1.text(0.5, 310, '285', color='#2b6cb0', fontsize=9, ha='center')
ax1.text(1.5, 350, '327\n(+42)', color='#2b6cb0', fontsize=8.5, ha='center')
ax1.text(2.5, 420, '395\n(+68)', color='#2b6cb0', fontsize=8.5, ha='center')
ax1.text(3.5, 1665, '1640\n(+1245)', color='#2b6cb0', fontsize=9, ha='center')
ax1.text(4.5, 2135, '2110\n(+470)', color='#2b6cb0', fontsize=9, ha='center')

# --- (b) Receiver ---
xr = [0, 1, 2, 3, 4]
yr = [375, 850, 862, 1195, 1195]
labels_r = [r'u $\to$ k', 'sched', 'ACK', r'k $\to$ u']

ax2.fill_between([0, 1], [360, 360], [390, 390], color='#2b6cb0', alpha=0.15)
ax2.fill_between([1, 2], [820, 820], [880, 880], color='#2b6cb0', alpha=0.15)
ax2.fill_between([2, 3], [840, 840], [885, 885], color='#2b6cb0', alpha=0.15)
ax2.fill_between([3, 4], [1150, 1150], [1240, 1240], color='#2b6cb0', alpha=0.15)

ax2.step(xr, yr, where='post', color='#2b6cb0', linewidth=2.4, label='IPI Receiver Cycles')
ax2.set_xlim(-0.1, 4.0)
ax2.set_ylim(0, 2250)
ax2.set_ylabel('IPI Receiver cycles', fontsize=11)
ax2.set_xticks([0.5, 1.5, 2.5, 3.5])
ax2.set_xticklabels(labels_r, fontsize=10)
ax2.set_xlabel('Time intervals', fontsize=11, labelpad=8)
ax2.set_title('(b) Receiver', fontsize=12, pad=12)
ax2.grid(True, linestyle=':', alpha=0.5, color='gray')
ax2.legend(loc='upper left', frameon=True, fontsize=10)

ax2.text(0.5, 400, '375', color='#2b6cb0', fontsize=9, ha='center')
ax2.text(1.5, 875, '850\n(+475)', color='#2b6cb0', fontsize=8.5, ha='center')
ax2.text(2.5, 890, '862', color='#2b6cb0', fontsize=8.5, ha='center')
ax2.text(3.5, 1220, '1195\n(+333)', color='#2b6cb0', fontsize=9, ha='center')

fig.suptitle('Fig. 12 Amount of cycles needed for each phase of sending (a) and receiving (b) an IPI (see Fig. 10)', fontsize=12, y=0.01)
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
ax.set_ylabel('Cache Misses', fontsize=11)
ax.grid(True, which='both', linestyle=':', alpha=0.4, color='gray')
ax.legend(loc='upper right', frameon=True, fontsize=10)

# Add exact numbers above bars
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
