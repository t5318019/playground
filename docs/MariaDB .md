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
    * TINYINT: 1 byte，範圍是 -128 至 127 或 0 至 255 。
    * BOOLEAN: 與 TINYINT(1) 是同義字。
    * SMALLINT: 2 bytes，範圍是 -32768 至 32767 或 0 至 65535 。
    * MEDIUMINT: 3 bytes，範圍是 -8388608 至 8388607 或 0 至 16777215 。
    * INT, INTEGER: 4 bytes，範圍是 -2147483648 至 2147483647 或 0 至 4294967295 。
    * BIGINT: 8 bytes，範圍是 -9223372036854775808 至 9223372036854775807 或 0 至 18446744073709551615 。
    * DECIMAL: 同義字有 DEC, NUMERIC, FIXED ，唯一的定點數 (fixed-point number) 資料類型。整數部分可達 65 位數，預設是 10 位數；小數部分可達 38 位數，預設是 0 位數。
    * FLOAT: 單精度 (single-precision) 浮點數，範圍請參閱 IEEE 754 標準，精確度大約是 7 位小數。
    * DOUBLE: 同義字有 DOUBLE PRECISION, REAL ，雙精度 (double-precision) 浮點數，範圍請參閱 IEEE 754 標準，精確度大約是 15 位小數。
    * BIT: 二進制位元，長度可達 64 bits，預設是 1 bit 。
* [String Data Types - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/string-data-types/)
    * CHAR: 固定長度的字串，最長至 255 字元。
    * VARCHAR: 可變長度的字串，最長至 65535 字元。
    * BINARY: 固定長度的字串，類似 CHAR 但以二進制儲存。
    * CHAR BYTE: 與 BINARY 是同義字。
    * VARBINARY: 可變長度的字串，類似 VARCHAR 但以二進制儲存。
    * TINYBLOB: 可變長度的資料，最長至 255 位元，在字首以 1-byte 記錄資料長度。
    * BLOB: 可變長度的資料，最長至 65535 位元，在字首以 2-byte 記錄資料長度。
    * MEDIUMBLOB: 可變長度的資料，最長至 16777215 位元，在字首以 3-byte 記錄資料長度。
    * LONGBLOB: 可變長度的資料，最長至 4294967295 位元，在字首以 4-byte 記錄資料長度。
    * TINYTEXT: 可變長度的字串，最長至 255 字元，在字首以 1-byte 記錄字串長度。
    * TEXT: 可變長度的字串，最長至 65535 字元，在字首以 2-byte 記錄字串長度。
    * MEDIUMTEXT: 可變長度的字串，最長至 16777215 字元，在字首以 3-byte 記錄字串長度。
    * LONGTEXT: 可變長度的字串，最長至 4294967295 字元，在字首以 4-byte 記錄字串長度。
    * ENUM: 列舉字串。
* [Date and Time Data Types - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/date-and-time-data-types/)
    * DATE: 日期，範圍從  '1000-01-01' 至 '9999-12-31' 。
    * TIME: 時間，範圍從 '-838:59:59.999999' 至 '838:59:59.999999' 。
    * DATETIME: 日期時間，範圍從 '1000-01-01 00:00:00.000000' 至 '9999-12-31 23:59:59.999999' 。
    * TIMESTAMP: 時間戳記，能儲存的範圍從 '1970-01-01 00:00:01' (UTC) 至 '2038-01-19 05:14:07' (UTC) 。
    * YEAR: 西元年，範圍從 1901 至 2155 。
* [Data Type Storage Requirements - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/data-type-storage-requirements/)

## 用戶端和工具程式 (Clients & Utilities)

* 命令列用戶端程式：[mysql](https://mariadb.com/kb/en/library/mysql-command-line-client/)

## 備份工具

### Percona XtraBackup

* [Percona XtraBackup - Documentation](https://www.percona.com/doc/percona-xtrabackup/LATEST/index.html)
* [Percona XtraBackup User Manual](https://www.percona.com/doc/percona-xtrabackup/LATEST/manual.html)

## Sample Database

* [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)
* [Employees Sample Database](https://dev.mysql.com/doc/employee/en/)
