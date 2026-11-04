---
id: pitfalls-of-ai-written-tests
title: AI に書かせたテストの落とし穴
aliases: [生成されたテストの質, テストの強さ, カバレッジの罠, ミューテーションテスト, テストを足す, テストを書かせる, テストの追加, カバレッジを上げる, 単体テスト]
type: concept
field: verify
chapter: テストで確かめる
order: 90
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: AI に書かせたテストが、今のバグ入りの挙動を正解として固めたり、壊しても落ちなかったりする落とし穴が分かる。テストそのものの強さを確かめる手を選べる。
signs:
  - {type: symptom, text: テストは全部通るのに、バグが残っている}
  - {type: symptom, text: カバレッジは高いのに、コードを壊しても落ちないテストばかりだ}
  - {type: goal, text: Claude に書かせたテストが役に立っているか確かめたい}
  - {type: goal, text: テストのない古いコードにテストを足したい}
prerequisites: [define-done]
related: [tests-first, protect-tests, differential-testing, property-based-tests, test-the-verifier, looks-are-not-quality, diffs-humans-must-read]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 今の挙動を正解として固める, anchor: pinning-bugs}
  - {title: 通るだけのテスト, anchor: weak-tests}
  - {title: テストの強さを確かめる, anchor: test-strength}
  - {title: テストのないコードに足させる, anchor: add-to-untested}
stage: stub
updated: 2026-11-04
---

## 今の挙動を正解として固める {#pinning-bugs}

## 通るだけのテスト {#weak-tests}

## テストの強さを確かめる {#test-strength}

## テストのないコードに足させる {#add-to-untested}
