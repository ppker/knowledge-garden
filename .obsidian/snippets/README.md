# Obsidian live-preview list threading and highlight

Obsidian forum thread: <https://forum.obsidian.md/t/plugin-for-bullet-threading/37317/22>

Add these CSS files in Appearance settings.

Changelog:

- 2024-08-15
  - separate versions for mouse hover and active line (keyboard focus)
    - can be enabled simultaneously without conflicts
  - works in live preview and source view
  - configurable with [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) plugin
  - threading snippets now have priority for wrapped text by default, can be toggled to priority for images
  - default styles adjusted to keep hover and active line threading distinguishable while using same color palette
  - threading line offsets are fixed to match latest Obsidian styles

- 2023-10-02
  - highlight snippet
    - halved the alpha, making highlight more subtle
    - made 6th color a bit more distinct from 5th
  - threading snippet
    - removed accidental dependency on another CSS snippet
    - adjusted offsets to better match indentation lines with the default font size
    - using `--list-indent` variable to hopefully make the snippet more compatible with styles that alter it
    - providing height calculations that prioritize wrapped text over images (or any other oversized inline content with default vertical alignment) - requires manual edits in 3 places to switch

----

Support me if you'd like me to publish Obsidian things more often:

<https://github.com/sponsors/KillyMXI>