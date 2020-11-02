# Subversion

Subversion (簡稱 SVN) 一個版本控制系統 (Version Control System, VCS)，如同 Git 的功能。與 Git 最大差異在於，SVN 是集中式 (Centralized) 版本控制系統，而 Git 是分散式 (Distributed) 版本控制系統。

SVN 是 CollabNet, Inc. 公司在 2000 年創造的系統，最初是為了解決 CVS 的問題，可以看成是 CVS 的改良版本。後來在 2009 年成為 Apache 的一個開源專案，重新命名為 Apache Subversion ，目前 2020 年最新的版本是 version 1.14.0 。

## 觀念

SVN 除了可以管理程式碼的版本，也可以管理任何檔案，SVN 本身沒有限制可處理的檔案類型。

儲存庫 (repository) 是版本控制系統的核心，儲存所有 (各個版本) 檔案內容的資訊，通常是檔案系統樹 (filesystem tree)，包含檔案和目錄，與其之間的階層關係。

工作副本 (working copy) 是指某一個版本的檔案系統樹。

版本控制系統不只一個使用者使用，因此會遇到多人存取的問題。有兩個解決方法： lock-modify-unlock 和 copy-modify-merge ， SVN 採用的是 copy-modify-merge 解決方法，但也提供 lock 操作。

每一個版本的 filesystem tree 狀態， SVN 都會指定一個號碼， revision 號碼從 0 開始增加，對於一個 repository 是全域的 revision 號碼。

每個工作副本會有一個 .svn 資料夾，這是 SVN 用於管理工作副本的目錄。

一般而言，一個 repository 可能會儲存多個專案，因此每個子目錄會是一個專案 (用這樣的方式管理)。於是開發一個專案的時候， working copy 會是對 repository 的子目錄 check out 。

## 建議的 Repository 結構

SVN 建議 Repository 中的每個專案都有下列 3 個子目錄：

* trunk：主線 (main line)，產品開發的主線。
* branches：分支，開發新功能的分支。
* tags：某一條線快照的狀態。

## 指令

[Subversion Command-Line Client](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.html) 指令就是 `svn` ， `svn --version` 印出 client 的版本資訊。

* [svn add](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.blame.html) 把項目(檔案與目錄)加入下次 commit 的清單當中。
* [svn blame (praise, annotate, ann)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.blame.html) 顯示檔案每一行的作者和修訂資訊。
* [svn cat](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.cat.html) 輸出檔案內容，相當於 type 或 cat 指令。，通常用參數指定特定版本的內容。
* [svn changelist (cl)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.changelist.html) 把檔案加入變更清單中，用於下次 commit 使用。
* [svn checkout (co)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.checkout.html) 從儲存庫取出檔案到工作副本，例如 `svn checkout http://svn.apache.org/repos/asf/httpd/httpd/trunk httpd-trunk`。
* [svn cleanup](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.cleanup.html) 清理工作副本。
* [svn commit (ci)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.commit.html) 提交工作副本的變動到儲存庫中。
* [svn copy (cp)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.copy.html) 複製工作副本或儲存庫的項目(檔案與目錄)。
* [svn delete (del, remove, rm)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.delete.html) 把項目從工作副本或儲存庫中刪除。
* [svn diff (di)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.diff.html) 顯示兩個版本或兩個路徑之間的差異。
* [svn export](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.export.html) 匯出，把指定的目錄內容輸出到另一個目錄中。
* [svn help (h, ?)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.help.html) 幫助，後面接子命令 (subcommand) 名稱，例如 `svn help checkout` 查詢 checkout 的用法。
* [svn import](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.import.html) 匯入，把現有的檔案 commit 到儲存庫中。
* [svn info](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.info.html) 顯示本地或遠端項目的資訊。
* [svn list (ls)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.list.html) 列出儲存庫的檔案與目錄清單，相當於 dir 或 ls 指令。
* [svn lock](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.lock.html) 鎖住某個路徑，讓其他人不能 commit 他們的變更。
* [svn log](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.log.html) 顯示 commit log 訊息。
* [svn merge](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.merge.html) 合併來源至工作副本的路徑。
* [svn mergeinfo](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.mergeinfo.html) 取得合併相關的資訊。
* [svn mkdir](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.mkdir.html) 建立目錄。
* [svn move (mv)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.move.html) 移動檔案或目錄。
* [svn patch](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.patch.html)
* [svn propdel (pdel, pd)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propdel.html)
* [svn propedit (pedit, pe)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propedit.html)
* [svn propget (pget, pg)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propget.html)
* [svn proplist (plist, pl)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.proplist.html)
* [svn propset (pset, ps)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propset.html)
* [svn relocate](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.relocate.html) 搬遷工作副本至不同的 URL。
* [svn resolve](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.resolve.html) 解決工作副本中項目的衝突。
* [svn resolved](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.resolved.html) *不適用 (deprecated)* 移除衝突的狀態，請改用 `svn resolve --accept` 指令。
* [svn revert](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.revert.html) 回復 (undo) 本地工作副本的變動。
* [svn status (stat, st)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.status.html) 印出工作副本中檔案與目錄的狀態。
* [svn switch (sw)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.switch.html) 更新工作副本到不同的 URL。
* [svn unlock](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.unlock.html) 解開鎖住的路徑。
* [svn update (up)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.update.html) 更新你的工作副本。
* [svn upgrade](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.upgrade.html) 升級，給 SVN 1.7 版本以前升級 .svn 資料夾使用。

## 參考資料

* [Apache Subversion](https://subversion.apache.org/)
* [Version Control with Subversion](http://svnbook.red-bean.com/en/1.7/index.html)
* [Git 和 Subversion的相比 | 連猴子都能懂的Git入門指南  | 貝格樂（Backlog）](https://backlog.com/git-tutorial/tw/reference/git-svn.html)
* [如何讓 TortoiseSVN 僅匯出新增或修改過的檔案 | The Will Will Web](https://blog.miniasp.com/post/2008/09/09/Using-TortoiseSVN-to-Export-Only-Added-Modified-Files)
