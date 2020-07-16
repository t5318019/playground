#!/usr/bin/env bash
git clone https://github.com/samba-team/samba.git
cd samba/
sudo apt-get -y install python-dev libgnutls-dev libacl1-dev libldap2-dev libpam0g-dev
./configure
make
