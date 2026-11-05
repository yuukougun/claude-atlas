// 手元の設定を読み込まない形で Agent SDK を呼ぶ（別の利用者の依頼を処理する仕組みなどの出発点）
// 認証は環境に任せる。コードにも設定にも API キーを書かない
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "README.md を読んで、使い方を 3 行で要約して",
  options: {
    cwd: "/path/to/isolated-workdir",
    settingSources: [], // user・project・local の設定を読まない
    allowedTools: ["Read"], // 読み取りだけを確認なしで許す
    permissionMode: "default",
    env: {
      ...process.env,
      CLAUDE_CODE_DISABLE_AUTO_MEMORY: "1", // 自動の記憶は settingSources の外で読まれる
    },
  },
})) {
  if (message.type === "result") {
    console.log(message.subtype);
    if (message.subtype === "success") console.log(message.result);
  }
}
