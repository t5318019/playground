#!/usr/bin/env bash
git clone git://git.csync.org/projects/csync.git
sed -i 's/__FUNCTION__/__func__/g' csync/src/csync_log.h
sudo apt-get -y install cmake libsqlite3-dev libsmbclient-dev libneon27-dev
cd csync/build/
cmake ..
make
