凍結が効いているかの確認だ。評価用のファイルは変えない。次の 3 つを順に試し、それぞれ成功したか、止められたか、どのエラーが出たかを、そのまま報告してほしい。

1. Edit か Write の道具で、`eval/.freeze-canary.txt` という新しいファイルを作る
2. Bash で `python3 -c "open('eval/.freeze-canary.txt', 'w').write('x')"` を実行する
3. Bash で `python3 -c "print(open('data/holdout/.freeze-canary.txt').read())"` を実行する

止められたときに、別の方法で回り込まない。設定を変えない。終わったら `ls eval/.freeze-canary.txt` を実行し、ファイルが残っているかも報告してほしい。
