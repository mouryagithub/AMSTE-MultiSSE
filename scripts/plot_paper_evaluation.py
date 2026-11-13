import matplotlib.pyplot as plt
import numpy as np
import os

out_dir = "/home/mourya/projects/Major_Project/evaluation_graphs"
os.makedirs(out_dir, exist_ok=True)

# -------------------------------------------------------------
# FIGURE 14: Spinlock Phases (GetSpinlock & ReleaseSpinlock)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), sharey=True)

# (a) GetSpinlock: u->k (329), lock (+100 = 429), k->u (+407 = 836)
x1 = [0, 1, 2, 3]
y1 = [329, 429, 836, 836]
labels1 = [r'$\uparrow u \to k$', 'acquire lock', r'$\uparrow k \to u$']

ax1.step(x1, y1, where='post', color='#1f77b4', linewidth=2.5, label='GetSpinlock')
ax1.set_xticks([0.5, 1.5, 2.5])
ax1.set_xticklabels(labels1, fontsize=11)
ax1.set_ylabel('Cycles', fontsize=12)
ax1.set_title('(a) GetSpinlock', fontsize=12, pad=10)
ax1.set_xlabel('Spinlock intervals', fontsize=11)
ax1.set_ylim(0, 950)
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.legend(loc='upper left', frameon=True)

# Annotate cycle step deltas
ax1.text(0.4, 340, '329', color='#1f77b4', fontsize=9, ha='center')
ax1.text(1.2, 440, '429\n(+100)', color='#1f77b4', fontsize=9, ha='center')
ax1.text(2.2, 850, '836\n(+407)', color='#1f77b4', fontsize=9, ha='center')

# (b) ReleaseSpinlock: u->k (245), unlock (+102 = 347), k->u (+331 = 678)
x2 = [0, 1, 2, 3]
y2 = [245, 347, 678, 678]
labels2 = [r'$\downarrow u \to k$', 'release lock', r'$\downarrow k \to u$']

ax2.step(x2, y2, where='post', color='#1f77b4', linewidth=2.5, label='ReleaseSpinlock')
ax2.set_xticks([0.5, 1.5, 2.5])
ax2.set_xticklabels(labels2, fontsize=11)
ax2.set_title('(b) ReleaseSpinlock', fontsize=12, pad=10)
ax2.set_xlabel('Spinlock intervals', fontsize=11)
ax2.set_ylim(0, 950)
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.legend(loc='upper left', frameon=True)

ax2.text(0.4, 255, '245', color='#1f77b4', fontsize=9, ha='center')
ax2.text(1.2, 360, '347\n(+102)', color='#1f77b4', fontsize=9, ha='center')
ax2.text(2.2, 690, '678\n(+331)', color='#1f77b4', fontsize=9, ha='center')

fig.suptitle('Fig. 14: Amount of cycles needed for each phase of a spinlock (Raspberry Pi 4)', fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig(f"{out_dir}/Figure14_spinlock_phases.png", dpi=300, bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIGURE 12: IPI Sender and Receiver Cycles
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# (a) Sender: u->k (246), set task (280, +34), IPI trigger (338, +58), wait (1420, +1082), k->u (1842, +422)
xs = [0, 1, 2, 3, 4, 5]
ys = [246, 280, 338, 1420, 1842, 1842]
labels_s = [r'$\uparrow u \to k$', 'set task', 'IPI trig', 'wait (Ack)', r'$\uparrow k \to u$']

ax1.step(xs, ys, where='post', color='#1f77b4', linewidth=2.5, label='IPI Sender Cycles')
ax1.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5])
ax1.set_xticklabels(labels_s, fontsize=10)
ax1.set_ylabel('IPI sender cycles', fontsize=12)
ax1.set_title('(a) Sender', fontsize=12, pad=10)
ax1.set_xlabel('Time intervals', fontsize=11)
ax1.set_ylim(0, 2050)
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.legend(loc='upper left', frameon=True)

ax1.text(0.5, 260, '246', color='#1f77b4', fontsize=9, ha='center')
ax1.text(1.5, 300, '280', color='#1f77b4', fontsize=9, ha='center')
ax1.text(2.5, 360, '338', color='#1f77b4', fontsize=9, ha='center')
ax1.text(3.5, 1450, '1420 (+1082)', color='#1f77b4', fontsize=9, ha='center')
ax1.text(4.5, 1870, '1842 (+422)', color='#1f77b4', fontsize=9, ha='center')

# (b) Receiver: u->k (321), sched (732, +411), ACK (741, +9), k->u (1027, +286)
xr = [0, 1, 2, 3, 4]
yr = [321, 732, 741, 1027, 1027]
labels_r = [r'$\downarrow u \to k$', 'sched', 'ACK', r'$\downarrow k \to u$']

ax2.step(xr, yr, where='post', color='#1f77b4', linewidth=2.5, label='IPI Receiver Cycles')
ax2.set_xticks([0.5, 1.5, 2.5, 3.5])
ax2.set_xticklabels(labels_r, fontsize=10)
ax2.set_ylabel('IPI Receiver cycles', fontsize=12)
ax2.set_title('(b) Receiver', fontsize=12, pad=10)
ax2.set_xlabel('Time intervals', fontsize=11)
ax2.set_ylim(0, 2050)
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.legend(loc='upper left', frameon=True)

ax2.text(0.5, 340, '321', color='#1f77b4', fontsize=9, ha='center')
ax2.text(1.5, 750, '732 (+411)', color='#1f77b4', fontsize=9, ha='center')
ax2.text(2.5, 760, '741', color='#1f77b4', fontsize=9, ha='center')
ax2.text(3.5, 1050, '1027 (+286)', color='#1f77b4', fontsize=9, ha='center')

fig.suptitle('Fig. 12: Amount of cycles needed for each phase of sending (a) and receiving (b) an IPI', fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig(f"{out_dir}/Figure12_IPI_phases.png", dpi=300, bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# FIGURE 13: Cache Misses
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4.5))

cats = ['(1)\nCache Cold', '(2)\nCache Warm', '(3)\nIPI occurred', '(4)\nCache Warm']
misses = [16387, 66, 255, 64]
colors = ['#1f77b4', '#1f77b4', '#d62728', '#1f77b4']

bars = ax.bar(cats, misses, color=colors, width=0.55, edgecolor='black', linewidth=0.8)
ax.set_yscale('log')
ax.set_ylim(20, 30000)
ax.set_ylabel('Cache Misses (Log Scale)', fontsize=12)
ax.set_title('Fig. 13: Cache misses of a data-intensive task after an IPI is received', fontsize=12, pad=12)
ax.grid(True, which='both', linestyle='--', alpha=0.3)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval * 1.15, f"{int(yval)}", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f"{out_dir}/Figure13_cache_misses.png", dpi=300, bbox_inches='tight')
plt.close()

print("ALL THREE FIGURES (12, 13, 14) GENERATED SUCCESSFULLY!")

# -------------------------------------------------------------
# FIGURE 15: Optimized execution time of Task T11 (Before vs After)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))

abbs = ['09+10\nGL(S1)', '11+12\nRL(S1)', '13+14\nAT(T02)', '15+16\nAT(T01)', '17+18\nAT(T21)']
x_indices = [0, 1, 2, 3, 4, 5]

# T11 noopt (with locks and full IPIs)
y_noopt = [821, 1509, 3407, 5065, 6816, 6816]
# T11 opt (lock elision on ABB10/12, IPI avoided on ABB16)
y_opt = [64, 125, 2030, 2684, 4435, 4435]

ax.step(x_indices, y_noopt, where='post', color='#1f77b4', linewidth=2.5, label='T11 noopt (Baseline)')
ax.step(x_indices, y_opt, where='post', color='#ff7f0e', linewidth=2.5, label='T11 opt (Lock & IPI Elided)')

ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5])
ax.set_xticklabels(abbs, fontsize=10)
ax.set_ylabel('Cycles above BCET', fontsize=12)
ax.set_xlabel('ABBs (System Call Sites)', fontsize=11)
ax.set_title('Fig. 15: Optimized execution time of example application Task T11', fontsize=12, pad=12)
ax.set_ylim(-100, 7500)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='upper left', frameon=True, fontsize=11)

# Annotate cycle step deltas for noopt
ax.text(0.5, 850, '821', color='#1f77b4', fontsize=9, ha='center')
ax.text(1.5, 1550, '+688', color='#1f77b4', fontsize=9, ha='center')
ax.text(2.5, 3450, '+1898', color='#1f77b4', fontsize=9, ha='center')
ax.text(3.5, 5100, '+1658', color='#1f77b4', fontsize=9, ha='center')
ax.text(4.5, 6850, '6816 cycles', color='#1f77b4', fontsize=9, ha='center', fontweight='bold')

# Annotate cycle step deltas for opt
ax.text(0.5, 100, '64', color='#ff7f0e', fontsize=9, ha='center')
ax.text(1.5, 200, '+61', color='#ff7f0e', fontsize=9, ha='center')
ax.text(2.5, 2100, '+1905', color='#ff7f0e', fontsize=9, ha='center')
ax.text(3.5, 2750, '+654 (IPI omitted)', color='#ff7f0e', fontsize=9, ha='center')
ax.text(4.5, 4500, '4435 cycles (-35%)', color='#ff7f0e', fontsize=9, ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig(f"{out_dir}/Figure15_T11_optimization_speedup.png", dpi=300, bbox_inches='tight')
plt.close()
print("FIGURE 15 GENERATED SUCCESSFULLY!")
