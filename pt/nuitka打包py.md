1 、下载安装 mingw64 配置环境变量

2、 **安装nuitka** pip install nuitka

3、打包命令   基于知乎和我自己的电脑摸索

3.1调试加上

--windows-disable-console #这一行去掉，执行时带cmd界面执行

nuitka --standalone --mingw64 --show-memory --show-progress --follow-imports --plugin-enable=qt-plugins --follow-import-to=need --output-dir=o index.py

参数简短说明

**--standalone** 默认包含参数--follow-imports 调用一些第三方库 为了完全独立运行

**--follow-imports** 对所有的引用到的库都进行打包

**--mingw64** 指定编译器

**--plugin-enable=qt-plugins**   qt库必须,指定更多第三方库

**--output-dir=DIRECTORY** 指定打包好的文件存放的目录，默认为当前目录

**--show-progress 和--show-scons** 用来显示详细打包过程，

根据修改命令

1.打包前先  activate my_py   （我的3.6环境）

2.执行命令

3.cmd 执行exe文件  将缺失的模块  可用everything软件 查找  拷贝过来（可拷文件夹） 直到不差

例如py8里面的，缺mani.ui 直接拷进去 缺图标 直接qrc和rc.py（图片转成二进制了）拷进去