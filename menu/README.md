進行管理はGithubを用いて行うこと

# 概要

カテゴリ・難易度別に以下のトピックについてトレーニングを行う．

|            |ビギナー      |常人         |玄人    |達人  |神   |  
| ---------- | ---------- | ---------- | ------ | --- | --- |
| 準備    | <span style="color: purple; ">Python, Git, Github</span>|／|／| ／ |／|
| 線形代数    | <span style="color: purple; ">ベクトル空間</span>| <span style="color: red; ">線形変換</span>| <span style="color: red; ">特異値分解と主成分分析</span>| ガウス過程       | 情報幾何    |
| ベイズ（確率） | <span style="color: purple; ">ベイズルール</span>| <span style="color: red; ">点推定</span>| <span style="color: red; ">分布推定</span>| ガウス過程       | モデル選択   |
| 前処理     | <span style="color: purple; ">正規化</span>| <span style="color: blue; ">データセット</span>| <span style="color: blue; ">生データ</span> | 特徴量エンジニアリング | 表現学習    |
| モデル     | <span style="color: purple; ">実装済みモデルの利用</span>| <span style="color: blue; ">kerasによる実装</span>| <span style="color: purple; ">スクラッチ実装</span>| 問題設定<br>（教師あり）       | 問題設定<br>（教師なし）   |
| 検証      | <span style="color: purple; ">描画</span>| <span style="color: blue; ">評価指標<br>（教師あり）</span>| 評価指標<br>（教師なし）| 実験デザイン<br>（教師あり）     | 実験デザイン<br>（教師なし） |

コースごとに選択する内容が異なる．

## コース
- **D進コース**
  - Doctorコースに進学したい人向け
  - カリキュラムは別途，提示します
- **理論コース**
  - 数学志向
- **応用コース**
  - 実装志向
- **卒業さえできればいいやコース**
  - カリキュラムは別途、提示します．

### コース別の取り組むメニューリスト
|            |ビギナー      |常人         |玄人    |達人  |神   |  
| ---------- | ---------- | ---------- | ------ | --- | --- |
| 理論コース| 全てやる|線形代数，ベイズ| 線形代数，ベイズ，モデル| エクストラ| エクストラ |
| 応用コース      | 全てやる | 前処理，モデル，検証|前処理，モデル| エクストラ| エクストラ

# メニュー詳細
## 準備（プログラミング基礎）
> **獲得スキルセット**  
> - Python, Git, Githubの環境構築ができる
> - Python, Git, Githubの基本的な操作ができる
### **Python**

- Python環境をセットアップせよ．
   - Anaconda等を用いたPythonパッケージの導入．バージョンは3系であれば特に指定しない．
   - Jupyter notebookも起動できるようにしておく
- [AidemyのPython入門コース](https://naichilab.blogspot.com/2014/01/gitsourcetreegit.html)
を受講せよ

### **Git**
- SourcetreeをPCにインストールせよ
   - Atlassianのアカウントを作成する必要がある
- ワークショップに参加せよ
   - [この記事](https://naichilab.blogspot.com/2014/01/gitsourcetreegit.html)の内容を皆で行うワークショップを4/16に開催する．

### **Github**
- Githubのアカウントを作成せよ
- ワークショップに参加せよ
   - 4/16に時間があれば行う．時間がなければ別の日程で行う．
   - [参考資料](https://qiita.com/takeokunnn/items/5bc499121a21f8c5b990
)

## **理論(線形代数・ベイズ)**
> **獲得スキルセット**
> - 線形代数
>    - ビギナー：ベクトル空間
>       - ベクトル空間が何かを説明できる
>       - ベクトル空間に標準内積を導入できる
>    - 常人：線形変換
>       - 写像が説明できる
>       - 射影が説明できる
>       - 線形変換の定義が説明できる
>    - 玄人：特異値分解と主成分分析
>       - 線形次元削減の定義を説明できる
>       - データ行列の分散共分散行列を対角化して主成分を求めることができる
>       - SVDを用いて主成分を求めることができる
>       - 求めた主成分を用いて次元削減ができる
> - ベイズルール
>    - ビギナー：ベイズルール
>       - 条件付き確率，周辺化，同時確率，独立の定義が書ける
>       - 条件付き確率の定義からベイズの定理を導出できる
>       - ベイズの定理の式の各部分の名前が言える
>    - 常人：点推定
>       - 問題設定を説明できる
>       - 最尤推定でデータからモデルのパラメータを推定できる
>       - MAP推定で（以下同）
>    - 玄人：分布推定
>       - 点推定との違いを説明できる
>       - ベイズ推定でデータからモデルのパラメータの確率分布を推定できる


これらは古川先生の講義を押さえれば獲得可能なスキルセットであるため，特定のトレーニングメニューは用意していない．その代わりに**火曜の1,2限**に古川先生の講義の**復習会**を行う．先輩たちとのフリーディスカッション形式で行うため，講義中に分からないところ・気になったところをピックアップしておくこと．





## 前処理
**ビギナー&常人：前処理入門**
> **獲得スキルセット**  
> - 与えられたnumpy arrayを平均0，分散1に標準化できる
> - sklearnやUCIなどの任意の公開データセットデータを「使える」
> - タスクに応じて適切なデータセットを調べられる
> - 標準的な形式のファイルを読み込める

1. この[データ解析の資料](https://data-flair.training/blogs/python-ml-data-preprocessing/)をローカルでjupyter notebookに写経した上で，PCAを用いてデータセットを可視化する処理を追加せよ．
2. [Sklearnのデータセット](https://scikit-learn.org/stable/datasets/index.html#toy-datasets)で同様の解析を行いなさい
   - iris
   - wine
   - boston
3. [UCIレポジトリ](http://archive.ics.uci.edu/)で同様の解析を行いなさい
   - Adult
   - Wine

**玄人：マルチメディアデータの前処理**
> **獲得スキルセット**
> - KaggleやEnronデータセットなどの生データからデータ整形・前処理を行い使用できる
> - 任意のデータセットを整形できる
> - 整形の工程管理ができる

1. Mongo DBの環境をつくりなさい
2. Enron DatasetをMongo DBで読み込みなさい
3. Mongoで以下の整形を行いなさい
   - 2001年の8,9,10月のデータを抽出する
4. pythonで以下の整形を行いなさい
   - ユーザー間のメールトラフィック数の抽出する
   - PCAで可視化する
## モデル

**ビギナー：sklearnを用いた実装済みモデルの利用**
> **獲得スキルセット**
> - irisデータセットに対してPCAをかける
> - Boston house-pricesに対して線形回帰を行い予測できる

1. sklearnの以下のサンプルコードを写経し自身の環境下で実行せよ
   - [単回帰](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html)
   - [PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

**常人：Kerasを用いたNNモデルの構築**
> **獲得スキルセット**
> - 任意のニューラルネットワークを構築できる
1. [チュートリアル](https://weblabo.oscasierra.net/python/keras-mnist-sample.html)を実行しmnist datasetをClassificationせよ
2. CNNを構築しmnist datasetに対するClassificationの精度を向上させよ
3. Autoencoderを構築しmnistデータを用いて学習させよ．また入力データと再構成した画像を比較せよ．
   任意の潜在変数からデコードした画像を表示せよ.

**玄人：スクラッチ実装**
> **獲得スキルセット**
> - 任意の数式をnumpy, tensorflowなどを用いて実装できる
1. [100 numpy exercises](https://github.com/rougier/numpy-100)を写経し実行せよ
2. 以下のチュートリアルを写経しながら実行せよ
    - [私訳「暫定的 NumPy チュートリアル」](https://naoyat.hatenablog.jp/entry/2011/12/29/021414)
    - [Computation on Arrays: Broadcasting](https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html)
    - [A Gentle Introduction to Broadcasting with NumPy Arrays](https://machinelearningmastery.com/broadcasting-with-numpy-arrays/)
3. 以下の手法を最低2つスクラッチ実装し，sklearnなどのライブラリと結果が一致するか確認せよ
    - 線形回帰
    - ロジスティック回帰
    - k-means
    - 主成分分析
## 検証

**ビギナー: matplotlibによる描画**
> **獲得スキルセット**
> - 結果を出力できる
>    - print
>    - plot
>    - scatter
>    - histgram
1. matplotlib tutorialの[pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)の内容を実行せよ.(必要に応じて[matplotlibのuser guide](https://matplotlib.org/tutorials/index.html)も参考に)
2. matplotlib tutorialのsample plots in matplotlibのサンプルプログラムを実行せよ
3. 自分の好きな関数を３つ選んで同じfigureでplotを用いて描画せよ
4. 自分の好きな関数を1つ選んで3次元のプロットを実行せよ.
5. animationを使って,自分の好きな関数を作成し,animationで動かせ（[参考](https://qiita.com/yubais/items/c95ba9ff1b23dd33fde2)）

**常人: 教師あり学習のモデル評価・選択**
> **獲得スキルセット**
> - 教師あり学習モデルの評価・選択が出来る
> - Cross Varidation: CVができる
> - 結果の平均分散を計算できる（バイアスバリアンス）
1. バイアスとバリアンスについて説明せよ.
2. cross Validationについて説明せよ.
3. sklearnのBoston house-pricesデータセットをloadして線形回帰を用いて学習させよ（[参考](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html)）
4. 学習させた結果をsklearnのcross validationで評価せよ（[参考](https://tech.mof-mof.co.jp/blog/scikit-learn-cross-validation.html)）
5. 学習結果の平均・分散を計算せよ（[参考](http://tekenuko.hatenablog.com/entry/2016/09/19/151547)）

**玄人: 教師なし学習の手法でモデルの評価・選択**
> **獲得スキルセット**
> - 教師なし学習のモデルの評価が出来る
>    - Acc, Precision, Recall, F1
>    - ARI
>    - 相互情報量(MI)

- 教師なし学習のクラスタリング手法を1つ選択し,学習結果を評価せよ
   - sklearnでiris データセットをloadせよ.
   - 教師なし学習のクラスタリング手法を1つ選択しデータを学習させる.
   - PCAでデータを2or3次元まで次元削減し可視化せよ．また各データに割り振られたクラスタおよびクラスタ境界も可視化すること
   - sklearnにある学習結果の評価指標(相互情報量など)を用いて学習結果を評価せよ.
- 教師なし学習の次元削減法を1つ選択し,人工データを用意して学習を行い,学習結果をMI(相互情報量)で評価せよ.
   - 人工データを用意せよ
   - 教師なしの次元削減法を1つ選択せよ
   - 学習結果を相互情報量を用いて評価せよ

※達人と神に関してはかなりAdvancedな内容なので，玄人までクリアした後で希望する学生にのみ公開する．


# スキルセットまとめ

改めてカテゴリと難易度ごとの身に着けるべきスキルを示す．トレーニング後に達成できているか確かめてみてほしい．

| |ビギナー|常人|玄人|達人|神|  
| ---------- | ---------- | ---------- | ------ | --- | --- |
| 準備    | プログラミング基礎<br><br>- Python, Git, Githubの基本的な操作ができる<br>- Python, Git, Githubの環境設定ができる                                          |／ |／|／|／|
| 線形代数    | ベクトル空間<br><br>- ベクトル空間が何かを説明できる<br>- ベクトル空間に標準内積を導入できる                                          | 線形変換<br><br>- 写像が説明できる<br>- 射影が説明できる<br>- 線形変換の定義が説明できる                                                   | 特異値分解と主成分分析<br><br>- 線形次元削減の定義を説明できる<br>- データ行列の分散共分散行列を対角化して主成分を求めることができる<br>- SVDを用いて主成分を求めることができる<br>- 求めた主成分を用いて次元削減ができる | ガウス過程       | 情報幾何    |
| ベイズ（確率） | ベイズルール<br><br>- 条件付き確率，周辺化，同時確率，独立の定義が書ける<br>- 条件付き確率の定義からベイズの定理を導出できる<br>- ベイズの定理の式の各部分の名前が言える | 点推定<br><br>- 問題設定を説明できる<br>- 最尤推定でデータからモデルのパラメータを推定できる<br>- MAP推定で（以下同）                                   | 分布推定<br><br>- 点推定との違いを説明できる<br>- ベイズ推定でデータからモデルのパラメータの確率分布を推定できる                                                             | ガウス過程       | モデル選択   |
| 前処理     | 正規化<br><br>- 与えられたnumpy arrayを平均0，分散1に標準化できる                                                    | データセット<br><br>- sklearnやUCIなどの任意の公開データセットデータを「使える」<br>   - タスクに応じて適切なデータセットを調べられる<br>   - 標準的な形式のファイルを読み込める | 生データ<br><br>- KaggleやEnronデータセットなどの生データからデータ整形・前処理を行い使用できる<br>- 任意のデータセットを整形できる<br>- 整形の工程管理ができる              | 特徴量エンジニアリング | 表現学習    |
| モデル     | 実装済みモデルの利用<br><br>- irisデータセットに対してPCAをかける<br>- Boston house-pricesに対して線形回帰を行い予測できる              | kerasを用いたモデルの実装<br><br>- 任意のニューラルネットワークを構築できる                                                             | スクラッチ実装<br><br>- 任意の数式をnumpy, tensorflowなどを用いて実装できる                                                                          | 問題設定<br>（教師あり）       | 問題設定<br>（教師なし）   |
| 検証      | 描画<br><br>- 結果を出力できる（画像、テキスト）<br>   - print<br>   - plot<br>   - scatter<br>   - histgram           | 評価指標<br>（教師あり）<br><br>- 教師あり学習モデルの評価・選択が出来る<br>   - CVができる<br>   - 結果の平均分散を計算できる（バイアスバリアンス）                          | 評価指標<br>（教師なし）<br><br>- 教師なし学習のモデルの評価が出来る<br>   - Acc, Precision, Recall, F1<br>   - ARI<br>   - 相互情報量(MI)                               | 実験デザイン<br>（教師あり）     | 実験デザイン<br>（教師なし） |
