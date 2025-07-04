# 安装Scrapy爬虫框架

### 1，安装Tiwsted
- 前往[Tiwsted](https://pypi.org/project/Twisted/#files)下载whl文件；
- 下载完成后新建一个文件夹，将下载好的文件剪切到该文件夹中；
- 对着文件右键重命名，复制文件名（包括后缀名，如：twisted-25.5.0-py3-none-any.whl）；
- 右键文件夹空白处，选择`在终端中打开`；
- 输入`pip install `后右键粘贴，然后回车进行安装；
- 安装完成会有<span style="color:gold;">黄字</span>警告，没有问题。

### 2，安装Scrapy
- 终端安装：
```python 
pip install Scrapy 
```

### 3，安装pywin32
- 终端安装：
```python
pip install pywin32
```

### 4，创建一个Scrapy项目
- 任意路径打开终端
- 输入`scrapy startproject name`并运行，name为项目名称

### 5，项目结构
- spiders：项目的spider编写目录
- _init_：项目的初始化文件
- items.py：项目的定义文件
- middlewares.py：项目的中间件文件
- pipelines.py：项目的管道文件
- settings.py：项目的设置文件