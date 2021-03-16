# MySQL

因為工作上使用的是 MySQL，不是 MariaDB ，所以另外建立一份文件記錄。這邊主要是參考 [MySQL :: MySQL 5.7 Reference Manual](https://dev.mysql.com/doc/refman/5.7/en/) 。

如何在 Windows 上手動安裝 MySQL 可以參考這裡： [2.3.4 Installing MySQL on Microsoft Windows Using a noinstall ZIP Archive
](https://dev.mysql.com/doc/refman/5.7/en/windows-install-archive.html)，若用 `mysqld --install` 指令安裝成 Windows 服務，預設的服務名稱是 MySQL。

如果將 MySQL 安裝成 Windows 服務，可以使用命令 `net start MySQL` 啟動，使用 `net stop MySQL` 停止，重新啟動則先停止再啟動。

MySQL 的資料庫內容存放在[資料路徑](https://dev.mysql.com/doc/refman/5.7/en/data-directory.html)下，每一個目錄都是一個資料庫，此資料庫目錄下的子目錄則是每一個資料表的內容，也就是說資料庫、資料表和目錄結構是有關係的。



## Data Manipulation Statements

* [SELECT Statement](https://dev.mysql.com/doc/refman/5.7/en/select.html)


## Sample Database

* [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/sakila-introduction.html)
* [Employees Sample Database](https://dev.mysql.com/doc/employee/en/)
