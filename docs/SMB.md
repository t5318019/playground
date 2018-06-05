# Server Message Block (SMB)

## 介紹

SMB 是一種通訊協定 (protocol) ，全名是  Server Message Block ，最早是由 IBM 所開發，基於 client-server 的應用架構，透過網路可以檔案分享 (file share) 與印表機分享 (print share) ，目前最新版本是 SMB 3.1.1 (簡稱 SMB3 )。

SMB 在 OSI 網路模型上屬於 Application Layer 和 Presentation Layer 。

SMB 依靠底層的通訊協定主要是 NetBIOS over TCP/IP (簡稱 NBT )，而 NetBIOS 全名是 Network Basic Input/Output System，NetBIOS 屬於 Session Layer 的通訊協定。

Common Internet File System (CIFS) 是 SMB 的另一個分支版本 (dialect) ，一般會用「 SMB/CIFS 」稱之。_CIFS 與 SMB 的關係，相當於 JavaScript 與 ECMAScript 的關係。_從歷史來看，IBM 定義了最早的 SMB ，之後微軟自己實現 SMB 並定義了 MS-CIFS (簡稱 CIFS )，微軟繼續擴充 CIFS 增加許多的支援並定義了 MS-SMB (也簡稱 SMB ) ，以範圍來看，MS-CIFS 是 MS-SMB 的子集合。要特別注意 SMB 這個縮寫指的是 MS-SMB 還是最早的 SMB，在網路上查資料的時候，常常會搞不清楚 CIFS 與 SMB 的關係 (例如誰先定義、誰是誰的集合等)。

CIFS 是主從式架構 (client-server) 的通訊協定，由一系列「 SMB 命令 (SMB commands) 」組成，而 SMB 命令則是包含伺服器和用戶端交換的「 SMB 訊息 (SMB messages) 」。而 SMB 訊息則是包含 3 個部分： (1) 固定 32-bytes 的標頭。 (2) 可變長度的參數區塊。 (3) 可變長度的資料區塊。

* [What is SMB?](https://www.samba.org/cifs/docs/what-is-smb.html)
* [Implementing CIFS](http://www.ubiqx.org/cifs/)
* [Microsoft SMB Protocol and CIFS Protocol Overview](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365233(v=vs.85).aspx)
* [[MS-CIFS]: Common Internet File System (CIFS) Protocol](https://msdn.microsoft.com/en-us/library/ee442092.aspx)
* [[MS-SMB]: Server Message Block (SMB) Protocol](https://msdn.microsoft.com/en-us/library/cc246231.aspx)
* [[MS-SMB2]: Server Message Block (SMB) Protocol Versions 2 and 3](https://msdn.microsoft.com/en-us/library/cc246482.aspx)
* [RFC 1001 - Protocol standard for a NetBIOS service on a TCP/UDP transport: Concepts and methods](https://tools.ietf.org/html/rfc1001)
* [RFC 1002 - Protocol standard for a NetBIOS service on a TCP/UDP transport: Detailed specifications](https://tools.ietf.org/html/rfc1002)
* [Stop using SMB1 | Storage at Microsoft](https://blogs.technet.microsoft.com/filecab/2016/09/16/stop-using-smb1/)
* [SMB2, a complete redesign of the main remote file protocol for Windows &#8211; Jose Barreto&#039;s Blog](https://blogs.technet.microsoft.com/josebda/2008/12/09/smb2-a-complete-redesign-of-the-main-remote-file-protocol-for-windows/)

## Samba

[Samba](https://www.samba.org/) 是在 Linux/Unix 上實現 SMB/CIFS 通訊協定的自由軟體 (free software)，授權條款是 GPLv3 。

* [Samba: An Introduction](https://www.samba.org/samba/docs/SambaIntro.html)
* [Using Samba](http://www.oreilly.com/openbook/samba/book/index.html)
* [SambaWiki](https://wiki.samba.org/index.php/Main_Page)
* [samba](https://www.samba.org/samba/docs/current/man-html/samba.7.html)
* [Ubuntu Manpage: samba - A Windows AD and SMB/CIFS fileserver for UNIX](http://manpages.ubuntu.com/manpages/xenial/man7/samba.7.html)
* [Samba Release History](https://www.samba.org/samba/history/)

Samba 軟體套件可以做的事情有：

* SMB 伺服器 (server)，提供檔案/印表機分享的功能
* Windows Domain Controller
* NetBIOS (rfc1001/1002) nameserver
* SMB 用戶端 (client)，存取其他檔案/印表機分享
* 一些指令工具 (command-line tool)
* 提供 Linux 的檔案系統，如 cifsvfs, smbfs

smb.conf 是 Samba 的設定檔，這個設定檔同時可以設定 SMB 伺服器 (server) 和 SMB 用戶端 (client)。

* [Ubuntu Manpage: smb.conf - The configuration file for the Samba suite](http://manpages.ubuntu.com/manpages/xenial/man5/smb.conf.5.html)
* [smb.conf](https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html)

### Samba source code

* 官方 Git 儲存庫： [https://git.samba.org/samba.git](https://git.samba.org/samba.git)
* GitHub Mirror 儲存庫： [GitHub - samba-team/samba](https://github.com/samba-team/samba)

### Samba 開發相關資訊

* 開發概觀： [Samba Development](https://www.samba.org/samba/devel/)
* 開發者文件： [Developer Documentation - SambaWiki](https://wiki.samba.org/index.php/Developer_Documentation)
* 建置 Samba 是使用 [Waf](https://waf.io/) 這項工具，可參閱： [Waf - SambaWiki](https://wiki.samba.org/index.php/Waf), [Waf - Wikipedia](https://en.wikipedia.org/wiki/Waf)

## mount.cifs

mount.cifs 是 Linux 系統上的命令，可以將 CIFS 的分享路徑 mount 在本機上，在 Ubuntu 上屬於 cifs-utils 套件。以前是用 smbmount 命令，屬於 smbfs 套件，但 smbmount 現在已經被 mount.cifs 取代。

* [Ubuntu Manpage: mount.cifs - mount using the Common Internet File System (CIFS)](http://manpages.ubuntu.com/manpages/xenial/man8/mount.cifs.8.html)

## mount_smbfs

mount_smbfs 是 FreeBSD 和 Mac OS X 系統上的命令，可以將 CIFS 的分享路徑 mount 在本機上。

* [mount_smbfs(8)](https://www.freebsd.org/cgi/man.cgi?mount_smbfs(8))

## smbclient

smbclient 命令是用來存取 SMB/CIFS 資源的用戶端程式，在 Ubuntu 上屬於 smbclient 套件。

* [Ubuntu Manpage: smbclient - ftp-like client to access SMB/CIFS resources on servers](http://manpages.ubuntu.com/manpages/xenial/en/man1/smbclient.1.html)
* smbclient 原始碼：[https://github.com/samba-team/samba/tree/master/source3/client](https://github.com/samba-team/samba/tree/master/source3/client)
* smbclient4 原始碼：[https://github.com/samba-team/samba/tree/master/source4/client](https://github.com/samba-team/samba/tree/master/source4/client)

## libsmbclient

libsmbclient 是 SMB 用戶端的程式庫 (client library)，可以用來開發 SMB 的應用程式，像是 smbclient 就是使用 libsmbclient 開發的用戶端程式。程式庫中比較重要的是 SMBCCTX 結構，意思是 SMB client context information，因為大多數的 function 呼叫時都要傳遞此類型的引數。

* Samba 3 原始碼：[https://github.com/samba-team/samba/tree/master/source3/libsmb](https://github.com/samba-team/samba/tree/master/source3/libsmb)
* Samba 3 標頭檔：[https://github.com/samba-team/samba/blob/master/source3/include/libsmbclient.h](https://github.com/samba-team/samba/blob/master/source3/include/libsmbclient.h)
* Samba 4 原始碼 & 標頭檔：[https://github.com/samba-team/samba/tree/master/source4/libcli](https://github.com/samba-team/samba/tree/master/source4/libcli)

## 其他

* PowerShell 有關 SMB 操作的 Cmdlet： [SmbShare](https://docs.microsoft.com/en-us/powershell/module/smbshare/?view=win10-ps)
* [如何在 Windows 和 Windows Server 中偵測、啟用及停用 SMBv1、SMBv2 和 SMBv3](https://support.microsoft.com/zh-tw/help/2696547/how-to-detect-enable-and-disable-smbv1-smbv2-and-smbv3-in-windows-and)
