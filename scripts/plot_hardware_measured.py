import matplotlib.pyplot as plt
import numpy as np
import os

out_dir = "/home/mourya/projects/Major_Project/evaluation_graphs"
os.makedirs(out_dir, exist_ok=True)

# -------------------------------------------------------------
# REAL HARDWARE DATA FROM RASPBERRY PI 4 (CORTEX-A72 PMU)
# Measured Live at 2026-11-12:
# val: [0, 306, 349, 498, 792, 1095, 1143, 1191, 1516]
# deltas: [306, 43, 149, 294, 303, 48, 48, 325]
# -------------------------------------------------------------

# (a) GetSpinlock phases (Pi 4 vs Paper):
# u->k: 306 (Paper: 329)
# lock: 192 (Paper: 100)
# k->u: 294 (Paper: 407)
# Total: 792 (Paper: 836)

# (b) ReleaseSpinlock phases (Pi 4 vs Paper):
# u->k: 303 (Paper: 245)
# unlock: 96 (Paper: 102)
# k->u: 325 (Paper: 331)
# Total: 724 (Paper: 678)

# Total Pair Saved: 1516 cycles (Paper: 1514 cycles) -> 99.9% MATCH!

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), sharey=True)

# -------------------- SUBPLOT A: GetSpinlock --------------------
x = [0, 1, 2, 3]

# Paper baseline
y_paper_get = [329, 429, 836, 836]
# Our Hardware Measurement
y_hw_get = [306, 498, 792, 792]

labels_get = [r'$\uparrow u \to k$', 'acquire lock', r'$\uparrow k \to u$']

ax1.step(x, y_paper_get, where='post', color='#7f7f7f', linestyle='--', linewidth=2, label='Paper Baseline (836 cyc)')
ax1.step(x, y_hw_get, where='post', color='#1f77b4', linewidth=2.8, label='Our Run on Pi 4 (792 cyc)')

ax1.set_xticks([0.5, 1.5, 2.5])
ax1.set_xticklabels(labels_get, fontsize=11)
ax1.set_ylabel('Cycles', fontsize=12)
ax1.set_title('(a) GetSpinlock', fontsize=13, fontweight='bold', pad=10)
ax1.set_xlabel('Spinlock intervals', fontsize=11)
ax1.set_ylim(0, 950)
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.legend(loc='upper left', frameon=True, fontsize=10)

# Annotations for Hardware Run
ax1.text(0.4, 320, '306', color='#1f77b4', fontsize=10, fontweight='bold', ha='center')
ax1.text(1.2, 510, '498\n(+192)', color='#1f77b4', fontsize=10, fontweight='bold', ha='center')
ax1.text(2.2, 805, '792 cycles\n(+294)', color='#1f77b4', fontsize=10, fontweight='bold', ha='center')

# -------------------- SUBPLOT B: ReleaseSpinlock --------------------
# Paper baseline
y_paper_rel = [245, 347, 678, 678]
# Our Hardware Measurement
y_hw_rel = [303, 399, 724, 724]

labels_rel = [r'$\downarrow u \to k$', 'release lock', r'$\downarrow k \to u$']

ax2.step(x, y_paper_rel, where='post', color='#7f7f7f', linestyle='--', linewidth=2, label='Paper Baseline (678 cyc)')
ax2.step(x, y_hw_rel, where='post', color='#2ca02c', linewidth=2.8, label='Our Run on Pi 4 (724 cyc)')

ax2.set_xticks([0.5, 1.5, 2.5])
ax2.set_xticklabels(labels_rel, fontsize=11)
ax2.set_title('(b) ReleaseSpinlock', fontsize=13, fontweight='bold', pad=10)
ax2.set_xlabel('Spinlock intervals', fontsize=11)
ax2.set_ylim(0, 950)
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.legend(loc='upper left', frameon=True, fontsize=10)

# Annotations for Hardware Run
ax2.text(0.4, 315, '303', color='#2ca02c', fontsize=10, fontweight='bold', ha='center')
ax2.text(1.2, 415, '399\n(+96)', color='#2ca02c', fontsize=10, fontweight='bold', ha='center')
ax2.text(2.2, 735, '724 cycles\n(+325)', color='#2ca02c', fontsize=10, fontweight='bold', ha='center')

fig.suptitle('Fig. 14: Hardware Validation on Raspberry Pi 4 — Spinlock Phases (Our Run vs Paper)', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()

out_img = f"{out_dir}/Figure14_hardware_spinlock_measured.png"
plt.savefig(out_img, dpi=300, bbox_inches='tight')
plt.close()

# Copy to artifacts
os.system(f"cp {out_img} /home/mourya/.gemini/antigravity/brain/83358ba8-8366-4f0e-9d63-1966596281b5/")
print("FIGURE 14 HARDWARE VALIDATION PLOT SAVED!")
