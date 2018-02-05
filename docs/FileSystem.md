# File Systems

## Z File System (ZFS)

ZFS 是一種檔案系統，全名是 Zettabyte File System，最早是由昇陽電腦 (Sun Microsystems) 所開發，開源碼的部分則有 OpenZFS 專案，ZFS 是 128 位元的檔案系統。

ZFS 特別的地方在於不僅是一個檔案系統，還包含磁碟區管理 (volume management) 的功能。

* [Chapter 19. The Z File System (ZFS)](https://www.freebsd.org/doc/handbook/zfs.html)
* [OpenZFS](http://open-zfs.org/wiki/Main_Page)
* [ZFS - Ubuntu Wiki](https://wiki.ubuntu.com/ZFS)
* [Oracle Solaris Administration: ZFS File Systems](https://docs.oracle.com/cd/E23824_01/html/821-1448/index.html)

## File Allocation Table (FAT)

FAT 家族有 FAT12, FAT16, FAT32, 與 exFAT (或稱 FAT64 )，其中 FAT 後面的數字代表檔案系統記錄叢集位址的位元數，以下用 FAT32 舉例。

FAT32 是用 32-bit 記錄叢集 (cluster) 的位址，理論上可定址到 2^32 個叢集，但 FAT32 保留最高 4 位元僅用 28 位元，以 FAT 支援最大的 32 kB 叢集來計算，FAT32 的最大磁碟區大小理論上是 8TB (= 32kB * 2^28)，但實際上依作業系統或磁碟工具的支援而定，以 Windows 來說目前限制在 32GB 。

FAT32 支援的最大檔案大小為 4GB (實際上是 2^32 少 1 個位元組)，這是因為 FAT32 使用 4 bytes 儲存檔案大小資訊。

每個磁碟區最多可存放的檔案數量為 4177920 個 (大約 2^22 )，這主要是由於 ScanDisk 工具程式的限制導致。

一個目錄最多可存放的檔案數量為 65534 個，根目錄沒有限制數量。這主要是規格限制 16-bit (參閱 [Microsoft Extensible Firmware Initiative FAT32 File System Specification](http://download.microsoft.com/download/1/6/1/161ba512-40e2-4cc9-843a-923143f3456c/fatgen103.doc) 最後面)，所以是 2^16 少兩個 "." 與 ".." 目錄檔案。

* [How FAT Works: Local File Systems](https://msdn.microsoft.com/en-us/library/cc776720)
* [Design of the FAT file system - Wikipedia](https://en.wikipedia.org/wiki/Design_of_the_FAT_file_system)
* [Windows File Systems - TechNet Articles - United States (English) - TechNet Wiki](https://social.technet.microsoft.com/wiki/contents/articles/5375.windows-file-systems.aspx)
* [Limitations of the FAT32 File System in Windows XP](https://support.microsoft.com/en-au/help/314463/limitations-of-the-fat32-file-system-in-windows-xp)
* [Working with File Systems](https://technet.microsoft.com/en-us/library/bb457112.aspx)

## New Technology File System (NTFS)

* [File System Functionality Comparison (Windows)](https://msdn.microsoft.com/en-us/library/windows/desktop/ee681827(v=vs.85).aspx)

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
