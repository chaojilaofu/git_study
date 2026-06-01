# -*- coding: utf-8 -*-
"""江苏大学课程论文图表生成参考脚本
使用 matplotlib 生成论文所需的 JPG 图表，自动处理中文字体。
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# === Windows 中文字体配置（关键！）===
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# === 示例：趋势对比图 ===
def example_trend_chart():
    years = np.arange(2010, 2024)
    val_a = 10 + np.cumsum(np.random.randn(len(years)) * 0.5)
    val_b = 20 + np.cumsum(np.random.randn(len(years)) * 0.5)
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(years, val_a, "o-", color="#1f77b4", linewidth=1.5, label="系列A")
    ax.plot(years, val_b, "s--", color="#ff7f0e", linewidth=1.5, label="系列B")
    ax.set_xlabel("年份", fontsize=11)
    ax.set_ylabel("数值（单位）", fontsize=11)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("fig_example_trend.jpg", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Saved: fig_example_trend.jpg")

# === 示例：柱状图 ===
def example_bar_chart():
    labels = ["类别A", "类别B", "类别C", "类别D"]
    values = [35, 28, 22, 15]
    
    fig, ax = plt.subplots(figsize=(7, 4))
    colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2"]
    bars = ax.bar(labels, values, color=colors, edgecolor="white", linewidth=0.8)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f"{v}%", ha="center", va="bottom", fontsize=10)
    ax.set_ylabel("占比 (%)", fontsize=11)
    ax.set_ylim(0, max(values) * 1.2)
    fig.tight_layout()
    fig.savefig("fig_example_bar.jpg", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Saved: fig_example_bar.jpg")

if __name__ == "__main__":
    example_trend_chart()
    example_bar_chart()
    print("所有图表已生成。放入 figures/ 目录后在 LaTeX 中引用。")
