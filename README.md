## BunShop-flask

## 本项目为提交Python个人WEB项目的前端部分

## （前端部分Vue项目见[BunShop-vue](https://github.com/FannyFirst/BunShop-vue)）

### 本项目使用Python3与flask框架编写（项目预览见[BunShop-vue](https://fannyfirst.github.io/BunShop-vue/#/)）

更多详细信息在提交的作业ppt内

### 你可以使用下面的引导过程在本地创建并启动项目

## Project setup

### Git clone

```shell
git clone https://github.com/FannyFirst/BunShop-flask.git
```

### Install virtualenv(python 虚拟环境)

```shell
pip3 install virtualenv
cd BunShop
virtualenv venv
source venv/bin/activate
```

### Install flask 

```shell
pip3 install flask
```

### Install Gunicorn

```shell
pip3 install gunicorn
```

### start BunShop

```shell
gunicorn -b 0.0.0.0:5000 task:run
```

