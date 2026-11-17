"""Assemble Supplementary Figures 1-5 from the panels written by the notebooks (run after notebooks 01-05)."""
import os
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

FIG = os.path.dirname(os.path.abspath(__file__))
PAN = os.path.join(FIG, "panels")


def panel(name):
    return os.path.join(PAN, name)


def autocrop(img, pad=10, thr=0.97):
    """Remove near-white margins around an image array."""
    rgb = img[..., :3].astype(float)
    if rgb.max() > 1:
        rgb = rgb / 255.0
    mask = rgb.min(axis=2) < thr
    rows, cols = np.where(mask.any(axis=1))[0], np.where(mask.any(axis=0))[0]
    r0, r1 = max(rows[0] - pad, 0), min(rows[-1] + pad, img.shape[0])
    c0, c1 = max(cols[0] - pad, 0), min(cols[-1] + pad, img.shape[1])
    return img[r0:r1, c0:c1]


def save(fig, name):
    fig.savefig(os.path.join(FIG, name), dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("written", name)


# Supplementary Figure 1: A | B | C
fig, axes = plt.subplots(1, 3, figsize=(21, 5.5))
for ax, p, letter in zip(axes, ["SuppFig1A.png", "SuppFig1B.png", "SuppFig1C.png"], "ABC"):
    ax.imshow(mpimg.imread(panel(p)))
    ax.axis("off")
    ax.text(-0.01, 1.02, letter, transform=ax.transAxes, fontsize=22, fontweight="bold", va="bottom", ha="right")
save(fig, "Supplementary_Figure_1.png")

# Supplementary Figure 2: as produced by notebook 03
shutil.copy2(panel("SuppFig2.png"), os.path.join(FIG, "Supplementary_Figure_2.png"))
print("written Supplementary_Figure_2.png")

# Supplementary Figure 3: A (XGBoost), B (linear regression) summary plots; C-F dependence plots
top = mpimg.imread(panel("SuppFig3AB.png"))
bottom = mpimg.imread(panel("SuppFig3CF.png"))
h_top, h_bot = top.shape[0] / top.shape[1], bottom.shape[0] / bottom.shape[1]
fig = plt.figure(figsize=(12, 12 * (h_top + h_bot)))
ax1 = fig.add_axes([0, h_bot / (h_top + h_bot), 1, h_top / (h_top + h_bot)])
ax2 = fig.add_axes([0, 0, 1, h_bot / (h_top + h_bot)])
for ax, img in [(ax1, top), (ax2, bottom)]:
    ax.imshow(img)
    ax.axis("off")
for x, y, letter in [(0.0, 1.0, "A"), (0.5, 1.0, "B")]:
    ax1.text(x, y, letter, transform=ax1.transAxes, fontsize=22, fontweight="bold", va="top")
for x, y, letter in [(0.0, 1.0, "C"), (0.5, 1.0, "D"), (0.0, 0.5, "E"), (0.5, 0.5, "F")]:
    ax2.text(x, y, letter, transform=ax2.transAxes, fontsize=22, fontweight="bold", va="top")
save(fig, "Supplementary_Figure_3.png")

# Supplementary Figure 4: force plots A (low), B (medium), C (high)
imgs = [autocrop(mpimg.imread(panel(f"SuppFig4_{n}.png"))) for n in ["low", "medium", "high"]]
ratios = [im.shape[0] / im.shape[1] for im in imgs]
fig, axes = plt.subplots(3, 1, figsize=(18, 18 * sum(ratios) * 1.15), gridspec_kw={"height_ratios": ratios})
for ax, im, letter in zip(axes, imgs, "ABC"):
    ax.imshow(im)
    ax.axis("off")
    ax.text(0.0, 1.0, letter, transform=ax.transAxes, fontsize=24, fontweight="bold", va="top")
save(fig, "Supplementary_Figure_4.png")

# Supplementary Figure 5: as produced by notebook 05
shutil.copy2(panel("SuppFig5.png"), os.path.join(FIG, "Supplementary_Figure_5.png"))
print("written Supplementary_Figure_5.png")
