# progress-writer.py
# 要約の指標だけを 1 行の JSON にして progress.jsonl へ書き足す。
# 生のログ（ループの中の print や例外の全文）は、別のファイル（raw.log）へ出す。
import json
import time


class Progress:
    def __init__(self, path="progress.jsonl", total=None, every_sec=60):
        self.path = path
        self.total = total          # 全体の大きさ（ステップ数・件数など）。分からなければ None
        self.every_sec = every_sec  # 書く間隔。ステップごとではなく時間で間引く
        self.start = time.time()
        self.last = 0.0

    def _write(self, status, step, metrics):
        now = time.time()
        row = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "status": status,       # running / done / failed のどれか
            "step": step,
            "total": self.total,
            "elapsed_s": round(now - self.start),
            **metrics,              # 見たい指標（損失・エラーの件数・処理の速さなど）
        }
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        self.last = now

    def tick(self, step, **metrics):
        # 呼ぶのは毎ステップでよい。書くのは every_sec 秒に 1 回だけ
        if time.time() - self.last >= self.every_sec:
            self._write("running", step, metrics)

    def finish(self, status, step=None, **metrics):
        # 終わりと失敗は、間隔に関係なく必ず書く
        self._write(status, step, metrics)


if __name__ == "__main__":
    # 動作の確かめ用。間隔を 1 秒にして、5 秒ほどの擬似ジョブを回す
    p = Progress(total=50, every_sec=1)
    errors = 0
    try:
        for i in range(1, 51):
            time.sleep(0.1)
            if i % 17 == 0:
                errors += 1
            p.tick(i, errors=errors, score=round(1 / i, 4))
        p.finish("done", step=50, errors=errors)
    except Exception as e:
        p.finish("failed", error=type(e).__name__)
        raise
