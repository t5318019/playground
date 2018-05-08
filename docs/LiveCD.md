# Live CD

## 介紹

Live CD 是包含「完整」作業系統的可開機光碟 (bootable CD) ，可用來測試或演示 (demo) 新的作業系統，而不需要將作業系統安裝到磁碟上。如果是可開機的 USB 磁碟，則稱為 Live USB。

* [LiveCD - Community Help Wiki](https://help.ubuntu.com/community/LiveCD)
* [LiveCDCustomization - Community Help Wiki](https://help.ubuntu.com/community/LiveCDCustomization)
* [LiveCD - Debian Wiki](https://wiki.debian.org/LiveCD)

## 從頭開始建立 Live CD

### 參考資料

* [LiveCDCustomizationFromScratch - Community Help Wiki](https://help.ubuntu.com/community/LiveCDCustomizationFromScratch)
* [LiveCD/Persistence - Community Help Wiki](https://help.ubuntu.com/community/LiveCD/Persistence)
* [LiveUsbPendrivePersistent - Ubuntu Wiki](https://wiki.ubuntu.com/LiveUsbPendrivePersistent)
* [CustomizeLiveInitrd - Ubuntu Wiki](https://wiki.ubuntu.com/CustomizeLiveInitrd)
* [GNU GRUB - GNU Project - Free Software Foundation (FSF)](https://www.gnu.org/software/grub/)
* [Syslinux Wiki](https://www.syslinux.org/wiki/)
* [The Linux Kernel Archives](https://www.kernel.org/)

### 相關手冊

* [Ubuntu Manpage: debootstrap - Bootstrap a basic Debian system](http://manpages.ubuntu.com/manpages/xenial/en/man8/debootstrap.8.html)
* [Ubuntu Manpage: syslinux - install the SYSLINUX bootloader on a FAT filesystem](http://manpages.ubuntu.com/manpages/xenial/en/man1/syslinux.1.html)
* [Ubuntu Manpage: mksquashfs - tool to create and append to squashfs filesystems](http://manpages.ubuntu.com/manpages/xenial/en/man1/mksquashfs.1.html)
* [Ubuntu Manpage: xorriso - creates,  loads, manipulates and writes ISO 9660 filesystem](http://manpages.ubuntu.com/manpages/xenial/en/man1/xorriso.1.html) (取代 mkisofs 指令)
* [Ubuntu Manpage: casper - a hook for initramfs-tools to boot live systems.](http://manpages.ubuntu.com/manpages/xenial/en/man7/casper.7.html)
* [Ubuntu Manpage: extlinux - install  the SYSLINUX bootloader on a ext2/ext3/ext4/btrfs](http://manpages.ubuntu.com/manpages/xenial/en/man1/extlinux.1.html)
* [Ubuntu Manpage: debirf - build an initrd to boot a full Debian system entirely from RAM](http://manpages.ubuntu.com/manpages/xenial/en/man1/debirf.1.html)
* [Ubuntu Manpage: cpio - copy files to and from archives](http://manpages.ubuntu.com/manpages/xenial/en/man1/cpio.1.html)

### 相關套件

* [Ubuntu – Details of package debootstrap in xenial](https://packages.ubuntu.com/xenial/debootstrap)
* [Ubuntu – Details of package syslinux in xenial](https://packages.ubuntu.com/xenial/syslinux)
* [Ubuntu – Details of package squashfs-tools in xenial](https://packages.ubuntu.com/xenial/squashfs-tools)
* [Ubuntu – Details of package xorriso in xenial](https://packages.ubuntu.com/xenial/xorriso)
* [Ubuntu – Details of package casper in xenial](https://packages.ubuntu.com/xenial/casper)
* [Ubuntu – Details of package lupin-casper in xenial](https://packages.ubuntu.com/xenial/lupin-casper)
* [Ubuntu – Details of package debirf in xenial](https://packages.ubuntu.com/xenial/debirf)
* [Ubuntu – Details of package grub2 in xenial](https://packages.ubuntu.com/xenial/grub2)
* [Ubuntu – Details of package grub2-common in xenial](https://packages.ubuntu.com/xenial/grub2-common)
* [Ubuntu – Details of package dbus in xenial](https://packages.ubuntu.com/xenial/dbus)
* [Ubuntu – Details of package ubuntu-standard in xenial](https://packages.ubuntu.com/xenial/ubuntu-standard)
* [Ubuntu – Details of package ubuntu-minimal in xenial](https://packages.ubuntu.com/xenial/ubuntu-minimal)
* [Ubuntu – Details of package discover in xenial](https://packages.ubuntu.com/xenial/discover)
* [Ubuntu – Details of package os-prober in xenial](https://packages.ubuntu.com/xenial/os-prober)
* [Ubuntu – Details of package linux-generic in xenial](https://packages.ubuntu.com/xenial/linux-generic)

### 相關知識

* [BootLoader - Debian Wiki](https://wiki.debian.org/BootLoader)
* [initramfs - Debian Wiki](https://wiki.debian.org/initramfs)
* [Initramfs - Ubuntu Wiki](https://wiki.ubuntu.com/Initramfs)
* [ramfs-rootfs-initramfs.txt](https://www.kernel.org/doc/Documentation/filesystems/ramfs-rootfs-initramfs.txt)
* [overlayfs.txt](https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt)
* [tmpfs.txt](https://www.kernel.org/doc/Documentation/filesystems/tmpfs.txt)
* [cpio - Debian Wiki](https://wiki.debian.org/cpio)
