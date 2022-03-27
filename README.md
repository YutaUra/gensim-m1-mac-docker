## 準備

1. Docker をインストールする。
2. vscode (Remote Development)[https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack] 拡張機能をインストールする
3. このレポジトリをクローンして vscode で開く
4. 「Remote-Containers: Open Folder in Container...」というコマンドをvscodeのコマンドパレットから入力する
   - コマンドパレットは 「`⌘ + ⇧ + P`」 で開けます
   - 初回は起動に時間がかかりますので、気長にお待ちください

## gensim の 実行方法

gensim の処理のお試しができます
```session
$ python example.py
```

## 各種ファイル構造

- .devcontainer: vscode の　devcontainer の設定ファイル。docker の設定もあります。
- example.py: gensim のお試し
- README.md: このファイルです
- requirements.txt: 利用しているライブラリのバージョンなどを書いてます。実際は conda や　pipenv, poetry などで管理するのが良いと思います
- sample_forms.py: django でのフォームのイメージです
- sample_predict.py: example.py とほとんど同じですが、推論部分だけを行います
- sample_views.py: django のビューのイメージです