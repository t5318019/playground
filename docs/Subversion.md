# Subversion

Subversion (簡稱 SVN) 一個版本控制系統 (Version Control System, VCS)，如同 Git 的功能。與 Git 最大差異在於，SVN 是集中式 (Centralized) 版本控制系統，而 Git 是分散式 (Distributed) 版本控制系統。

SVN 是 CollabNet, Inc. 公司在 2000 年創造的系統，最初是為了解決 CVS 的問題，可以看成是 CVS 的改良版本。後來在 2009 年成為 Apache 的一個開源專案，重新命名為 Apache Subversion 。

## Repository 結構建議

SVN 建議 Repository 中的每個專案都有下列 3 個子目錄：

* trunk：主線 (main line)，產品開發的主線。
* branches：分支，開發新功能的分支。
* tags：某一條線快照的狀態。

## 指令

[Subversion Command-Line Client](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.html) 指令就是 `svn` ， `svn --version` 印出 client 的版本資訊。目前 2020 年最新的版本是 version 1.14.0 。

* [svn add](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.blame.html)
* [svn blame (praise, annotate, ann)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.blame.html)
* [svn cat](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.cat.html)
* [svn changelist (cl)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.changelist.html)
* [svn checkout (co)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.checkout.html)
* [svn cleanup](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.cleanup.html)
* [svn commit (ci)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.commit.html)
* [svn copy (cp)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.copy.html)
* [svn delete (del, remove, rm)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.delete.html)
* [svn diff (di)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.diff.html)
* [svn export](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.export.html)
* [svn help (h, ?)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.help.html)
* [svn import](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.import.html)
* [svn info](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.info.html)
* [svn list (ls)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.list.html)
* [svn lock](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.lock.html)
* [svn log](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.log.html)
* [svn merge](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.merge.html)
* [svn mergeinfo](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.mergeinfo.html)
* [svn mkdir](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.mkdir.html)
* [svn move (mv)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.move.html)
* [svn patch](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.patch.html)
* [svn propdel (pdel, pd)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propdel.html)
* [svn propedit (pedit, pe)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propedit.html)
* [svn propget (pget, pg)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propget.html)
* [svn proplist (plist, pl)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.proplist.html)
* [svn propset (pset, ps)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propset.html)
* [svn relocate](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.relocate.html)
* [svn resolve](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.resolve.html)
* [svn resolved](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.resolved.html)
* [svn revert](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.revert.html)
* [svn status (stat, st)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.status.html)
* [svn switch (sw)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.switch.html)
* [svn unlock](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.unlock.html)
* [svn update (up)](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.update.html)
* [svn upgrade](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.upgrade.html)

## 參考資料

* [Apache Subversion](https://subversion.apache.org/)
* [Version Control with Subversion](http://svnbook.red-bean.com/en/1.7/index.html)
