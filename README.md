# Docker を使った Python の実行方法(社内向け)

Windows にインストールされた Docker Toolbox を使って Python を実行する方法を説明する。
なお、sample.how-to-use-python-with-docker フォルダを C:\Users\gnkm\Documents の下に置いたものとして説明する。
まず下記コマンドを実行しておく。

```
cd Documents/gnkm/sample.how-to-use-python-with-docker
```

## 基本的な使い方

下記コマンドで `print.py` を実行できる。

```
docker run -v $PWD:/tmp/working -w=/tmp/working --rm -it --name python python:3.8.5-alpine3.12 python print.py
```

`--name` の後の `python` は任意のものでよい。もしくはなくてもよい。
その場合 Docker がランダムで名前を割り当てる。

`python:3.8.5-alpine3.12` の部分は使用するイメージ名を指定する。

## `docker run` コマンドを簡単に実行するシェルスクリプト

下記コマンドで `print.py` を実行できる。

```
./docker-run-01.sh py print.py
```

を実行すると `print.py` を実行できる。
なお、python:3.8.5-alpine3.12 イメージをダウンロードしていないと
実行前にこのイメージのダウンロードが始まる。

## イメージの拡張方法(パッケージの追加方法)

ファイル `Dockerfile`, コマンド `docker build` を使う。

```
cd docker
```

を実行した後

```
docker build --no-cache -t gnkm/python-lp:v1 .
```

を実行すると、新たなイメージ gnkm/python-lp が作られる。

`docker-run-02.sh` を使って

```
./docker-run-02.sh py app.py
```

を実行すると、 `app.py` を実行できる。

追加でライブラリが必要になったら都度 Dockerfile を編集して `docker build` コマンドを実行すればよい。

## コンテナにインストールされている Python パッケージの確認方法

`docker-run-02.sh` を使って

```
./docker-run-02.sh pip list
```

を実行すると、ターミナルに表示される。
ただ、インストールされているパッケージが多いときは

```
./docker-run-02.sh pip list > packages.txt
```

として、`packages.txt` を確認する方がやりやすい。
