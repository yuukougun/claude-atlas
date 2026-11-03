# 目次（試験用の抜き書き）

tests/tools/test_check_catalog.py の試験用。本物の planning/catalog/README.md のうち、tools/check_catalog.py が読むところ（§3 の visual の kind、§4.7 の templates の kind、§5 の機能の id の表）だけを、同じ書き方で置く。

## 3. <field>.yaml の形式

```yaml
    visual: {kind: static, text: "お願いと鍵の二層の図"}   # 図の案（任意。kind は static・mermaid・dynamic）
```

## 4. 規則

### 4.7 そのほかの項目

- `templates`：載せる予定の雛形。`kind` は settings・hook・skill・subagent・claude-md・prompt・other。安全とデータの雛形は `safety: true`（動作確認を通るまで載せない）

## 5. 機能の id（`tracks`）

`tracks` には、次の id を使う。ない機能は、ファイルの末尾の `new_features` に `{id, title, note}` で足す。

| 面 | id |
| --- | --- |
| Claude Code の文脈と指示 | `claude-md`・`rules`・`skills` |
| Claude Code の縛り | `hooks`・`permissions`・`sandbox` |
| Claude Code の任せ方 | `worktrees`・`agent-view` |

## 6. 検査

試験用の抜き書きなので、ここから先はない。
