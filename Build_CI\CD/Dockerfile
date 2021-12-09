FROM jenkins/jenkins:lts
ARG HOST_UID=1001
ARG HOST_GID=998
USER root
RUN apt-get update
RUN apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN apt  install -y awscli
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker-ce.list
RUN apt-get update
RUN apt-get -y install docker-ce docker-ce-cli containerd.io
RUN usermod -u $HOST_UID jenkins
RUN groupmod -g $HOST_GID docker
RUN usermod -aG docker jenkins
USER jenkins
