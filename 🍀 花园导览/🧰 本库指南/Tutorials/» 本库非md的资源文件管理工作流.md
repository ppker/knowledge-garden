---
date created: 2022-08-07
date modified: 2023-03-14
title: » 本库非md的资源文件管理工作流

publish: true
tags: [AI生成, workflow, file-management]
aliases: [非md资源文件管理, 附件管理]
---
# 非 MD 资源文件管理工作流

本指南旨在为您提供一个清晰、高效的方法，来管理 Obsidian 仓库中的非 Markdown 格式的资源文件（如图片、PDF、视频、音频、脚本等）。

核心目标是利用 Obsidian 强大的链接和反向链接功能，确保每一个资源都能被有效追踪，了解其在知识库中的具体引用位置。

## 1. 核心原则

- **统一存放**: 将绝大部分非 MD 资源文件集中存储在 `Extras/Attachments/` 目录下。
- **分类管理**: 在 `Extras/Attachments/` 内部，根据文件类型创建子文件夹，如 `Images`, `PDFs`, `Videos`, `Audio`, `Scripts` 等。
- **链接优先**: 始终使用 Markdown 链接 `[[]]` 或嵌入 `![[]]` 的方式引用资源，而不是复制文件。
- **明确命名**: 为文件设定一个清晰、可读的名称，便于搜索和识别。

## 2. 存储位置策略

### a. 主要存储库：`Extras/Attachments/`

这是您仓库中所有通用资源文件的"中央车站"。

- **`Extras/Attachments/Images/`**: 存放通用图片。
- **`Extras/Attachments/PDFs/`**: 存放 PDF 文档。
- **`Extras/Attachments/Videos/`**: 存放视频文件。
- **`Extras/Attachments/Audio/`**: 存放音频文件。
- **`Extras/Attachments/Scripts/`**: 存放代码脚本。
- **`Extras/Attachments/Icons/`**: 存放图标文件，您已在实践。
- **`Extras/Attachments/Other/`**: 存放其他未分类的文件。

**自动化配置建议**：
在 Obsidian 的设置中，找到 `文件与链接` -> `附件默认存放路径`，将其设置为 `指定的附件文件夹`，并在下方的路径中填写 `Extras/Attachments`。这样，当您粘贴图片或拖入文件时，它们会自动保存到这个位置。

### b. 特定上下文存储

对于与特定项目或主题高度绑定的资源，可以存放在其对应的目录中。

- **`Atlas/Draws/`**: 用于存放 Excalidraw 或 Canvas 的绘图文件，这些是您核心知识地图的一部分。
- **`Spaces/1-Project/项目名称/assets/`**: 如果一个资源**仅**用于某个特定项目，可以随项目存放，方便项目整体迁移或归档。

## 3. 引用方法

为了让反向链接生效，请务必使用以下方法引用您的资源：

- **嵌入图片**: `![[my-image.png]]`
- **嵌入PDF的特定页面**: `![[my-document.pdf#page=3]]`
- **链接到文件**: `[[my-document.pdf]]`
- **链接并设置显示文本**: `[[my-document.pdf|查看我的文档]]`

通过这种方式，您可以在右侧的"反向链接"面板中，清晰地看到每个资源文件被哪些笔记所引用。

## 4. 为资源文件创建"元数据笔记" (可选但推荐)

对于一些重要的资源文件（如一个复杂的设计稿、一份重要的PDF报告），您可以为其创建一个同名的 `.md` 笔记，用来记录其元数据。

**示例**：
您有一个重要的图表文件 `2025-market-analysis.png`。

1.  在它旁边创建一个 `2025-market-analysis.md` 文件。
2.  在该 Markdown 文件中，您可以记录：
    - 文件的来源、作者。
    - 文件的简要描述。
    - 相关的思考和评论。
    - 使用 `tags` 和 `aliases` 增加可发现性。
    - 最后，嵌入该图片 `![[2025-market-analysis.png]]`。

```markdown
---
tags: [report, market-analysis, AI生成]
aliases: [2025年市场分析图]
source: "某个研究机构"
---
# 2025年市场分析图

这张图表展示了2025年AI市场的预期份额分布。

**核心观点**:
- A领域的增长最为显著。
- B领域趋于饱和。

![[2025-market-analysis.png]]

---
*关联笔记: [[AI行业观察]]*
```

这样做的好处是，您的资源文件本身也成为了一个可被深度搜索和关联的知识节点，而不仅仅是一个附件。

## 5. 总结

| 场景 | 推荐做法 |
| :--- | :--- |
| 通用图片、PDF、音视频 | 存入 `Extras/Attachments/` 下的分类文件夹，并通过 `![[]]` 或 `[[]]` 引用。 |
| 项目特定文件 | 存入项目文件夹内的 `assets` 子目录。 |
| 核心知识图谱、绘图 | 存入 `Atlas/Draws/`。 |
| 想为资源添加更多说明 | 创建同名的 `.md` 文件作为"元数据笔记"。 |

遵循这套工作流，您将能最大限度地发挥 Obsidian 的优势，让每一个知识片段（无论格式）都成为您知识网络中可追溯、可管理的一部分。
