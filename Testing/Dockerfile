FROM ubuntu:latest

RUN sudo apt-get update
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN sudo apt-get install -y openssh-server nano htop ssh screen openvpn

RUN /bin/bash -c "echo "alias ls='ls -lh --color'" > /etc/bash.bashrc"
RUN /bin/bash -c "source /etc/bash.bashrc"

WORKDIR /root/Git

VOLUME /root/Git /synced
