# Web Distributed Authoring and Versioning (WebDAV)

## 介紹

WebDAV 是一種通訊協定，全名是 Web Distributed Authoring and Versioning ，用於分散式的編寫內容和版本管理，有點類似協同合作編輯的概念。WebDAV 實際上是 HTTP/1.1 的擴充功能，因此想要瞭解 WebDAV 的話，要先對 HTTP/1.1 有基本的認識。

### HTTP Methods for Distributed Authoring

* PROPFIND
* PROPPATCH
* MKCOL
* GET, HEAD
* POST
* DELETE
* PUT
* COPY
* MOVE
* LOCK
* UNLOCK

### Status Code Extensions to HTTP/1.1

* 207 Multi-Status
* 422 Unprocessable Entity
* 423 Locked
* 424 Failed Dependency
* 507 Insufficient Storage

### 參考資料

* [WebDAV Resources](https://web.archive.org/web/20171012072404/http://www.webdav.org/)
* [RFC 4918 - HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)](https://tools.ietf.org/html/rfc4918)
* [RFC 3253 - Versioning Extensions to WebDAV (Web Distributed Authoring and Versioning)](https://tools.ietf.org/html/rfc3253)
* [WebDAV：網際網路檔案管理的標準 | iThome](https://www.ithome.com.tw/node/33039)

## SabreDAV

[SabreDAV](http://sabre.io/) 是 PHP 中著名的 WebDAV 框架，可以用來開發 WebDAV 伺服器。

* [Getting Started - sabre/dav](http://sabre.io/dav/gettingstarted/)
* [Standards Support - sabre/dav](http://sabre.io/dav/standards-support/)
* [GitHub - sabre-io/dav: sabre/dav is a CalDAV, CardDAV and WebDAV framework for PHP](https://github.com/sabre-io/dav)
