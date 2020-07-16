#!/usr/bin/env bash
sudo apt-get -y install vim git curl
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get -y install nodejs

sudo sed -i 's/"quiet splash"/"quiet splash video=hyperv_fb:1920x1080"/g' /etc/default/grub
sudo update-grub
reboot
