# UAutoIDE

国内一流的Unity3D手游自动化录制与回放工具

## 如何参与开发

* python 3.7, pip
* node, yarn

Pull submodule:

```
> git submodule update --init --recursive
```

Create python venv(optional):

```
> python -m venv venv
> venv\Scripts\activate.bat
```

Install python requirements:

```
> python -m pip install -U pip
> python -m pip install -U setuptools
> pip install -r requirements.txt
```

Install Node requirements :

```
> cd miniperf/ui
> yarn install
> yarn dev
```

Run:
```
> python -m miniperf.app
```

Package:(Windows only)

```
> python -m pip install wheel
> python -m pip install pynsist
> python build.py
```

output file: dist/UAutoIDE-x.x.x.zip

## 目录结构

* docs: 文档
* miniperf: 
    * ui: UI页面（HTML/JS/CSS)
        * libs/tpt-ui-lib: UI库
    * 自动化录制转表工具实现



## 分支说明

* master, 用于发布，对应正式版。
* dev, 用于开发，并且对应测试版。
* 其他分支, 用于实验性特性开发。


## 打包说明

windows打包exe流程：
```python
# python build.py --build_type release --flavor internal
```
打包成功后会打印 `Build Success.`, 输出的文件在dist目录下，例如：
* UAutoIDE-1.0.1-internal-release.zip
* latest.json (用于自动更新


Build Type(打包版本)：
* debug: 调试版本
* prerelease: 预发布版本(用于提测)
* release: 发布版本

Project Flavor(产品变种):
* internal: 内部版本(DSP账户系统，内网服务器，提供给内部测中用户使用)
* public: 外部版本(Testplus账户系统，外网服务器，提供给外部用户使用)


linux和mac os仅支持pip安装。

## 发布流程

1. 在dev分支开发下一个新版本。
2. 新版本开发完成后提交测试版，提测并修复BUG。
3. 测试通过后，合并dev分支到master分支，发布正式版。 

## 前端学习文档

https://react-bootstrap.github.io/components/buttons/