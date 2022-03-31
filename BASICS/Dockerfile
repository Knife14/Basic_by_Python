# 在ubuntu20.04的docker容器中部署python工程项目
# 进入 docker 容器以后，需要切换用户，在root用户底下，部分绘制渲染功能将无法正常使用
# 一般编写习惯，越不会变动的命令放到越前面，因为当dockerfile有所更新需要重新编译时，将会从改变的命令开始往后编译。

# 创建镜像命令
# docker build -t imagename:tag ./dockerfile_path
# -t 添加标签； ./dockerfile_path dockerfile存放路径

# 创建容器并进入容器
# docker run( / create) --runtime=nvidia -e DISPLAY=${DISPLAY} -v /tmp/.X11-unix:/tmp/.X11-unix -it --name=...  imagename:tag /bin/bash
# docker attach ContainerID
# --runtime=nvdidia 启动本地显卡；
# -v /tmp/.X11-unix:/tmp/.X11-unix 共享本地unix端口；
# -e DISPLAY=${DISPLAY} 修改可视化环境变量
# -it 以终端命令行方式交互
# --name=... 给容器命名

# docker ps 查看容器
# docker images 查看镜像

FROM nvidia/opengl:base-ubuntu20.04  # 可以根据自己的意愿选择基于何种公共镜像（docker pub）进行自定义

ENV DEBIAN_FRONTEND=noninteractive

ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES},display  # 绘制渲染功能需要配置显卡

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list  # 更换下载源

# 更新下载源列表与下载相应的软件库
# 下载默认yes需要添加 -y
# 利用 apt install 下载软件库是为了最恰当的版本适配
RUN apt-get clean \
    && apt-get update -y \
    && apt-get install -y \
        libmysqlclient-dev tzdata \
        libgl1-mesa-glx libglib2.0-dev libxcb-xinerama0 \
        python3 python3-dev python3-pip \
        python3-pyqt5 pyqt5chart-dev

ENV LANG C.UTF-8

# 更新 pip 版本
RUN python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

# 下载无法用 apt install 下载的python库
RUN pip3 install install -i https://pypi.tuna.tsinghua.edu.cn/simple \
    grpcio==1.41.0 \
    protobuf==3.19.4 \
    grpcio-tools==1.41.0
