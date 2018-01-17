# Server Message Block (SMB)

## 介紹

SMB 是一種通訊協定 (protocol) ，全名是  Server Message Block ，最早是由 IBM 所開發，基於 client-server 的應用架構，透過網路可以分享檔案與印表機，目前最新版本是 SMB 3.1.1 。

SMB 在 OSI 網路模型上屬於 Application Layer 和 Presentation Layer 。

SMB 依靠底層的通訊協定主要是 NetBIOS over TCP/IP (簡稱 NBT )，而 NetBIOS 全名是 Network Basic Input/Output System，，NetBIOS 屬於 Session Layer 的通訊協定。

Common Internet File System (CIFS) 是 SMB 的另一個分支版本 (dialect) ，以範圍來看，CIFS 是 SMB 的子集合，SMB 延伸 CIFS 增加許多的支援。

* [What is SMB?](https://www.samba.org/cifs/docs/what-is-smb.html)
* [Implementing CIFS](http://www.ubiqx.org/cifs/)
* [Microsoft SMB Protocol and CIFS Protocol Overview](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365233(v=vs.85).aspx)
* [[MS-CIFS]: Common Internet File System (CIFS) Protocol](https://msdn.microsoft.com/en-us/library/ee442092.aspx)
* [[MS-SMB]: Server Message Block (SMB) Protocol](https://msdn.microsoft.com/en-us/library/cc246231.aspx)
* [[MS-SMB2]: Server Message Block (SMB) Protocol Versions 2 and 3](https://msdn.microsoft.com/en-us/library/cc246482.aspx)

## Samba

[Samba](https://www.samba.org/) 是在 Linux/Unix 上實現 SMB/CIFS 通訊協定的自由軟體 (free software)，授權條款是 GPLv3 。

* [Samba: An Introduction](https://www.samba.org/samba/docs/SambaIntro.html)
* [Using Samba](http://www.oreilly.com/openbook/samba/book/index.html)
* [SambaWiki](https://wiki.samba.org/index.php/Main_Page)
* [samba](https://www.samba.org/samba/docs/current/man-html/samba.7.html)
* [Ubuntu Manpage: samba - A Windows AD and SMB/CIFS fileserver for UNIX](http://manpages.ubuntu.com/manpages/xenial/man7/samba.7.html)

Samba 軟體套件可以做的事情有：

* SMB 伺服器 (server)，提供檔案/印表機分享的功能
* Windows Domain Controller
* NetBIOS (rfc1001/1002) nameserver
* SMB 用戶端 (client)，存取其他檔案/印表機分享
* 一些指令工具 (command-line tool)
* 提供 Linux 的檔案系統，如 cifsvfs, smbfs

### Samba source code

* 官方 Git 儲存庫： [https://git.samba.org/samba.git](https://git.samba.org/samba.git)
* GitHub Mirror 儲存庫： [GitHub - samba-team/samba](https://github.com/samba-team/samba)

### Samba 開發相關資訊

* 開發概觀： [Samba Development](https://www.samba.org/samba/devel/)
* 開發者文件： [Developer Documentation - SambaWiki](https://wiki.samba.org/index.php/Developer_Documentation)
* 建置 Samba 是使用 [Waf](https://waf.io/) 這項工具，可參閱： [Waf - SambaWiki](https://wiki.samba.org/index.php/Waf), [Waf - Wikipedia](https://en.wikipedia.org/wiki/Waf)

## mount.cifs

mount.cifs 命令可以將 CIFS 的分享路徑 mount 在本機上，在 Ubuntu 上屬於 cifs-utils 套件。

* [Ubuntu Manpage: mount.cifs - mount using the Common Internet File System (CIFS)](http://manpages.ubuntu.com/manpages/xenial/man8/mount.cifs.8.html)

## smbclient

smbclient 命令是用來存取 SMB/CIFS 資源的用戶端程式，在 Ubuntu 上屬於 smbclient 套件。

* [Ubuntu Manpage: smbclient - ftp-like client to access SMB/CIFS resources on servers](http://manpages.ubuntu.com/manpages/xenial/en/man1/smbclient.1.html)

## 其他

* PowerShell 有關 SMB 操作的 Cmdlet： [SmbShare](https://docs.microsoft.com/en-us/powershell/module/smbshare/?view=win10-ps)
