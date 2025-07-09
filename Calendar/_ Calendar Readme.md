---
date created: 2025-04-26
date modified: 2025-06-17
tags:
  - workflow
publish: true
是否已review: true
---

## 主要作用

存放[[daily note]]，以及[[计划与回顾]]笔记。

实际的任务管理、日程管理，我依然习惯通过[[Spaces/3-Resource/软件梳理/安卓软件/滴答清单|滴答清单]]和[[谷歌日历]]。obsidian中，只使用`#todo`标签，做个简单备忘提醒，笔记写完的时候，将标签删除。


## base左上角，可以按照年份筛选

```base
filters:
  and:
    - file.folder.contains(this.file.folder)
views:
  - type: table
    name: "2025"
    filters:
      and:
        - file.name.startsWith("2025")
    columnSize:
      file.name: 128
  - type: table
    name: "2024"
    filters:
      and:
        - file.name.startsWith("2024")
    columnSize:
      file.name: 122
  - type: table
    name: "2023"
    filters:
      and:
        - file.name.startsWith("2023")
  - type: table
    name: "2022"
    filters:
      and:
        - file.name.startsWith("2022")
    order:
      - file.name

```
