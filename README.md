**RSA暗号コマンド**

**概要**

RSA暗号の鍵生成、暗号化、復号を行う学習用のLinuxコマンドです。

標準入力から英文または暗号文を受け取り、処理結果を標準出力へ出力します。

※学習用の簡易的なRSA暗号であり、実際の機密情報の保護には使用できません。

**動作環境**

- Ubuntu Linux
- Python 3.12
- 外部ライブラリ不要

**インストール方法**

```console
$ git clone https://github.com/arazinn/rsa_cryptography.git
$ cd リポジトリ名
$ chmod +x rsa.py
```

**使用方法**

1. 鍵の生成

```console
$ ./rsa.py keygen
```

公開鍵 `public.key` と秘密鍵 `private.key` が生成されます。

2. 暗号化

```console
$ echo "Hello World" | ./rsa.py encrypt > cipher.json
```

入力した英文を暗号化し、JSON形式で `cipher.json` に保存します。

3. 復号

```console
$ ./rsa.py decrypt < cipher.json
Hello World
```

暗号文を復号し、元の英文を表示します。

**注意事項**

- ASCII文字のみ対応しています。
- 暗号化と復号には同じ鍵を使用してください。
- 鍵ファイルは実行したディレクトリに保存されます。
- 秘密鍵を第三者に公開しないでください。

**テスト**

Python標準ライブラリの `unittest` を使用しています。

```console
$ python3 -m unittest discover -v
```

素数判定、鍵生成、文字列変換、暗号化と復号をテストします。

GitHub Actionsでも自動テストを実行します。

**ライセンス**

MIT License

詳細は [LICENSE](LICENSE) を参照してください。