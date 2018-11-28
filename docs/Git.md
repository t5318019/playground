# Git

Git (the stupid content tracker) 是一個版本控制系統 (Version Control System, VCS)，在 2005 年由 Linus Torvalds 所開發。版本控制能夠記錄一個檔案或多個檔案的變更，因此你可以在之後回復以前的版本。

版本控制系統有三種類型：
* Local Version Control Systems: [Revision Control System, RCS](https://en.wikipedia.org/wiki/Revision_Control_System)
* Centralized Version Control Systems: [Concurrent Versions System, CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System), [Subversion, SVN](https://en.wikipedia.org/wiki/Apache_Subversion), [Perforce](https://en.wikipedia.org/wiki/Perforce)
* Distributed Version Control Systems: [Git](https://git-scm.com/), [Mercurial](https://en.wikipedia.org/wiki/Mercurial), [Bazaar](https://en.wikipedia.org/wiki/GNU_Bazaar), [Darcs](https://en.wikipedia.org/wiki/Darcs)

Git 是屬於 Distributed Version Control Systems 的類型。

## 觀念

Git 把資料當成「快照流 (stream of snapshots)」，不同於其他的 VCS 把資料的變更當成差異 (difference)。Git 有點像是一個小型的檔案系統。

大部分 Git 操作都在本機 (local) 上的檔案和資源，不需要和其他伺服器溝通。好處是操作的執行速度。

所有在 Git 的東西都有檢查碼 (checksum)，因此可以追蹤任何的資料變動和損毀。Git 用的是 SHA-1 雜湊演算法。

Git 的操作都是把資料加進 Git 的資料庫中，很難遺失任何資料和變動，或不能回復以前的版本。

Git 上的檔案有下列狀態：
* tracked: 在 Git 版本控制裡面。
    * committed: 已經儲存在 Git 的資料庫中。
    * modified: 檔案內容已變動。
    * staged: 將變動的檔案標示起來，用於準備 commit 到版本中。
    * unmodified: 檔案已經 committed 但內容沒有變動。
* untracked: 不在 Git 版本控制裡面。

Git 上的檔案有三大部分：
* .git Directory (Repository): 儲存 Git 資料庫的地方。
* Working Tree (Working Directory): 將某個版本 checkout 出來的工作區域。
* Staging Area:  儲存 staged 檔案的地方。

Git 的分支 (Branching) 可說是殺手級功能 (killer feature)，建立與切換分支非常快速。幾乎是即時完成，因此 Git 鼓勵使用者經常分支 (branch) 和合併 (merge)，意思也就是說我們開發的方式也要跟著改變。

## 常用指令

* Setup and Config
    * [git](https://git-scm.com/docs/git)
    * [config](https://git-scm.com/docs/git-config)
    * [help](https://git-scm.com/docs/git-help)
* Getting and Creating Projects
    * [init](https://git-scm.com/docs/git-init)
    * [clone](https://git-scm.com/docs/git-clone)
* Basic Snapshotting
    * [add](https://git-scm.com/docs/git-add)
    * [status](https://git-scm.com/docs/git-status)
    * [diff](https://git-scm.com/docs/git-diff)
    * [commit](https://git-scm.com/docs/git-commit)
    * [reset](https://git-scm.com/docs/git-reset)
    * [rm](https://git-scm.com/docs/git-rm)
    * [mv](https://git-scm.com/docs/git-mv)
* Branching and Merging
    * [branch](https://git-scm.com/docs/git-branch)
    * [checkout](https://git-scm.com/docs/git-checkout)
    * [merge](https://git-scm.com/docs/git-merge)
    * [mergetool](https://git-scm.com/docs/git-mergetool)
    * [log](https://git-scm.com/docs/git-log)
    * [stash](https://git-scm.com/docs/git-stash)
    * [tag](https://git-scm.com/docs/git-tag)
    * [worktree](https://git-scm.com/docs/git-worktree)
* Sharing and Updating Projects
    * [fetch](https://git-scm.com/docs/git-fetch)
    * [pull](https://git-scm.com/docs/git-pull)
    * [push](https://git-scm.com/docs/git-push)
    * [remote](https://git-scm.com/docs/git-remote)
    * [submodule](https://git-scm.com/docs/git-submodule)
* Inspection and Comparison
    * [show](https://git-scm.com/docs/git-show)
    * [log](https://git-scm.com/docs/git-log)
    * [diff](https://git-scm.com/docs/git-diff)
    * [shortlog](https://git-scm.com/docs/git-shortlog)
    * [describe](https://git-scm.com/docs/git-describe)
* Patching
    * [apply](https://git-scm.com/docs/git-apply)
    * [cherry-pick](https://git-scm.com/docs/git-cherry-pick)
    * [diff](https://git-scm.com/docs/git-diff)
    * [rebase](https://git-scm.com/docs/git-rebase)
    * [revert](https://git-scm.com/docs/git-revert)

## 參考資料

* [Git - Reference](https://git-scm.com/docs)
* [Git - Book](view-source:https://git-scm.com/book/en/v2)
* 【30 天精通 Git 版本控管】 作者: 黃保翕 ( Will 保哥 ) [Learn-Git-in-30-days/README.md at master · doggy8088/Learn-Git-in-30-days · GitHub](https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/README.md) 
* [Git FAQ - Git SCM Wiki](https://git.wiki.kernel.org/index.php/GitFaq)
