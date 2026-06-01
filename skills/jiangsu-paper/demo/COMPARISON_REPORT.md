# Demo 对比报告：用 Skill vs 不用 Skill

## 测试任务
撰写 "太阳能光伏发电技术综述" 课程论文，格式遵循江苏大学（理工农医教类）规范。

## 结果对比

| 指标               | 不用 Skill                          | 用 Skill                           |
|--------------------|-------------------------------------|------------------------------------|
| 编译器             | pdflatex                            | pdflatex                           |
| 编译结果           | 有错误（字体冲突）                   | 零错误                             |
| PDF 大小           | 495 KB                              | 534 KB                             |
| 页数               | **7 页**（冗余严重）                 | **4 页**（紧凑规范）               |
| 页眉页脚           | ❌ 缺失                              | ✅ 左侧"江苏大学课程论文"+右侧标题  |
| 参考文献           | ❌ 无自定义格式                       | ✅ 居中标题+正确格式                |
| 封面               | ❌ 多大标题+日期+签字                  | ✅ 仅四行信息                       |
| 摘要               | ❌ 有英文摘要+摘要含引用               | ✅ 仅中文摘要+无引用                |
| 原创性声明          | ❌ 多余                               | ✅ 无                               |
| 职称               | ❌ 教授                               | ✅ 讲师                             |
| 结论引用           | ❌ 结论中有引用                        | ✅ 结论无引用                       |
| 作者               | 超级老付                             | 超级老付                           |

## 不用 Skill 的 9 个具体错误

1. **手动指定字体** → 与 pdflatex 冲突，产生 `Missing \begin{document}` 错误
2. **缺少页眉页脚** → 无 `fancyhdr`，论文看起来不正式
3. **封面多了大标题** → "江苏大学课程论文" 不在模板规范中
4. **职称写错** → 写"教授"应为"讲师"
5. **多了日期行** → 模板无日期要求
6. **多了原创性声明** → 课程论文无需声明页
7. **多了英文摘要** → 仅需中文摘要
8. **摘要和结论中有引用** → `\cite{}` 只能出现在正文
9. **参考文献无格式** → 缺自定义标题排版

## 用 Skill 的正确配置（关键代码）

### 页眉页脚
```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\zihao{6}\rmfamily 江苏大学课程论文}
\fancyhead[R]{\zihao{6}\rmfamily 论文标题}
\fancyfoot[C]{\zihao{6}\thepage}
\renewcommand{\headrulewidth}{0.4pt}
```

### 参考文献（避免重复标题）
```latex
\renewcommand{\refname}{}           % 隐藏默认标题
\begin{center}
    {\zihao{-2}\bfseries 参考文献}   % 手动居中标题
\end{center}
\begin{thebibliography}{99}
...
```

## 文件清单
```
demo/
├── COMPARISON_REPORT.md          ← 本报告
├── with_skill/                   ← 正确版本
│   ├── main.tex + main.pdf (4页)
│   └── figures/demo_chart.jpg
└── without_skill/                ← 错误版本（教学用）
    ├── main.tex + main.pdf (7页)
    └── figures/demo_chart.jpg
```
