# Init System

* [Chapter 3. The system initialization](https://www.debian.org/doc/manuals/debian-reference/ch03.en.html)
* [Debate/initsystem - Debian Wiki](https://wiki.debian.org/Debate/initsystem/)

## SysVinit

SysV 是 System V (唸作 System Five) 的縮寫，而 SysVinit 是當初用在 System V 的 Init System 。

* [Ubuntu Manpage: runlevel - event signalling change of system runlevel](http://manpages.ubuntu.com/manpages/xenial/en/man7/runlevel.7.html)
* [Ubuntu Manpage: runlevel - output previous and current runlevel](http://manpages.ubuntu.com/manpages/xenial/en/man8/runlevel.8.html)
* [浅析 Linux 初始化 init 系统，第 1 部分: sysvinit](https://www.ibm.com/developerworks/cn/linux/1407_liuming_init1/index.html)

## Upstart

Upstart 是 Ubuntu 為了取代 SysVinit 所開發出來的系統，採用事件為基礎的設計 (event-based)，利用事件驅動的方式可以平行執行多個程式，提高開機的速度與效能。

* [Upstart Intro, Cookbook and Best Practises](http://upstart.ubuntu.com/cookbook/)
* [Ubuntu Manpage: init - Upstart process management daemon](http://manpages.ubuntu.com/manpages/trusty/en/man8/init.8.html)
* [Ubuntu Manpage: initctl - init daemon control tool](http://manpages.ubuntu.com/manpages/xenial/en/man8/initctl.8.html)
* [Ubuntu Manpage: upstart-events - Well-known Upstart events summary](http://manpages.ubuntu.com/manpages/xenial/en/man7/upstart-events.7.html)
* [浅析 Linux 初始化 init 系统，第 2 部分: UpStart](https://www.ibm.com/developerworks/cn/linux/1407_liuming_init2/index.html)

## systemd

systemd 指的是 system daemon 的意思，全部小寫而且沒有空格。

* [systemd](https://www.freedesktop.org/wiki/Software/systemd/)
* [Ubuntu Manpage: systemctl - Control the systemd system and service manager](http://manpages.ubuntu.com/manpages/xenial/en/man1/systemctl.1.html)
* [Ubuntu Manpage: systemd, init - systemd system and service manager](http://manpages.ubuntu.com/manpages/xenial/en/man1/systemd.1.html)
* [浅析 Linux 初始化 init 系统，第 3 部分: Systemd](https://www.ibm.com/developerworks/cn/linux/1407_liuming_init3/index.html)
* [SystemdForUpstartUsers - Ubuntu Wiki](https://wiki.ubuntu.com/SystemdForUpstartUsers)
* [Rethinking PID 1](http://0pointer.de/blog/projects/systemd.html)
