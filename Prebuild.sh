sudo apt update
sudo apt install -y cmake g++ curl unzip
sudo mkdir -p /usr/local/opencv
sudo chown -R $USER /usr/local/opencv
cd /usr/local/opencv
curl -O https://github.com/opencv/opencv/archive/4.x.zip
cp 4.x.zip opencv.zip
curl -O https://github.com/opencv/opencv_contrib/archive/4.x.zip
cp 4.x.zip opencv_contrib.zip
rm -rf opencv-4.x opencv_contrib-4.x build
unzip opencv.zip
unzip opencv_contrib.zip
mkdir build 
cd build
rm -f CMakeCache.txt