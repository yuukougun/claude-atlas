# Agent SDK を呼ぶとき、読み込む設定・許す道具・権限モードを省略に頼らず書く
# 認証は環境に任せる。コードにも設定にも API キーを書かない
import asyncio

from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query


async def main() -> None:
    options = ClaudeAgentOptions(
        cwd="/path/to/workdir",  # 作業ディレクトリ。project の設定はここから探す
        setting_sources=["project"],  # 読み込む設定の置き場を明示する（user・local は読まない）
        allowed_tools=["Read", "Grep", "Glob"],  # 確認なしで使わせる道具。読み取りだけ
        permission_mode="default",  # 権限モードも明示する
    )
    async for message in query(prompt="src/ の構成を要約して", options=options):
        if isinstance(message, ResultMessage):
            # subtype が success 以外のときは、結果を信じる前に原因を見る
            print(message.subtype)
            print(message.result)


asyncio.run(main())
