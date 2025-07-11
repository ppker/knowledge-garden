---
date created: 2022-08-25
date modified: 2023-03-14
title: How to automatically sync this library to github daily
publish: true
---
[[How to specify which notes in this library are synced to github]]

Why not use the [[Obsidian Git]] plugin?
Because when it executes the git synchronization command, it will make obsidian very laggy. And I only need to use git to back up to github regularly. For other git version rollback functions, I use [[Spaces/3-Resource/Software-Sorting/macos-software/VSCode]] to open this library to execute, which is more comprehensive and easier to use. So I adopted the operating system-level automatic execution of git commands solution, rather than the obsidian built-in git execution solution.

How to configure the operating system-level automatic git command?
Just find an automated running tool, and set it to trigger the following command regularly:

```zsh
cd /Users/cdd/Works/knowledge-garden
git pull
git add .
git commit -m "auto by keyboard"
git push
```

Common tools on mac include: [[Keyboard Maestro]], [[hazel]], etc. I use the former. The configuration screenshot is as follows:
![](https://img2.oldwinter.top/202208250919001.png) 