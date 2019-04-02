# Workout Reportとは？

九州工業大学・古川研究室の新入生向けのトレーニングメニューとそのレポートのこと．
用意されているメニューの中からトレーニングを選択する．行ったらそれをレポート（報告）する．

# 目的：武器を手に入れる
自分が研究をしていくためのスキル，つまり武器を手に入れることが目的である．
メニューをこなすことで，機械学習のアルゴリズム開発を行う上での基本となる知識や実験のためのテクニックを身につけることができる．

# 方針：Just Do it !!
まずは[この動画](https://www.youtube.com/watch?v=ZXsQAXx_ao0&
)を見て欲しい．

やることは用意済み．ひたすら己を鍛えよう．

# メニューについて
詳細は`menu/README.md`を参照

# スケジュール
|    |                   | Work out report                         | その他                                       |
| -- | ----------------- | --------------------------------------- | ----------------------------------------- |
| 4月 | 第二週               | ガイダンス，Git&Githubワークショップ<br>トレーニング開始     | オリエンテーション<br>ワークショップ<br> |
| 5月 | 15                | ビギナー達成，コース選択<br>コース別の「常人」にトライ           | テーマ紹介                                   |
| 6月 | 14                | 「常人」達成<br>「玄人」に取り掛かる（スクラッチ実装を優先的に）          | flab教室ーガウス過程編                           |
| 7月 | 16<br>16~23<br>31 | 総まとめレポート1次提出<br>レビュー&修正<br>Qiitaに投稿 | テーマ決め                                   |
| 8月 |                   |                                         | flab教室ー研究室の基盤技術編                        |



# ワークアウトの進め方

[Githubのリポジトリ](https://github.com/furukawa-laboratory/workout_report_2019)を使ってワークアウトの進行を管理する．1つのトレーニングの始まりから終了までは以下の流れとなる．

1. メニューからトレーニング内容を確認し，実際に行う内容を[Issue](https://seleck.cc/647)に起こす
   -  To-doをIssueとして文章に書き起こすということが研究を行う際にも重要．その訓練だと思って取り組む．
   -  ちなみにIssueの本来の意味としてはIssue≠To-doなので注意
2. ブランチを切りトレーニングを行う
    - トレーニングで出てくるアウトプットをコミットする
       - なんらかのコミットできる形にして残すことが重要
          - プログラミングであれば`.py`や`.ipynb`ファイル
          - 数式の展開であればその写真など
          - 復習会であればそのホワイトボードの写真など
    - 適宜プッシュも忘れない
3. **ミニレポート** を提出する
   - ミニレポートとはトレーニング内容の報告書のこと
   - 紙媒体ではなく[Pull Request](https://seleck.cc/635)を用いる
      - トレーニングをコミットしたブランチのプルリクエストを出す
      - コメント欄にトレーニング内容の端的なまとめを書く
      - トレーニング前に出したIssueを引用すること
4. 上級生によるレビュー
   - 上級生がトレーニング内容についてコメントする
   - Q&Aもここでやると形に残るので良い
5. マージ
   - レビュワーがこれでOK!と判断するとmasterにマージされる
     - マージされるとProfileにおいてContributionとして可視化される（通称：草が生える）ので自分の頑張りを確認する良い指標となる

※Githubの扱いは慣れが必要．最初は手続きが複雑で繁雑に感じるかもしれないが，研究プロジェクトを管理するトレーニングになるので頑張ってほしい．


# まとめレポート：Qiitaでの解説記事
ワークアウトの内容を定着させるためにまとめレポートを作成する．トレーニング毎のミニレポートとは異なるので注意すること．以下が執筆の流れである．
1. 記事の第一稿はGithub上でmarkdown形式で提出する
   - フォーマットとしてはQiitaの解説記事
   - 記事数としては3本を目安にする
   - 第一稿提出は7月16日までに行うこと．これより早い分には問題ない．
2. GithubのReview機能を用いて上級生からのReviewと修正を繰り返す
3. 「完全」もしくは「完璧」になり次第，Qiitaに投稿する．

# トレーニングの際に参考となる文献
- ガウス過程と機械学習（線形回帰やガウス過程回帰の理論）
- 機械学習のエッセンス（基本的な線形代数・確率・プログラミング・スクラッチ実装）
- イラストで学ぶ機械学習（基本的な機械学習の手法がまとまった辞書的な本）
- 線形代数セミナー（線形代数・特異値分解）
- ベイズ推論による機械学習入門（ベイズ）
- Pythonで機械学習（実践的なPythonコードのexample）
- 特徴量エンジニアリング（前処理）

# アドバイス
- わからないときは先輩に聞くのがwork out reportを乗り切るコツ!!
- スキルを身に付ける時は筋トレするしかない！理解するにもまずは筋トレが先である！乗り切った後の自分の姿を想像しながらメニューを楽しもう！
