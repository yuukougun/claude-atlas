"""勝敗だけから、勝率の 95% 区間と、見分けに要る試合数の目安を出す。

前提：引き分けのない、独立な試合。引き分けは除くか、別に数える。
使い方：python win-rate-interval.py 勝ち数 試合数
        python win-rate-interval.py --need 0.55   （真の勝率を 0.55 と見たときの目安）
"""
import math
import sys

Z = 1.96  # 95% 区間（正規近似）


def interval(wins: int, games: int) -> tuple[float, float, float]:
    p = wins / games
    half = Z * math.sqrt(p * (1 - p) / games)
    return p, p - half, p + half


def games_needed(p: float) -> int:
    """区間の下限が 0.5 を上回るのに要る試合数（真の勝率が p のとき）。"""
    gap = p - 0.5
    return math.ceil(Z * Z * p * (1 - p) / (gap * gap))


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--need":
        p = float(sys.argv[2])
        print(f"真の勝率 {p:.3f} を見分ける目安：約 {games_needed(p)} 試合")
    elif len(sys.argv) == 3:
        wins, games = int(sys.argv[1]), int(sys.argv[2])
        p, lo, hi = interval(wins, games)
        verdict = "50% と区別できる" if lo > 0.5 else "50% と区別できない"
        print(f"勝率 {p:.3f}　95% 区間 [{lo:.3f}, {hi:.3f}]　{verdict}")
    else:
        sys.exit(__doc__)
