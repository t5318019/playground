# Server Message Block (SMB)

## 介紹

SMB 是一種通訊協定 (protocol) ，全名是  Server Message Block ，最早是由 IBM 所開發，基於 client-server 的應用架構，透過網路可以分享檔案與印表機，目前最新版本是 SMB 3.1.1 。

SMB 在 OSI 網路模型上屬於 Application Layer 和 Presentation Layer 。

SMB 依靠底層的通訊協定主要是 NetBIOS over TCP/IP (簡稱 NBT )，而 NetBIOS 全名是 Network Basic Input/Output System，，NetBIOS 屬於 Session Layer 的通訊協定。

Common Internet File System (CIFS) 是 SMB 的另一個分支版本 (dialect) ，以範圍來看，CIFS 是 SMB 的子集合，SMB 延伸 CIFS 增加許多的支援。

* [What is SMB?](https://www.samba.org/cifs/docs/what-is-smb.html)
* [Microsoft SMB Protocol and CIFS Protocol Overview](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365233(v=vs.85).aspx)
* [[MS-CIFS]: Common Internet File System (CIFS) Protocol](https://msdn.microsoft.com/en-us/library/ee442092.aspx)
* [[MS-SMB]: Server Message Block (SMB) Protocol](https://msdn.microsoft.com/en-us/library/cc246231.aspx)
* [[MS-SMB2]: Server Message Block (SMB) Protocol Versions 2 and 3](https://msdn.microsoft.com/en-us/library/cc246482.aspx)

## Samba

Samba 是在 Linux/Unix 上實現 SMB/CIFS 通訊協定的自由軟體 (free software)。

* [Samba: An Introduction](https://www.samba.org/samba/docs/SambaIntro.html)
* [Using Samba](http://www.oreilly.com/openbook/samba/book/index.html)
* [SambaWiki](https://wiki.samba.org/index.php/Main_Page)
* [GitHub - samba-team/samba](https://github.com/samba-team/samba)

## mount.cifs

mount.cifs 命令可以將 CIFS 的分享路徑 mount 在本機上，在 Ubuntu 上屬於 cifs-utils 套件。

* [Ubuntu Manpage: mount.cifs - mount using the Common Internet File System (CIFS)](http://manpages.ubuntu.com/manpages/xenial/man8/mount.cifs.8.html)

## smbclient

smbclient 命令是用來存取 SMB/CIFS 資源的用戶端程式，在 Ubuntu 上屬於 smbclient 套件。

* [Ubuntu Manpage: smbclient - ftp-like client to access SMB/CIFS resources on servers](http://manpages.ubuntu.com/manpages/xenial/en/man1/smbclient.1.html)
