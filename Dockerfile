# 建立 python3.11 环境
FROM python:3.9.16

# 镜像作者
MAINTAINER hmq

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 设置pip源为国内源
COPY pip.conf /root/.pip/pip.conf

# 在容器内创建django文件夹
RUN mkdir -p /usr/local/src/django

# 设置容器内工作目录
WORKDIR /usr/local/src/django

# 将当前目录文件加入到容器工作目录中（. 表示当前宿主机目录）
ADD . /usr/local/src/django

# pip安装依赖
RUN pip3 install --upgrade pip
RUN ["pip3", "install", "-r", "/usr/local/src/django/requirements.txt"]
