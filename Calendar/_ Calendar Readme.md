---
date created: 2025-04-26
date modified: 2025-06-17
tags:
  - workflow
publish: true
---

## 按照年份筛选

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
