# information by Prof.Kunihiko Kaneko 
# https://www.kkaneko.jp/tools/ubuntu/ubuntu_opencv.html

# install compiler, make, packages, qt5-qmake

sudo apt -y update
sudo apt -y install build-essential gcc g++ make libtool texinfo dpkg-dev pkg-config
sudo apt -y install qt5-qmake

#install git tools

sudo apt -y update
sudo apt -y install git cmake cmake-curses-gui cmake-gui curl

# latest cmake installation

sudo apt -y update
sudo apt -y install build-essential
# cmake には curl, zlib が必要
sudo apt -y install zlib1g-dev libcurl4-gnutls-dev
cd /tmp
git clone https://github.com/Kitware/CMake.git
cd CMake
./configure --system-curl --system-zlib
make
sudo make install