# claude-atlas

Claude 全般を使いこなすための、辞書として引く日本語の教材。この辞典は Anthropic の公式の教材ではない。

- サイト：https://yuukougun.github.io/claude-atlas/
- 状態：土台を作っている段階で、ページはまだない。制作の進み具合は [planning/progress.md](planning/progress.md) にある

## リポジトリの中身

| 場所 | 中身 |
| --- | --- |
| `docs/` | サイトのページ（Markdown） |
| `overrides/` | サイトのテンプレート・JavaScript と、同梱の Mermaid |
| `data/` | 変わりやすい値・出典・古くなった助言の台帳 |
| `schema/` | 語彙（`site.yml`）と、形式の定義 |
| `tools/`・`tests/` | 生成と検査の道具と、その試験 |
| `planning/` | 要件・決定・設計・目次・制作の記録 |
| `.claude/` | Claude Code の設定（フックと権限。下の節） |
| `.github/workflows/` | CI（ビルド・検査・Zensical の試験ビルド・外部リンク）と、GitHub Pages への公開 |

## 手元でサイトを見る

[uv](https://docs.astral.sh/uv/) が要る（Python 3.12 は uv が用意する）。

```bash
uv sync --locked
uv run mkdocs serve          # http://127.0.0.1:8000/claude-atlas/
uv run mkdocs build --strict # CI と同じビルドの検査
```

## Claude Code でこのリポジトリを開くとき

`.claude/settings.json` に、制作の規則の一部を縛るフックと権限の設定（`hooks` と `permissions`）が入っている。Claude Code でこのリポジトリを開くと、読者の環境でも動く。入っているものとその働き、読者の環境で動くものと動かないもの、依存が欠けたときの動きは、[.claude/README.md](.claude/README.md) にある。

## ライセンス

© 2026 yuukougun

- 本文と図：CC BY 4.0（[LICENSE-docs](LICENSE-docs)）
- コードと雛形と、そのほかのファイル：MIT License（[LICENSE](LICENSE)）
- 同梱の Mermaid（`overrides/assets/vendor/mermaid-11.17.2/`）：MIT License（同じディレクトリの LICENSE）
