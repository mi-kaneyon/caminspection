# 作業手順
ASK corporation internal repository （社内限定リポジトリです）

# 0.イメージ作成準備
- Balna Etcher
- 64GB以上のMicroSDカード


# 1.Jetson Nano OSイメージ作成（Windows上）
1. Nvidia DeveloperサイトよりJetson Nanoイメージをダウンロードします。ここでは4.6.1をダウンロードします。
1. 次いでダウンロードしたzipファイルを任意のフォルダに回答します。imgの拡張子ファイルができているはずです。
1. MicroSDカードをPCでフォーマットできるように装着します。
1. Balna Etcherを起動します。
![balenaEtcher 2023_02_09 11_15_19](https://user-images.githubusercontent.com/53809036/217700137-accf5034-ba5a-4ec1-b1d4-3178ab79fd74.png)

- 画面左よりイメージファイルの選択ー＞書き込みメディアの選択ー＞Flash（書き込み実行「）します。
- ※コマンドプロンプトが表示されるので、「はい」で進めていきます。書き込みは15分程度かかります。

# 2.Jetson Nano 最終設定（Jetson上）
- メニュー通り進めるだけですが、言語は必ず”英語”にしてください。
- キーボードは日本語でも構いません。
- 検査の利便性からアカウントはすべて「nvidia」で統一します。
- 完了後、ターミナル画面を開き、以下コマンド実行してください。

```

sudo apt update
sudo apt upgrade -y

```
- パスワードはアカウントと同じ、upgradeは初回10分以上かかります。完了後、rebootコマンドかGUIのRESTARTで再起動します。

# 3.Opencv＋GStreamer書き換え（Jetson上）
- それぞれは単体でインストール済みですが、検査プログラム実行のため消去・再ビルドします。
