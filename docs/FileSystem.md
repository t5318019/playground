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
