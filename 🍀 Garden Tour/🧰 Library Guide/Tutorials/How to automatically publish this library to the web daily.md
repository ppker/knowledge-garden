---
date created: 2022-08-25
date modified: 2023-03-14
title: How to automatically publish this library to the web daily
publish: true
---
To publish the obsidian note library to the web like a blog, this library currently adopts 2 third-party free solutions. For details, see [[The most perfect free publishing solution for obsidian at present - a progressive tutorial]].

After executing the note library synchronization command of [[How to automatically sync this library to github daily]], then execute the command to pull the latest notes from the note library and automatically synchronize to the git repository. Note that the repositories of my 2 solutions here both use the [[git submodule]] method:

- [GitHub - oldwinter/dg: The most perfect free solution for digital gardens](https://github.com/oldwinter/dg)
- [GitHub - oldwinter/dg3: 🌱 host your own second brain and digital garden for free](https://github.com/oldwinter/dg3)

After the first git clone on your computer, you also need to execute `git submodule update --init --recursive` to initialize the submodule, so that the following commands can be executed smoothly.

The command is as follows:

```zsh
# dg jekyll solution
cd /Users/cdd/works/dg/_notes/
git checkout -q main
git pull 
cd /Users/cdd/works/dg
git add .
git commit -m "auto publish1 by keyboard"
git push

# dg3 quartz solution
cd /Users/cdd/works/dg3/content/
git checkout -q main
git pull
cd /Users/cdd/works/dg3
git add .
git commit -m "auto publish3 by keyboard"
git push
```

After pushing to github, the subsequent build and release process will be automatically triggered. Currently, my dg solution is hosted on , and my dg3 solution is hosted on [[Vercel]]. 