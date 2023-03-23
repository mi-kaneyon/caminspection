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

# 3.Opencv＋GStreamer書き換え準備（Jetson上）
- それぞれは単体でインストール済みですが、検査プログラム実行のため消去・再ビルドします。
@octocat :+1:　リポジトリ内のPrebuild.sh　をターミナル画面で実行するか、ファイルを開いてコピペします。

# 4.Opencv＋GStreamer書き換え（Jetson上）
1. リポジトリ内のpre-setup.sh　をターミナル画面で実行するか、ファイルを開いてコピペします。
2. opencv_makelist.txtを開き、cmakeの準備をします。特に以下の個所は個別でコピペしてください。

```
cmake   -D CMAKE_INSTALL_PREFIX=/usr/local \
-D BUILD_opencv_world=ON \
-D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules \
-D INSTALL_TESTS=ON \
-D INSTALL_C_EXAMPLES=ON \
-D WITH_PYTHON=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_opencv_python2=OFF \
-D BUILD_opencv_python3=ON \
-D PYTHON_DEFAULT_EXECUTABLE=python3 \
-D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
-D WITH_OPENCL=OFF \
-D WITH_CUDA=ON \
-D CUDA_ARCH_BIN=5.3 \
-D CUDA_ARCH_PTX="" \
-D WITH_CUDNN=ON \
-D WITH_CUBLAS=ON \
-D ENABLE_FAST_MATH=ON \
-D CUDA_FAST_MATH=ON \
-D OPENCV_DNN_CUDA=ON \
-D ENABLE_NEON=ON \
-D WITH_QT=ON \
-D WITH_OPENMP=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=OFF \
-D WITH_GSTREAMER=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=ON \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D BUILD_EXAMPLES=OFF .. \
  ../opencv-4.x

```
3.　続きのコマンド部分（♯のコメント除く）もトラブル防止のため、処理完了後にコピペしてください。

```

# finished compile copy and paste below one by one

cmake --build .
#
sudo make install
#
sudo /sbin/ldconfig

```

4. 最後のコマンドが終了した後に　以下コマンドを実行し、再起動します。

```
sudo apt update
sudo apt upgrade -y

```

# 5.オートフォーカス検査ツール実行環境の作成｛Jetson上)
1. リポジトリ内のstart.shをhome内にコピーします。
- 下記のURLもしくは「ubuntu スタートアップ ツール」で検索した通り、スタートアップツールでstart.shを起動時に実行するように登録します。
https://dailylife.pman-bros.com/start_up/

```
#ターミナル画面を開き、念のため下記実行
cd ~/
sudo chmod +x start.sh

```
2. お客様提供の検査ツール(cam_autofocus-main)を/home/kensa/ディレクトリを作り、解凍・コピーします。
3. ファイル内にあるREASMEファイルの指示通りに設定を変更します。
4. startupファイルを任意のエディタで開いて、全記載を書き換えてください。

```

~/.config/autostart/

[Desktop Entry]
Version=1.0
Name=Test        
Comment=Test the terminal running a command inside it
Exec=gnome-terminal -e "bash -c '/home/nvidia/start.sh;$SHELL'"
Icon=utilities-terminal
Terminal=false
Type=Application
Categories=Application;
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=start
Comment[en_US]=ddd


```

5. 保存後再帰動し、プログラム開始（シリアル番号入力表示）になることを確認します。
