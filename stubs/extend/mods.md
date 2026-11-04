---
id: mods
title: Mods（プラグインで挙動を深く変える）
nav_title: Mods
aliases: [Claude Mods, mod, hooks module, plugin-authoring]
type: feature
field: extend
chapter: プラグイン
order: 230
level: 仕組みにする
priority: 任意
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: []
pitfalls: []
scenes: [開発]
summary: プラグインの一種の mod で、Claude Code の画面や挙動そのものを変えられる。動くコードが深く入り込むので、ほかのプラグインより入れる前の確認を重くする。
signs:
  - {type: goal, text: Claude Code の画面や動きそのものに手を入れたい}
  - {type: goal, text: 会話の横に、作業の状態を常に出しておきたい}
prerequisites: [plugins-and-marketplaces]
related: [hooks-basics, vetting-extensions, usage-context-statusline, writing-safe-hooks]
tracks: [mods, plugins]
sources: []
volatility: 高
stage: stub
updated: 2026-11-04
---
