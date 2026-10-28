"""Draw the three-state ring and the four-state competitor at q=1/20 (Figure 1)."""
from fractions import Fraction as Fr
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
q = Fr(1, 20)
s = 1 + q
ring = [[-s, 1, q], [q, -s, 1], [1, q, -s]]
Qs = [[Fr(-21, 20), Fr(4781, 4800), Fr(31, 1200), Fr(9, 320)],
      [Fr(1, 20), Fr(-79, 60), Fr(19, 15), 0],
      [Fr(4, 5), Fr(1, 3), Fr(-131, 60), Fr(21, 20)],
      [Fr(21, 20), 0, Fr(1, 5), Fr(-5, 4)]]


def fmt(x):
    return f"{float(x):.3g}"


def draw(ax, Q, pos, names, title, cost):
    n = len(Q)
    for i in range(n):
        for j in range(i + 1, n):
            if Q[i][j] == 0 and Q[j][i] == 0:
                continue
            (x1, y1), (x2, y2) = pos[i], pos[j]
            for (a, b, c, rad) in ((i, j, Q[i][j], 0.18), (j, i, Q[j][i], 0.18)):
                (xa, ya), (xb, yb) = pos[a], pos[b]
                ax.annotate("", xy=(xb, yb), xytext=(xa, ya),
                            arrowprops=dict(arrowstyle="-|>", lw=0.6 + 2.2 * float(c) / 1.3,
                                            color="#33415c", shrinkA=17, shrinkB=17,
                                            connectionstyle=f"arc3,rad={rad}"))
                mx, my = (xa + xb) / 2, (ya + yb) / 2
                dx, dy = xb - xa, yb - ya
                ax.text(mx + 0.5 * rad * dy, my - 0.5 * rad * dx,
                        fmt(c), fontsize=7.5, ha="center", va="center", color="#33415c",
                        bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))
    for k, (x, y) in enumerate(pos):
        col = "#e07a5f" if names[k] == "A" else "#3d7ea6"
        ax.add_patch(plt.Circle((x, y), 0.13, color=col, zorder=3))
        ax.text(x, y, names[k], ha="center", va="center", color="white", fontsize=10,
                weight="bold", zorder=4)
    ax.set_title(f"{title}\nentropy production {cost}", fontsize=9.5)
    ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.2, 1.3); ax.set_aspect("equal"); ax.axis("off")


fig, axs = plt.subplots(1, 2, figsize=(8.2, 3.9))
draw(axs[0], ring, [(0, 1), (-0.95, -0.65), (0.95, -0.65)], ["A", "B1", "B2"],
     "(a) cheapest three-state mechanism (ring)", "2.8459")
draw(axs[1], Qs, [(0, 1.05), (-1.0, -0.05), (0, -0.95), (1.0, -0.05)], ["A", "B1", "B2", "B3"],
     "(b) four-state mechanism $Q_*$", "2.7731")
fig.text(0.5, 0.015, "Both produce exactly the same observed A/B signal at q = 1/20. "
         "Arrow labels are transition rates; arrow width grows with rate.", ha="center", fontsize=8)
fig.tight_layout(rect=(0, 0.04, 1, 1))
out = ROOT / "paper" / "figures"
fig.savefig(out / "networks.pdf"); fig.savefig(out / "networks.png", dpi=200)
print("wrote", out / "networks.pdf")
