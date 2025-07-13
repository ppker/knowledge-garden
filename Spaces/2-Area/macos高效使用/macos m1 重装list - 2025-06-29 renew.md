---
相关笔记:
  - "[[MacOS 2023年7月软件安装列表-适配映兔工作流]]"
  - "[[macos m3 重装list]]"
date created: 2023-09-02
date modified: 2025-07-04
publish: true
---

> 要注意，有arm或通用版本，则尽量不要使用intel版本，卡顿且耗电。

## 个人必装

从[[App软件管理.base]]筛选7分和6分必装。5分选装。

- [[搜狗输入法]]
- [[Arc浏览器]]
	- 目前还不支持profile同步，所以需要重新手动弄一遍插件和账号登录等等。
	- [[arc浏览器插件重装list]]
- [[夸克网盘]]
- [[Obsidian]]
- [[Notion]]
- [[Spaces/3-Resource/软件梳理/macos软件/Bob]]
- [[滴答清单]]
- [[Cursor]]
- [[Raycast]]
- [[Clash Verge]]
- [[Warp]]
- [[Ice]]
- [[CleanShot X]]
- [[istat Menus]]
- [[BetterAndBetter]]
- [[BetterTouchTool]]
- [[Latest - MacOS软件]]
- [[微信]]
- [[Spaces/3-Resource/软件梳理/macos软件/微信读书]]
- [[AlDente]]
- [[CotEditor]]
- [[Spaces/3-Resource/软件梳理/macos软件/IINA]]
- [[Input source pro]]
- [[Keka]]
- [[OrbStack]]
- [[Spaces/3-Resource/软件梳理/macos软件/PearCleaner]]
- [[QuickRecorder]]

### 可以通过homebrew一键安装

8g内存备用机，有些软件就不装了。

```
brew install --cask orbstack
brew install --cask karabiner-elements
```

```
brew install --cask arc
brew install --cask bettertouchtool
brew install --cask cherry-studio
brew install --cask clash-verge-rev
brew install --cask coteditor
brew install --cask cursor
brew install --cask folo
brew install --cask input-source-pro
brew install --cask iina
brew install --cask pearcleaner
brew install --cask piclist
brew install --cask quickrecorder
brew install --cask raycast
brew install --cask warp
brew install --cask blip

brew install google-drive

brew install font-lxgw-wenkai
brew install jordanbaird-ice
brew install keka
brew install latest
brew install lihaoyun6/tap/quickrecorder
brew install notion
brew install obsidian
brew install qlstephen
brew install qlvideo
brew install quicklook-json
brew install quicklookase
brew install zen
```

```base
formulas:
  image: image(icon)
properties:
  note.brew 安装命令:
    displayName: brew安装命令
views:
  - type: table
    name: macos软件列表视图
    filters:
      and:
        - tags.containsAny("macOS软件")
        - "!brew安装命令.isEmpty()"
        - 评价 >= 5
    order:
      - file.name
      - 评价
      - brew安装命令
      - 是否有破解版
      - 是否已重装
      - 当前是否还在使用
      - 设置同步
      - 是否已备份
    sort:
      - property: 评价
        direction: DESC
      - property: brew安装命令
        direction: ASC
      - property: 是否有破解版
        direction: ASC
      - property: 当前是否还在使用
        direction: DESC
    columnSize:
      file.name: 121
      note.评价: 109
      note.当前是否还在使用: 105

```

## 破解版

> 从[[Macked]]下载。

1. iStat Menus
2. CleanShot X
3. Bob
4. AlDente
5. TickTick
6. LookAway
7. spotify

```base
formulas:
  image: image(icon)
properties:
  note.brew 安装命令:
    displayName: brew安装命令
views:
  - type: table
    name: macos软件列表视图
    filters:
      and:
        - tags.containsAny("macOS软件")
        - 是否有破解版 == true
    order:
      - file.name
      - 评价
      - brew安装命令
      - 是否有破解版
      - 是否已重装
      - 当前是否还在使用
      - 设置同步
      - 是否已备份
    sort:
      - property: 评价
        direction: DESC
      - property: brew安装命令
        direction: ASC
      - property: 当前是否还在使用
        direction: DESC
    columnSize:
      file.name: 121
      note.评价: 109
      note.当前是否还在使用: 105

```

## 软件配置设置同步


```base
formulas:
  image: image(icon)
properties:
  note.brew 安装命令:
    displayName: brew安装命令
views:
  - type: table
    name: macos软件列表视图
    filters:
      and:
        - tags.containsAny("macOS软件")
        - "!brew安装命令.isEmpty()"
        - 评价 >= 5
    order:
      - file.name
      - 评价
      - 设置同步
      - brew安装命令
      - 是否有破解版
      - 是否已重装
      - 当前是否还在使用
      - 是否已备份
    sort:
      - property: 评价
        direction: DESC
      - property: brew安装命令
        direction: ASC
      - property: 是否有破解版
        direction: ASC
      - property: 当前是否还在使用
        direction: DESC
    columnSize:
      file.name: 121
      note.评价: 109
      note.设置同步: 176
      note.当前是否还在使用: 105

```

### 账号自动云同步

- 搜狗输入法
	- 个人词库同步可能有bug，要多等一段时间。目前有30万条，如果没显示这么多，证明还没同步。

### 手动导出导入

- [[Raycast]]，等app装完了再导入。

### 其他云同步

 - chrome 各个插件的配置
 - 油猴脚本的配置

```base
filters:
  and:
    - tags.contains("chrome插件")
views:
  - type: table
    name: Table
    order:
      - file.name
      - 评价
      - 是否有firefox版本
      - 设置同步
    sort:
      - property: 评价
        direction: DESC
```
 

## 命令行工具

- [[Homebrew]]
	- [[kubectl]]
	- [[podman]]
	- [[pandoc]]
	- [[zoxide|zoxide]]
	- [[ffmpeg]]
	- [[kubectl]]
	- brew install fd rg fzf
		- [[fd命令]]
		- [[rg|rg命令]]
		- [[fzf]]
- 官方脚本安装
	- [[Spaces/3-Resource/软件梳理/linux常用命令/ohmyzsh|ohmyzsh]]
	- [[gemini-cli]]


## 开发环境

### 通用环境和命令行

- [[git 命令本机权限配置]]
- [[mise|mise]]
- [[dot文件配置同步仓库]]

### 开发类型app

#### 后端用app

- [[Navicat]]
	- [[DataGrip]]
- [[Proxyman]]
	- [[reqable]]
- [[Goland]]
- [[OrbStack]]


#### 安卓

- [[360 加固助手]]
- [[Android Studio]]

#### ios开发

- [[Developer]]
- [[xcode]]


#### 前端

- [[微信开发者工具]]
- [[webstorm]]

#### 运维




## MacOS系统配置

[[macos 使用体验优化配置]]
