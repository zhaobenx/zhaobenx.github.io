---
layout: post
title: Windows下使用CLion和MinGW进行OpenCV开发
tag: ['技术', '编译', 'C++', 'OpenCV', 'CLion', 'MinGW', 'CMake']
comments: true
---

# 所需软件

*   Git
*   CMake
*   MinGW-w64
*   CLion

# 安装步骤

## 下载源码

使用Git从Github官方库[OpenCV](https://github.com/OpenCV/OpenCV)下载源码，注若需要使用SIFT和SURF等收费模块需另外从[OpenCV_contrib](https://github.com/OpenCV/OpenCV_contrib)。

## 配置CMake

打开CMake-gui，在第一栏输入OpenCV源码位置，第二栏选择编译后目录，可以选择如图所示OpenCV/build-debug或OpenCV/build

![CMake-screenshot-1](/img/CMake-screenshot-1.jpg)

点击`Configure`，Makefile格式选择`MinGW Makefile`编译器选择默认，之后需要等待一段时间。

等出现如图很多配置项后，即可跟剧需求做选择，如去除勾选test、doc、python、java等选项，按自己需求选择。

**注意，为使用SIFT等算法，需将`OPENCV_EXTRA_MODULES_PATH`设置为下载的opencv_contrib/modules，同时注意把反斜杠换成斜杠。**

同时可将`CMAKE_BUILD_TYPE`设为`RelWithDebInfo `，这样方便对源码进行Debug。

设置完毕后再次点击`Configure`成功后再点`Generate`即可。

## 编译

命令行打开所配置的build目录，输入`mingw32-make -j4 install`进行编译，跟剧硬件配置将花费不同的时间，在我笔记本上花了大概30分钟，选项的`-j4`跟剧电脑核心数选择，即八核可以选择`-j8`。

## 环境变量配置

打开环境变量配置，在path一项添加`E:\opencv\build-debug\install\x64\mingw\bin`，具体目录取决于编译目录。

之后重启电脑使环境变量生效。

## CLion设置

新建CLion项目，将`CMakeLists.txt`内容写作：

```cmake
cmake_minimum_required(VERSION 3.9)
# 你的项目名称
project(playopencv1)

set(CMAKE_CXX_STANDARD 11)

# OpenCV目录
set(OpenCV_DIR "E:\\opencv\\build-debug")
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")

FIND_PACKAGE(OpenCV REQUIRED)

# 可以不加
include_directories(E:/opencv/modules/features2d/src)

add_executable(playopencv1 main.cpp)



include_directories(${OpenCV_INCLUDE_DIRS})
# 添加需要的库名字
set(OpenCV_LIBS opencv_core opencv_imgproc opencv_highgui opencv_imgcodecs opencv_xfeatures2d)

# linking
target_link_libraries(playopencv1 ${OpenCV_LIBS})

```

之后编写`main.cpp`:

```cpp
#include <iostream>

#include "opencv2/opencv.hpp"
#include "opencv2/xfeatures2d.hpp"
#include "opencv2/features2d.hpp"
//
using namespace cv;
using namespace std;

int main()
{
    Mat img1 = imread("test.jpg");
    if (img1.empty())
    {
        cout << "error" << endl;
        return -1;
    }

    auto sift = xfeatures2d::SIFT::create();
    auto orb = ORB::create();
    auto img2 = img1.clone();

    vector<KeyPoint> keypoints_1, keypoints_2;

    sift->detect(img1, keypoints_1);
    orb->detect(img1, keypoints_2);

    drawKeypoints(img1, keypoints_1, img1);
    drawKeypoints(img2, keypoints_2, img2);
    cout<<"image size: "<<img1.size<<" "<<img2.size<<endl;
    hconcat(img1, img2, img1);
    cout<<"combined image size: "<<img1.size<<endl;

    namedWindow( "haha",CV_WINDOW_FREERATIO);
    imshow("haha", img1);
    waitKey(0);
    return 0;
}
```

将`test.jpg`置入`cmake-build-debug`目录，运行，弹出图像并显示特征点，测试成功。