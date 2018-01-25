# MariaDB

## 介紹

[MariaDB](https://mariadb.com/) 是一種關聯式資料庫管理系統 (relational database management system, RDBMS) ，MariaDB 是 [MySQL](https://www.mysql.com/) 的分支，用來直接替代 MySQL 。

* MySQL 的發明者是 3 位瑞典人： Michael Widenius, David Axmark, Allan Larsson ，他們同時也是 MySQL [AB](https://en.wikipedia.org/wiki/Aktiebolag) 公司的創辦人。
* [MySQL AB](https://en.wikipedia.org/wiki/MySQL_AB) 成立於 1995 年，昇陽電腦 (Sun Microsystems) 在 2008 年併購 MySQL AB，而甲骨文 (Oracle) 則在 2010 年併購昇陽電腦，目前 MySQL 隸屬於甲骨文，這也是為何 MySQL 的發明者要分支建立新的 MariaDB 的原因。
* MySQL 的命名來自於 Michael Widenius 大女兒 [My](https://dev.mysql.com/doc/refman/5.7/en/history.html) 的名字，而 MariaDB 則是來自於他小
女兒 [Maria](https://mariadb.com/kb/en/library/why-is-the-software-called-mariadb/) 的名字。
* MySQL 的 Logo 是海豚 (dolphin)，而 MariaDB 的 Logo 是海豹 (seal)。
* [MariaDB Documentation](https://mariadb.com/kb/en/library/documentation/)
* MariaDB source code 在官方 Git 儲存庫：[GitHub - MariaDB/server](https://github.com/MariaDB/server)，授權條款是 GPLv2 。

## 儲存引擎 (Storage Engines)

* [MyISAM](https://mariadb.com/kb/en/library/myisam-storage-engine/)，從 MySQL 3.23 至 5.5 之前是預設的儲存引擎。
* [Aria](https://mariadb.com/kb/en/library/aria-storage-engine/)
* [InnoDB](https://mariadb.com/kb/en/library/xtradb-and-innodb/) 源自於 Innobase Oy 公司，從 MariaDB and MySQL 5.5 開始是預設的儲存引擎。
* [XtraDB](https://mariadb.com/kb/en/library/about-xtradb/)
* [MEMORY](https://mariadb.com/kb/en/library/memory-storage-engine/)
* [BDB](https://mariadb.com/kb/en/library/bdb-obsolete/) 源自於 Berkeley DB ，從 MySQL 5.1 之後不支援，當然 MariaDB 也不支援了。

## 結構化查詢語言 (Structured Query Language, SQL)

* [Administrative SQL Statements - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/administrative-sql-statements/)
* [Account Management SQL Commands - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/account-management-sql-commands/)
* [Data Definition - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/data-definition/)
* [Data Manipulation - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/data-manipulation/)

## 資料類型 (Data Types)

* [Numeric Data Types - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/data-types-numeric-data-types/)
* [String Data Types - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/string-data-types/)
* [Date and Time Data Types - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/date-and-time-data-types/)

## 用戶端和工具程式 (Clients & Utilities)

* 命令列用戶端程式：[mysql](https://mariadb.com/kb/en/library/mysql-command-line-client/)

## 備份工具

### Percona XtraBackup

* [Percona XtraBackup - Documentation](https://www.percona.com/doc/percona-xtrabackup/LATEST/index.html)
* [Percona XtraBackup User Manual](https://www.percona.com/doc/percona-xtrabackup/LATEST/manual.html)

## Sample Database

* [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)
* [Employees Sample Database](https://dev.mysql.com/doc/employee/en/)
