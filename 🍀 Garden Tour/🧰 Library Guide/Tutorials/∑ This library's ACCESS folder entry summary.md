---
date created: 2022-08-04
date modified: 2023-03-14
tags:
  - moc
  - todo/continuous-iteration
  - todo/now
  - todo/this-week
title: ∑ This library's ACCESS folder entry summary
publish: true
---
up:: [[ACCESS Note Organization Method]]
x:: [[∑ This library's ACCESS workflow summary]] , [[This library's ACCESS folder structure and hybrid note-taking method]]

>[!INFO] Usage principle
> You should be able to click on a link below to enter a file and directly create new related resource files under that file. This can ensure that no isolated files are created to the greatest extent, so that at least one link is generated between notes.

## Atlas

- [[∑ canvas creation entry]]
- [[∑ This library's Dataview summary]]
- [[∑ excalidraw whiteboard creation entry]]
- [[_ MOCs Readme]]
- [[§ TOCs]]

## Calendar

- [obsidian daily note](obsidian://advanced-uri?daily=true&mode=append)
- #todo/now #todo/this-week
- [Anki review notes](obsidian://advanced-uri?vault=knowledge-garden&commandid=obsidian-spaced-repetition%253Asrs-note-review-open-note)
- [[∑ Article drafts]]
- [[∑ Published articles]]

## Cards

- During the process of reviewing [[daily note]], you can drag the cards in batches, or use the cmd + shift + m shortcut key.
- [[» Emoji symbol record of this library's notes]]

## Extras

- Putting externally referenced pdf and other source files into the obsidian library can indeed achieve the effect of two-way links, but it will make the size of the library expand sharply, which is not conducive to packaging and sending to others. However, let's try to put them in first and consider adjusting them later. [[2022-10-01]] update, it is more convenient to put the pictures directly in the image bed.
- [[∑ Template file creation entry]]
- [billfish image and video management](billfish://)

## Sources

%%Fixed folder, non-growth, so no dataview%%

- [[∑ Article notes]]
- [[∑ Reading notes]]
- [[∑ Course notes]]
- [[∑ Movie notes]]
- [[∑ TV series notes]]
- [[∑ Subscription-based journal notes]]
- [[∑ Paper notes]]
- [[∑ Video notes]]

## Spaces

All MOC files in PARA under Spaces

%%Non-fixed folder, changes with the focused projects and fields, so you can use dataview for dynamic indexing%%

- Project
	- [[∑ Building a Second Brain Translation and Reading Notes]]
	- [[∑ Integration of human and technology]]
	- [[∑ chrome plugins]]
	- [[∑ obsidian plugins]]
	- [[∑ VSCode plugins]]
- Area
	- [[∑ Personal appearance management]]
	- [[∑ Personal career]]
	- [[∑ Fronted roadmap]]
	- [[∑ Cloud computing and cloud native]]
	- [[∑ Sports and health]]
	- [[∑ DevOps roadmap]]
	- [[∑ Knowledge management]]
- Resource
	- [[∑ Computer Science]]
	- [[§ Honor of Kings]]
	- [[∑ Small knowledge points]]
	- [[∑ golang]]

## Miscellaneous

```dataviewjs
// Get files with specified tags in the specified folder
const filter = '"Spaces" and #MOC'
// Group by folder, retrieve the tags, modification time and other related information of all files in the folder
const groups =  dv.pages(`${filter}`).groupBy(p => p.file.folder)
for (let group of groups) {
	dv.header(4, group.key);
	dv.table(["Name", "Creation Date", "Modification Date"],
		group.rows
			.sort(k => k.file.name, 'asc')
			.map(k => [k.file.link, k.file.cday, k.file.mday]))
}
```

- [[§ This library's obsidian usage manual]] 