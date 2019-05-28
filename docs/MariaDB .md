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
* [MySQL :: MySQL 5.7 Reference Manual :: MySQL Glossary](https://dev.mysql.com/doc/refman/5.7/en/glossary.html)

## 儲存引擎 (Storage Engines)

不論使用何種[儲存引擎](https://mariadb.com/kb/en/library/storage-engines/)，MySQL 使用 [.frm 檔案](https://dev.mysql.com/doc/internals/en/frm-file-format.html) 儲存資料表的定義資訊。我們必須針對用途與目的選擇正確的儲存引擎，可以使用 `SHOW ENGINES` 命令查看資料庫支援的儲存引擎有哪些。

* [MyISAM](https://mariadb.com/kb/en/library/myisam-storage-engine/) 從 MySQL 3.23 至 5.5 之前是預設的儲存引擎。
* [Aria](https://mariadb.com/kb/en/library/aria-storage-engine/)
* [InnoDB](https://mariadb.com/kb/en/library/xtradb-and-innodb/) 源自於 Innobase [Oy](https://en.wikipedia.org/wiki/Osakeyhti%C3%B6) 公司，從 MariaDB and MySQL 5.5 開始是預設的儲存引擎。
    * [XtraDB/InnoDB File Format](https://mariadb.com/kb/en/library/xtradbinnodb-file-format/): 有 2 種格式，原本的羚羊 (Antelope) 和後來新的梭魚 (Barracuda) ，預設是羚羊的檔案格式。
    * [XtraDB/InnoDB Storage Formats](https://mariadb.com/kb/en/library/xtradbinnodb-storage-formats/): 有 4 種格式: Compact, Redundant, Compressed, Dynamic ，預設是 Compact 的儲存格式。
* [XtraDB](https://mariadb.com/kb/en/library/about-xtradb/) 是 InnoDB 效能改善的分支版本，與 InnoDB 完全相容。
    * [Why does MariaDB 10.2 use InnoDB instead of XtraDB?](https://mariadb.com/kb/en/library/why-does-mariadb-102-use-innodb-instead-of-xtradb/)
* [MEMORY](https://mariadb.com/kb/en/library/memory-storage-engine/)
* [CSV](https://mariadb.com/kb/en/library/csv/)
* [BLACKHOLE](https://mariadb.com/kb/en/library/blackhole/)
* [MERGE](https://mariadb.com/kb/en/library/merge/) 也就是 MRG_MyISAM 儲存引擎。
* [ARCHIVE](https://mariadb.com/kb/en/library/archive/)
* [FEDERATED](https://mariadb.com/kb/en/library/federatedx-storage-engine/)
* [BDB](https://mariadb.com/kb/en/library/bdb-obsolete/) 源自於 Berkeley DB ，從 MySQL 5.1 之後不支援，當然 MariaDB 也不支援了。

## 結構化查詢語言 (Structured Query Language, SQL)

### 陳述式 (Statements)

你可以在用戶端程式使用 [HELP](https://mariadb.com/kb/en/library/help-command/) 命令查詢各種命令的語法和說明文件。

* [Administrative SQL Statements - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/administrative-sql-statements/)
    * [USE](https://mariadb.com/kb/en/library/use/): 使用指定的資料庫當作預設值。
    * [EXPLAIN](https://mariadb.com/kb/en/library/explain/)
    * [SET CHARACTER SET](https://mariadb.com/kb/en/library/set-character-set/)
    * [SET PASSWORD](https://mariadb.com/kb/en/library/set-password/)
    * [SHOW VARIABLES](https://mariadb.com/kb/en/library/show-variables/): 顯示 MariaDB 的系統變數。
    * [SHOW DATABASES](https://mariadb.com/kb/en/library/show-databases/): 顯示所有的資料庫名稱。
    * [SHOW TABLES](https://mariadb.com/kb/en/library/show-tables/): 顯示指定資料庫內所有的資料表名稱。
    * [SHOW COLUMNS](https://mariadb.com/kb/en/library/show-columns/): 顯示指定資料表內所有的欄位資訊。
    * [SHOW INDEX](https://mariadb.com/kb/en/library/show-index/): 顯示資料表的索引。
    * [SHOW CREATE DATABASE](https://mariadb.com/kb/en/library/show-create-database/): 顯示資料庫建立的資訊。
    * [SHOW CREATE TABLE](https://mariadb.com/kb/en/library/show-create-table/): 顯示資料表建立的資訊。
    * [SHOW STATUS](https://mariadb.com/kb/en/library/show-status/): 顯示伺服器的狀態。
    * [SHOW TABLE STATUS](https://mariadb.com/kb/en/library/show-table-status/): 顯示資料表的狀態。
* [Account Management SQL Commands - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/account-management-sql-commands/) (Data Control Languag, DCL)
    * [CREATE USER](https://mariadb.com/kb/en/library/create-user/)
    * [GRANT](https://mariadb.com/kb/en/library/grant/)
* [Data Definition - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/data-definition/) (Data Definition Language, DDL)
    * [CREATE](https://mariadb.com/kb/en/library/create/)
    * [DROP](https://mariadb.com/kb/en/library/drop/)
    * [ALTER](https://mariadb.com/kb/en/library/alter/)
* [Data Manipulation - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/data-manipulation/) (Data Manipulation Language, DML)
    * [SELECT](https://mariadb.com/kb/en/library/select/)
    * [INSERT](https://mariadb.com/kb/en/library/insert/)
    * [UPDATE](https://mariadb.com/kb/en/library/update/)
    * [DELETE](https://mariadb.com/kb/en/library/delete/)

### 語言結構 (Language Structure)

* [Identifier Names](https://mariadb.com/kb/en/library/identifier-names/)

## 資料類型 (Data Types)

注意：欄位定義的字串長度與中英文無關，也就是實際可儲存的字數，但佔用的 bytes 可能不同。可用 [LENGTH](https://mariadb.com/kb/en/library/length/) 和 [CHAR_LENGTH](https://mariadb.com/kb/en/library/char_length/) 取得相關資訊。

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

* 命令列用戶端程式： [mysql](https://mariadb.com/kb/en/library/mysql-command-line-client/)
* 管理 mysqld daemon 的程式： [mysqladmin](https://mariadb.com/kb/en/library/mysqladmin/)

## 設定

* [Configuring MariaDB with my.cnf - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/configuring-mariadb-with-mycnf/)
* [Server System Variables - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/server-system-variables/)

## High Availability & Performance Tuning

* [Replication Overview - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/replication-overview/)
* [MariaDB Galera Cluster - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/galera-cluster/)
* [MariaDB MaxScale - MariaDB Knowledge Base](https://mariadb.com/kb/en/mariadb-enterprise/maxscale/)
* [Optimization and Tuning - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/optimization-and-tuning/)

## MariaDB Galera Cluster

MariaDB Galera Cluster 和 [MySQL NDB Cluster](https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster.html) 是不一樣的！

在 [MariaDB 10.1](https://mariadb.com/kb/en/library/changes-improvements-in-mariadb-101/) 版本以後，Galera Cluster 已經是內建在 MariaDB 當中，透過設定 `wsrep_on=ON` 就能夠啟用 Galera Cluster 的功能，不需要另外安裝其他套件。注意目前只有 Linux 能使用 MariaDB Galera Cluster ，而且只支援 XtraDB/InnoDB 儲存引擎。

當 MariaDB 變成 Galera Cluster 之後，資料庫的資料會同步複製到各台 MariaDB 之中，其實是「[Virtually Synchronous Replication](https://mariadb.com/kb/en/library/about-galera-replication/)」。技術上是擴充 MariaDB 支援 [wsrep API](http://galeracluster.com/documentation-webpages/architecture.html) (Write-Set Replication API) ，並實作 Galera Replication 程式庫處理資料的同步。

Galera Cluster 的特色：

* Synchronous replication：同步指的是在任何時刻各台的資料都是一致的。優點是高可用性、Transaction 可以平行的在多台上執行。缺點是效能較差、實作較複雜。
* Active-active multi-master topology：架構上沒有 standby & slave。
* Read and write to any cluster node：每一台都可以存取。
* Automatic membership control, failed nodes drop from the cluster
* Automatic node joining
* True parallel replication, on row level
* Direct client connections, native MariaDB look & feel

參考資料：

* [Galera Cluster Documentation &#8212; Galera Cluster Documentation](http://galeracluster.com/documentation-webpages/)
* [Galera Cluster Status Variables - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/galera-cluster-status-variables/)：查看有哪些狀態，可以用 `SHOW STATUS LIKE 'wsrep%';` 指令顯示。
* [Galera Cluster System Variables - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/galera-cluster-system-variables/)：說明有哪些設定值。
* [wsrep_provider_options - MariaDB Knowledge Base](https://mariadb.com/kb/en/library/wsrep_provider_options/)：說明 Galera provider 的設定。

## 備份工具

### Percona XtraBackup

* [Percona XtraBackup - Documentation](https://www.percona.com/doc/percona-xtrabackup/LATEST/index.html)
* [Percona XtraBackup User Manual](https://www.percona.com/doc/percona-xtrabackup/LATEST/manual.html)

## Sample Database

* [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)
* [Employees Sample Database](https://dev.mysql.com/doc/employee/en/)
