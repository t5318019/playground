#!/usr/bin/env bash
sudo apt-get -y install openjdk-8-jre tomcat8 exuberant-ctags
sudo mkdir -p /var/opengrok/etc
sudo chown -R tomcat8: /var/opengrok/
wget https://github.com/OpenGrok/OpenGrok/releases/download/1.0/opengrok-1.0.tar.gz
tar xzf opengrok-1.0.tar.gz
sudo opengrok-1.0/bin/OpenGrok deploy
