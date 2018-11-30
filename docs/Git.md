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

所有在 Git 的東西都有檢查碼 (checksum)，因此可以追蹤任何的資料變動和損毀。Git 用的是 SHA-1 雜湊演算法 (長度是 160 位元，40 個字元)。

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

Git 指令依操作用途分成兩大類：
* Plumbing commands: 偏向 VCS 底層內部的操作功能。
* Porcelain commands: 比較方便使用的 (user-friendly)、一般操作 VCS 的功能。

## 常用指令

* Setup and Config
    * [git](https://git-scm.com/docs/git): the stupid content tracker
    * [config](https://git-scm.com/docs/git-config): Get and set repository or global options
    * [help](https://git-scm.com/docs/git-help): Display help information about Git
* Getting and Creating Projects
    * [init](https://git-scm.com/docs/git-init): Create an empty Git repository or reinitialize an existing one
    * [clone](https://git-scm.com/docs/git-clone): Clone a repository into a new directory
* Basic Snapshotting
    * [add](https://git-scm.com/docs/git-add): Add file contents to the index
    * [status](https://git-scm.com/docs/git-status): Show the working tree status
    * [diff](https://git-scm.com/docs/git-diff): Show changes between commits, commit and working tree, etc
    * [commit](https://git-scm.com/docs/git-commit): Record changes to the repository
    * [reset](https://git-scm.com/docs/git-reset): Reset current HEAD to the specified state
    * [rm](https://git-scm.com/docs/git-rm): Remove files from the working tree and from the index
    * [mv](https://git-scm.com/docs/git-mv): Move or rename a file, a directory, or a symlink
* Branching and Merging
    * [branch](https://git-scm.com/docs/git-branch): List, create, or delete branches
    * [checkout](https://git-scm.com/docs/git-checkout): Switch branches or restore working tree files
    * [merge](https://git-scm.com/docs/git-merge): Join two or more development histories together
    * [mergetool](https://git-scm.com/docs/git-mergetool): Run merge conflict resolution tools to resolve merge conflicts
    * [log](https://git-scm.com/docs/git-log): Show commit logs
    * [stash](https://git-scm.com/docs/git-stash): Stash the changes in a dirty working directory away
    * [tag](https://git-scm.com/docs/git-tag): Create, list, delete or verify a tag object signed with GPG
    * [worktree](https://git-scm.com/docs/git-worktree): Manage multiple working trees
* Sharing and Updating Projects
    * [fetch](https://git-scm.com/docs/git-fetch): Download objects and refs from another repository
    * [pull](https://git-scm.com/docs/git-pull): Fetch from and integrate with another repository or a local branch
    * [push](https://git-scm.com/docs/git-push): Update remote refs along with associated objects
    * [remote](https://git-scm.com/docs/git-remote): Manage set of tracked repositories
    * [submodule](https://git-scm.com/docs/git-submodule): Initialize, update or inspect submodules
* Inspection and Comparison
    * [show](https://git-scm.com/docs/git-show): Show various types of objects
    * [log](https://git-scm.com/docs/git-log): Show commit logs
    * [diff](https://git-scm.com/docs/git-diff): Show changes between commits, commit and working tree, etc
    * [shortlog](https://git-scm.com/docs/git-shortlog): Summarize git log output
    * [describe](https://git-scm.com/docs/git-describe): Give an object a human readable name based on an available ref
* Patching
    * [apply](https://git-scm.com/docs/git-apply): Apply a patch to files and/or to the index
    * [cherry-pick](https://git-scm.com/docs/git-cherry-pick): Apply the changes introduced by some existing commits
    * [diff](https://git-scm.com/docs/git-diff): Show changes between commits, commit and working tree, etc
    * [rebase](https://git-scm.com/docs/git-rebase): Reapply commits on top of another base tip
    * [revert](https://git-scm.com/docs/git-revert): Revert some existing commits

## 內部運作和實作原理

技術上來看，Git 底層是一個內容尋址的檔案系統 (content-addressable filesystem) ，上層則是一個 VCS 的操作介面。

有 4 個重要的東西在 .git 資料夾中：
* HEAD 檔案: 指向目前 check out 的分支。
* index 檔案: 儲存  Staging Area 的資訊。
* objects 目錄: Git 儲存內容 (content) 的地方，或稱 object database 。
* refs 目錄: 儲存指向 commit 物件的資訊，有 3 部分：heads, remotes, tags。

Git objects 的 3 種類型 (type)：
* blob: 單純儲存檔案的內容。
* tree: 用於儲存 object 的權限、類型、檔案名稱。
* commit: 儲存 commit 資訊。

### Plumbing Commands

* [cat-file](https://git-scm.com/docs/git-cat-file): Provide content or type and size information for repository objects
* [check-ignore](https://git-scm.com/docs/git-check-ignore): Debug gitignore / exclude files
* [checkout-index](https://git-scm.com/docs/git-checkout-index): Copy files from the index to the working tree
* [commit-tree](https://git-scm.com/docs/git-commit-tree): Create a new commit object
* [count-objects](https://git-scm.com/docs/git-count-objects): Count unpacked number of objects and their disk consumption
* [diff-index](https://git-scm.com/docs/git-diff-index): Compare a tree to the working tree or index
* [for-each-ref](https://git-scm.com/docs/git-for-each-ref): Output information on each ref
* [hash-object](https://git-scm.com/docs/git-hash-object): Compute object ID and optionally creates a blob from a file
* [ls-files](https://git-scm.com/docs/git-ls-files): Show information about files in the index and the working tree
* [merge-base](https://git-scm.com/docs/git-merge-base): Find as good common ancestors as possible for a merge
* [read-tree](https://git-scm.com/docs/git-read-tree): Reads tree information into the index
* [rev-list](https://git-scm.com/docs/git-rev-list): Lists commit objects in reverse chronological order
* [rev-parse](https://git-scm.com/docs/git-rev-parse): Pick out and massage parameters
* [show-ref](https://git-scm.com/docs/git-show-ref): List references in a local repository
* [symbolic-ref](https://git-scm.com/docs/git-symbolic-ref): Read, modify and delete symbolic refs
* [update-index](https://git-scm.com/docs/git-update-index): Register file contents in the working tree to the index
* [update-ref](https://git-scm.com/docs/git-update-ref): Update the object name stored in a ref safely
* [verify-pack](https://git-scm.com/docs/git-verify-pack): Validate packed Git archive files
* [write-tree](https://git-scm.com/docs/git-write-tree): Create a tree object from the current index

## 參考資料

* [Git - Reference](https://git-scm.com/docs)
* [Git - Book](https://git-scm.com/book/en/v2)
* 【30 天精通 Git 版本控管】 作者: 黃保翕 ( Will 保哥 ) [Learn-Git-in-30-days/README.md at master · doggy8088/Learn-Git-in-30-days · GitHub](https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/README.md) 
* [Git FAQ - Git SCM Wiki](https://git.wiki.kernel.org/index.php/GitFaq)
