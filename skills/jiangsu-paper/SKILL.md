---
name: jiangsu-paper
description: |
  撰写江苏大学课程论文（理工农医教类）时使用此 skill。
  涵盖 LaTeX 模板、中文字体配置、pdflatex 编译注意事项、
  引用规范、Python 图表生成、以及常见陷阱的排查。
  关键词：江苏大学、课程论文、LaTeX、中文论文、氢能、工业脱碳、
  碳中和、ctexart、pdflatex、matplotlib 中文。
metadata:
  short-description: 江苏大学课程论文 LaTeX 模板与写作规范
---

# 江苏大学课程论文写作 Skill

## 核心规则（不可违反）

### 1. 编译引擎
- **必须**使用 `pdflatex`，**禁止**使用 `xelatex`
  - xelatex 在 Windows 上存在图片嵌入 bug，部分 JPG 无法显示
  - 文档第一行写 `% !TEX program = pdflatex`
- **必须**在纯 ASCII 路径下编译（无中文目录名）
  - pdflatex 对中文路径支持极差，会报 `Emergency stop`
  - 先在英文路径编译，再复制 PDF 到目标位置
- **必须**编译 3 次：第 1 次生成辅助文件，第 2-3 次解决目录和交叉引用

### 2. 文档结构与格式
- 文档类：`\documentclass[12pt,a4paper]{ctexart}`
- 页边距：`[top=2.5cm, bottom=2.5cm, left=3.0cm, right=2.5cm]`
- 行距：`\onehalfspacing`（1.5 倍），段首缩进 `\parindent=2em`
- 字体：ctex 默认 Windows 字体（宋体 SimSun、黑体 SimHei、楷体 KaiTi）
  - 英文用 `\usepackage{times}` 获得 Times New Roman
  - 节标题 `\heiti`（黑体），小节标题 `\songti\bfseries`（宋体加粗）

### 3. 封面格式（必须严格遵守）
封面不使用 `\titlepage`，直接用 `\begin{center}...\end{center}`，内容仅四行：

```
专业班级：××××          学生姓名：×××
指导教师：×××            职    称：讲师
```

- **禁止**添加"江苏大学课程论文"大字标题
- **禁止**添加日期、签字行
- **禁止**添加原创性声明
- **禁止**添加英文摘要
- 摘要紧接封面之后，不分页

### 4. 引用规范
- `\cite{}` **只能**出现在正文（第 1 节到最后一节），**不得**出现在摘要、结论
- 引用按顺序出现：[1], [2], [3]...每篇文献最好只引用一次
- 使用 `\begin{thebibliography}{99}` + `\bibitem{key}` 手动管理
- bibitem 顺序必须与正文中首次出现顺序一致

### 5. 图表生成
- 用 Python + matplotlib 生成，保存为 JPG（不要 PNG）
- 中文字体设置（Windows）：
  ```python
  import matplotlib.pyplot as plt
  plt.rcParams["font.sans-serif"] = ["SimHei"]
  plt.rcParams["axes.unicode_minus"] = False
  ```
- 图表放入 `figures/` 子目录，用 `\includegraphics` + `\captionof{figure}` 引用
- 使用 `\label{fig:xxx}` 和 `\ref{fig:xxx}` 交叉引用

## 常见陷阱排查

| 症状 | 原因 | 解决 |
|------|------|------|
| 图片不显示（空白框） | 用了 xelatex | 改用 pdflatex |
| Emergency stop，提示输入文件名 | 中文路径 | 移到英文路径编译 |
| 目录页码全为 ?? | 只编译了 1 次 | 编译 3 次 |
| 参考文献显示 [?] | bibitem 未定义或编译不足 | 确认 bibitem 存在 + 编译 3 次 |
| 中文在图表中显示为方块 | matplotlib 未设中文字体 | 设 `font.sans-serif = ["SimHei"]` |
| 参考文献重复出现 | 复制粘贴导致 thebibliography 块重复 | 只保留一个 `\begin{thebibliography}...\end{thebibliography}` |

## 论文结构模板

```
封面（四行信息）
中文摘要 + 关键词
目录 (\tableofcontents)
正文：
  \section{绪论}
  \section{相关背景/现状}
  \section{核心技术分析}
  \section{...}
  \section{国际经验}
  \section{结论}
  \subsection{主要结论}
  \subsection{研究展望}
\begin{thebibliography}{99}
  \bibitem{key1} 作者. 标题[J]. 期刊, 年份.
  ...
\end{thebibliography}
```

## 工作流程

1. 在英文路径创建项目目录，含 `figures/` 子目录
2. 用此 skill 的模板 `templates/main.tex` 作为起点
3. Python 脚本生成图表 → `figures/*.jpg`
4. `pdflatex main.tex` × 3
5. 复制 `main.pdf` 到最终位置


## 页眉页脚配置（必须）

```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\zihao{6}\rmfamily 江苏大学课程论文}
\fancyhead[R]{\zihao{6}\rmfamily 论文标题}
\fancyfoot[C]{\zihao{6}\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\setlength{\headheight}{14.5pt}
\addtolength{\topmargin}{-2.5pt}
```
封面用 `\thispagestyle{empty}` 隐藏页眉页脚。

## 参考文献格式（避免标题重复）

```latex
\renewcommand{\refname}{}           % 必须！隐藏 thebibliography 默认标题
\begin{center}
    {\zihao{-2}\bfseries 参考文献}
\end{center}
\vspace{12bp}
\begin{thebibliography}{99}
    \bibitem{key} ...
\end{thebibliography}
```
**禁止** 使用 `\section*{参考文献}`，否则标题出现两次。
