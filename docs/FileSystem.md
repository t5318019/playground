# File Systems

## Z File System (ZFS)

ZFS 是一種檔案系統，全名是 Zettabyte File System，最早是由昇陽電腦 (Sun Microsystems) 所開發，開源碼的部分則有 OpenZFS 專案，ZFS 是世界上第一個 128 位元的檔案系統，可儲存至 256 quadrillion zettabytes，也就是 2^128 位元組。 (quadrillion = 10^15, zettabytes = 2^70 bytes)

ZFS 的設計有 3 個主要目標 (也是殺手級的優點) ：

1. 資料完整性 (data integrity) ：所有的資料都包含 64 位元的總和檢查碼 (checksum)，用於錯誤校正以確保完整性。
2. 共用儲存 (pooled storage) ：實體儲存裝置以儲存池的方式進行管理與使用。
3. 效能 (performance) ：具備多個快取機制以提升效能。

ZFS 特別的地方在於 ZFS 不僅是一個檔案系統，還包含磁碟區管理 (volume management) 的功能，磁碟區是以「儲存池 (storage pool) 」的方式使用。一般的檔案系統是建立在磁碟區上，但 ZFS 檔案系統 (稱為「資料集 (dataset)」) 則是建立在儲存池上，並且可多個 ZFS dataset 共用同一個儲存池。

可被加入儲存池的裝置共有 7 種類型，ZFS 稱為 vdev (全名是 virtual device) 。

1. disk: 區塊裝置 (block device) ，像是整個磁碟或磁碟分割區 (partition)。
2. file: 一般的檔案，通常用於測試和實驗的用途。
3. mirror: 2 個以上的區塊裝置，資料將被複製到多個裝置上，當裝置損毀到剩下一個時，資料還是能保證完整。
4. raidz, raidz2, raidz3: 類似磁碟陣列但改善傳統 RAID 的缺點，ZFS 提供 3 種等級的同位元資料 (parity) 保護。
    * raidz 也就是 raidz1，稱為 Single-parity RAID-Z ，類似於傳統的 RAID-5 。
    * raidz2，稱為 Double-parity RAID-Z ，類似於傳統的 RAID-6 。
    * raidz3，稱為 Triple-Parity RAID-Z 。
5. spare: 用於熱備援 (hot spare) ，當使用中的裝置失敗時才會進行替換，正常情形下是沒有使用 spare vdev 。
6. log: 用於 ZFS intent log (ZIL) 。預設的 ZIL 儲存於 pool 當中，為了更好的效能可以將 ZIL 另外儲存於單獨的磁碟中。
7. cache: 用於快取以提升效能。

儲存池建立後，我們就能夠在上面建立資料集，ZFS 有 4 種類型的 dataset 。

1. file system: 就是 ZFS 檔案系統，比較特別的是 ZFS 具有階層架構，稱為 ZFS File System Hierarchy 。
2. volume: 作為區塊裝置使用，例如用在 swap 裝置上，參考：[HOWTO use a zvol as a swap device](https://github.com/zfsonlinux/pkg-zfs/wiki/HOWTO-use-a-zvol-as-a-swap-device)。
3. snapshot: file system 或 volume 的快照。
4. bookmark: 快照的參照 (refernece)。

在 Ubuntu 16.04 以後安裝的指令：`apt install zfsutils-linux` 或 `apt install zfs` ( zfs 套件實際上是 zfsutils-linux ) 。 Ubuntu 與 ZFS 的版本關係如下。

| Ubuntu 版本               | ZFS 版本                                                     |
| ------------------------- | ------------------------------------------------------------ |
| 16.04 LTS (Xenial Xerus)  | [0.6.5.6](https://packages.ubuntu.com/xenial/zfsutils-linux) |
| 18.04 LTS (Bionic Beaver) | [0.7.5](https://packages.ubuntu.com/bionic/zfsutils-linux)   |
| 18.10 (Cosmic Cuttlefish) | [0.7.9](https://packages.ubuntu.com/cosmic/zfsutils-linux)   |
| 19.04 (Disco Dingo)       | [0.7.12](https://packages.ubuntu.com/disco/zfsutils-linux)   |

在 Ubuntu 16.04 會安裝下列服務：

| 服務名稱                                     | 說明                                 |
| -------------------------------------------- | ------------------------------------ |
| /etc/init.d/zfs-share                        | LSB: Network share OpenZFS datasetss |
| /lib/systemd/system/zfs-import-cache.service | Import ZFS pools by cache file       |
| /lib/systemd/system/zfs-import-scan.service  | Import ZFS pools by device scanning  |
| /lib/systemd/system/zfs-mount.service        | Mount ZFS filesystems                |
| /lib/systemd/system/zfs.target               | ZFS startup target                   |

### ZFS 相關指令與文件

主要有兩個指令， zpool 用來管理儲存池，而 zfs 則是用來管理資料集。

* [Ubuntu Manpage: zpool - configures ZFS storage pools](http://manpages.ubuntu.com/manpages/xenial/man8/zpool.8.html)
* [Ubuntu Manpage: zfs - configures ZFS file systems](http://manpages.ubuntu.com/manpages/xenial/man8/zfs.8.html)
* [Ubuntu Manpage: pool-features - ZFS pool feature descriptions](http://manpages.ubuntu.com/manpages/xenial/man5/zpool-features.5.html)
* [Ubuntu Manpage: zfs-events - Events created by the ZFS filesystem.](http://manpages.ubuntu.com/manpages/xenial/man5/zfs-events.5.html)
* [Ubuntu Manpage: zfs-module-parameters - ZFS module parameters](http://manpages.ubuntu.com/manpages/xenial/man5/zfs-module-parameters.5.html)
* [Ubuntu Manpage: zdb - Display zpool debugging and consistency information](http://manpages.ubuntu.com/manpages/xenial/en/man8/zdb.8.html)

### ZFS 參考資料

* [Chapter 19. The Z File System (ZFS)](https://www.freebsd.org/doc/handbook/zfs.html)
* [Oracle Solaris Administration: ZFS File Systems](https://docs.oracle.com/cd/E23824_01/html/821-1448/index.html)
* [Creating a ZFS File System Hierarchy - Oracle Solaris Administration: ZFS File Systems](https://docs.oracle.com/cd/E23824_01/html/821-1448/gaypa.html)
* [OpenZFS](http://open-zfs.org/wiki/Main_Page)
* [Aaron Toponce : Install ZFS on Debian GNU/Linux](https://pthree.org/2012/04/17/install-zfs-on-debian-gnulinux/)
* [GitHub - zfsonlinux/zfs: ZFS on Linux - the official OpenZFS implementation for Linux.](https://github.com/zfsonlinux/zfs)
* [ZFS - Ubuntu Wiki](https://wiki.ubuntu.com/ZFS)
* [Kernel/Reference/ZFS - Ubuntu Wiki](https://wiki.ubuntu.com/Kernel/Reference/ZFS)
* [Ubuntu – Details of package zfsutils-linux in xenial](https://packages.ubuntu.com/xenial/admin/zfsutils-linux)
* [The 'hidden' cost of using ZFS for your home NAS](http://louwrentius.com/the-hidden-cost-of-using-zfs-for-your-home-nas.html)
* [128-bit storage: are you high? | Oracle Jeff Bonwick&#039;s Blog](https://blogs.oracle.com/bonwick/128-bit-storage:-are-you-high)
* [How to improve ZFS performance &#8211; ICESQUARE &#8211; Solve Computer Server Problems, Computer Help, Server Support, Server Help](https://icesquare.com/wordpress/how-to-improve-zfs-performance/)

## File Allocation Table (FAT)

FAT 家族有 FAT12, FAT16, FAT32, 與 exFAT (或稱 FAT64 )，其中 FAT 後面的數字代表檔案系統記錄叢集位址的位元數，以下用 FAT32 舉例。而叢集是 FAT 檔案系統可以操作的最小單位，與磁碟可操作的最小單位是磁區 (sector) 不一樣。

FAT32 是用 32-bit 記錄叢集 (cluster) 的位址，FAT 32 是 Windows 95 以後才引進的檔案系統，理論上可定址到 2^32 個叢集，但 FAT32 保留最高 4 位元僅用 28 位元，以 FAT 支援最大的 32 kB 叢集 (一個叢集可儲存 32 kB 的資料) 來計算，FAT32 的最大磁碟區大小理論上是 8TB (= 32kB * 2^28)，但實際上依作業系統或磁碟工具的支援而定，目前以 Windows 來說是限制在 32GB 。

FAT32 支援的最大檔案大小為 4GB (實際上是 2^32 少 1 個位元組)，這是因為 FAT32 使用 4 bytes 儲存檔案大小資訊。

每個磁碟區最多可存放的檔案數量為 4177920 個 (大約 2^22 )，這主要是由於 ScanDisk 工具程式的限制導致。

一個目錄最多可存放的檔案數量為 65534 個，根目錄沒有限制數量。這主要是規格限制 16-bit (參閱 [Microsoft Extensible Firmware Initiative FAT32 File System Specification](http://download.microsoft.com/download/1/6/1/161ba512-40e2-4cc9-843a-923143f3456c/fatgen103.doc) 最後面)，所以是 2^16 少兩個 "." 與 ".." 目錄檔案。FAT 中的目錄本身也是一種「檔案」，是設定 ATTR_DIRECTORY (0x10) 屬性的檔案，而根目錄則是一種特別的目錄，根目錄具有 ATTR_VOLUME_ID (0x08) 屬性。

FAT 的資料在磁碟上是以 "Little-endian" 的位元組順序存放，低位元存放於低位址，高位元存放於高位址。檔名是不區分大小寫 (case-insensitive)。

FAT 檔案系統的紀錄資訊 (entry) 有下列屬性與用途：

* ATTR_READ_ONLY: 唯讀，不能寫入。
* ATTR_HIDDEN: 列出目錄下的檔案清單時，要不能被顯示。
* ATTR_SYSTEM: 作業系統使用的檔案。
* ATTR_VOLUME_ID: 一個磁碟區 (volume) 只能有一個，檔名將會是磁碟區名稱。
* ATTR_DIRECTORY: 標示這個檔案紀錄是一個目錄。
* ATTR_ARCHIVE: 用於備份工具程式標示是否已經備份。

FAT 檔案系統的時間資訊如下，注意到這些時間日期是以機器的本地時間為儲存資訊。

* DIR_CrtTimeTenth (1 byte): 建立時間，非必要，單位是 10 毫秒 (millisecond)，有效範圍是 0 到 199 ，因此檔案建立時間的精確度是 10 毫秒。
* DIR_CrtTime (2 bytes): 建立時間，非必要，最小單位是 2 秒，有效範圍是 00:00:00 到 23:59:58 。
* DIR_CrtDate (2 bytes): 建立日期，非必要，有效範圍是 1980-01-01 到 2107-12-31 。
* DIR_LstAccDate (2 bytes): 最後存取時間，非必要，有效範圍是 1980-01-01 到 2107-12-31 ，精確度是 1 天，因為沒有記錄時間。
* DIR_WrtTime (2 bytes): 最後寫入時間，必要，最小單位是 2 秒，有效範圍是 00:00:00 到 23:59:58 。
* DIR_WrtDate (2 bytes): 最後寫入日期，必要，有效範圍是 1980-01-01 到 2107-12-31 。

### FAT 參考資料

* [How FAT Works: Local File Systems](https://msdn.microsoft.com/en-us/library/cc776720)
* [Design of the FAT file system - Wikipedia](https://en.wikipedia.org/wiki/Design_of_the_FAT_file_system)
* [Windows File Systems - TechNet Articles - United States (English) - TechNet Wiki](https://social.technet.microsoft.com/wiki/contents/articles/5375.windows-file-systems.aspx)
* [Limitations of the FAT32 File System in Windows XP](https://support.microsoft.com/en-au/help/314463/limitations-of-the-fat32-file-system-in-windows-xp)
* [Working with File Systems](https://technet.microsoft.com/en-us/library/bb457112.aspx)
* [Description of the FAT32 File System](https://support.microsoft.com/zh-tw/help/154997/description-of-the-fat32-file-system)

## New Technology File System (NTFS)

NTFS 在 4kB 叢集大小下可支援最大 16TB 的磁碟區，若是用最大 64kB 的叢集，則磁碟區可支援到 256TB 的大小。架構上可定址到 2^64 - 1 個叢集，但實際上依 Windows 實作則是 2^32 - 1 個叢集。

每個磁碟區最多可存放的檔案數量為 4294967295 (= 2^32 - 1) 個。單個檔案架構上可至 16 EB (= 2^64 - 1k)，但實作上是 16TB (= 2^44 - 64k)。

* [File System Functionality Comparison (Windows)](https://msdn.microsoft.com/en-us/library/windows/desktop/ee681827(v=vs.85).aspx)
* [NTFS Technical Reference: Local File Systems | Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758691(v%3dws.10))
* [[MS-FSA]: Appendix A: Product Behavior](https://msdn.microsoft.com/en-us/library/ff469400.aspx)

## FUSE (Filesystem in Userspace)

FUSE 是 Linux 系統中使用者空間 (userspace) 檔案系統的框架，包含核心模組 (fuse.ko)、使用者空間的程式庫 (libfuse.*) 和工具程式 (fusermount)。FUSE 的優點在於使用非特權 (non-privileged) 掛載，因而提供使用新的檔案系統的可能性。例如 SSHFS (Secure SHell FileSystem) 就是以 FUSE 開發，底層使用 SFTP 通訊協定的一種檔案系統。

### libfuse 程式庫

libfuse 讓我們開發新的檔案系統，它提供兩種類型的API，兩者都是將 kernel 的請求 callback 呼叫傳入給主程式處理，差異如下：

* high-level, synchronous API:
    * 操作的是檔名 (filename) 或路徑 (path)
    * 使用 [include/fuse.h](https://github.com/libfuse/libfuse/blob/master/include/fuse.h) 標頭檔
    * 參考範例 [hello.c](https://github.com/libfuse/libfuse/blob/master/example/hello.c)
* low-level, asynchronous API:
    * 操作的是 [inode](http://www.linfo.org/inode.html)
    * 使用 [include/fuse_lowlevel.h](https://github.com/libfuse/libfuse/blob/master/include/fuse_lowlevel.h) 標頭檔
    * 參考範例 [hello_ll.c](https://github.com/libfuse/libfuse/blob/master/example/hello_ll.c)

如果要開發自己的檔案系統，可以參考 libfuse 裡面的 [example](https://github.com/libfuse/libfuse/tree/master/example) 的原始碼，裡面有很多可以參考，其中 [passthrough](https://github.com/libfuse/libfuse/blob/master/example/passthrough.c) 範例映射根目錄到掛載點，是檔案系統的經典範例。

* [https://www.kernel.org/doc/Documentation/filesystems/fuse.txt](https://www.kernel.org/doc/Documentation/filesystems/fuse.txt)
* [GitHub - libfuse/libfuse: The reference implementation of the Linux FUSE (Filesystem in Userspace) interface](https://github.com/libfuse/libfuse)
* [GitHub - libfuse/sshfs: A network filesystem client to connect to SSH servers](https://github.com/libfuse/sshfs)
* [libfuse: libfuse API documentation](http://libfuse.github.io/doxygen/)

## Overlay Filesystem

[OverlayFS](https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt) 是 Linux 的一種檔案系統，有時稱為聯合檔案系統 (union filesystem)。如同 OverlayFS 的名字，OverlayFS 是將一個檔案系統 (稱為 upper filesystem ) 覆蓋至另一個檔案系統 (稱為 lower filesystem ) 上，合併 (merge) 而成一個檔案系統。

* OverlayFS 在 [Linux 3.18](https://kernelnewbies.org/Linux_3.18) 合併到 kernel 中。
* lower filesystem 是 Linux 支援的任一檔案系統，可以是唯讀權限。
* upper filesystem 通常是可讀寫，但支援寫入可能需要額外資訊，NFS 就不太適合當上層的檔案系統。
* 若上下層都是唯讀，任何檔案系統都可以支援。
* [mount](http://manpages.ubuntu.com/manpages/xenial/en/man8/mount.8.html) 的時候使用 lowerdir 和 upperdir 選項指定上下層的目錄。另外需要設定 workdir 選項 (目錄必須為空) ，並且要和 upperdir 是相同的檔案系統。
    * mount 指定檔案系統 types 是用 "overlay" 的名稱，在還沒整進 kernel 前則是用 "overlayfs" 的名稱。
    * workdir 以前可忽略，但整進 kernel 後必須指定這個選項。
