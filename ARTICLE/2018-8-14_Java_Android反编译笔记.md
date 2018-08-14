一、准备必要工具

　　工欲善其事，必先利其器，首先我们要下载好反编译apk时需要的相关工具
1.1、使用工具

    apktool （资源文件获取） 
    dex2jar（源码文件获取）
    jd-gui  （源码查看）

1.2、工具介绍

　　apktool  

     　　　　作用：资源文件获取，可以提取出图片文件和布局文件进行使用查看

　　dex2jar

     　　　　作用：将apk反编译成java源码（classes.dex转化成jar文件）

　　jd-gui/jd-intellij
     　　　　作用：jd-gui查看APK中classes.dex转化成出的jar文件，即源码文件,jd-intellij查看class文件（需要先把jar解压）
1.3工具下载

    apktool下载地址：https://bitbucket.org/iBotPeaches/apktool/downloads
    dex2jar下载地址：http://sourceforge.net/projects/dex2jar/files/
    jd-gui/jd-intellij下载地址：http://jd.benow.ca/
    jd-inttellij也可以直接intellij内安装（setting->plugin->搜索java decompiler plugin）
二、使用方法
1. apktool
对某个apk
```
java -jar [apktool.jar路径] d -f [apk路径] -o [输出文件夹路径（没有则创建）]
```
2. dex2jar
对apk解压开的那个classes.dex文件
```
d2j-dex2jar.sh [classes.dex文件路径] -o [输出jar文件路径]
```
3. jd-gui/jd-intellij
* 直接启动这个jd-gui的jar包即可，在GUI界面内打开反编译的jar包
* jd-intellij下载安装在intellij后打开反编译得到的jar包的解压文件夹
