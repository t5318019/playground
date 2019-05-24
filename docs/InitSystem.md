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

systemd 指的是 system daemon 的意思，systemd 的名稱全部都是小寫而且沒有空格。 Ubuntu 從 [15.04](https://wiki.ubuntu.com/VividVervet/ReleaseNotes) 開始用 systemd 取代原本的 Upstart。

systemd 是基於單元 ([unit](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)) 的概念所設計的，每個單元擁有一個名稱 (name) 和一種類型 (type)，systemd 共有下列幾種類型：

* [service](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
* [socket](https://www.freedesktop.org/software/systemd/man/systemd.socket.html)
* [device](https://www.freedesktop.org/software/systemd/man/systemd.device.html)
* [mount](https://www.freedesktop.org/software/systemd/man/systemd.mount.html)
* [automount](https://www.freedesktop.org/software/systemd/man/systemd.automount.html)
* [swap](https://www.freedesktop.org/software/systemd/man/systemd.swap.html)
* [target](https://www.freedesktop.org/software/systemd/man/systemd.target.html)
* [path](https://www.freedesktop.org/software/systemd/man/systemd.path.html)
* [timer](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)
* [slice](https://www.freedesktop.org/software/systemd/man/systemd.slice.html)
* [scope](https://www.freedesktop.org/software/systemd/man/systemd.scope.html)
* [systemd](https://www.freedesktop.org/wiki/Software/systemd/)

其他參考資料：

* [Ubuntu Manpage: systemd, init - systemd system and service manager](http://manpages.ubuntu.com/manpages/xenial/en/man1/systemd.1.html)
* [Ubuntu Manpage: systemctl - Control the systemd system and service manager](http://manpages.ubuntu.com/manpages/xenial/en/man1/systemctl.1.html)
* [Ubuntu Manpage: journalctl - Query the systemd journal](http://manpages.ubuntu.com/manpages/xenial/en/man1/journalctl.1.html)
* [浅析 Linux 初始化 init 系统，第 3 部分: Systemd](https://www.ibm.com/developerworks/cn/linux/1407_liuming_init3/index.html)
* [SystemdForUpstartUsers - Ubuntu Wiki](https://wiki.ubuntu.com/SystemdForUpstartUsers)
* [Ubuntu Wiki: systemd](https://wiki.ubuntu.com/systemd)
* [systemd - Debian Wiki](https://wiki.debian.org/systemd)
* [Rethinking PID 1](http://0pointer.de/blog/projects/systemd.html)
