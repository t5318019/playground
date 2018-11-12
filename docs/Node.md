# Node

## 介紹

Node.js 是一個建於 V8 JavaScript 引擎上的一套伺服端平台，採用 JavaScript 程式語言，Node.js 使用事件驅動 (event-driven)、非阻斷式 (non-blocking) 的輸入/輸出模型，因此具有輕量級、高效率的特性，特別適合用於資料密集 (data-intensive)、即時 (real-time) 的應用領域。

[瑞安‧達爾 (Ryan Dahl)](https://github.com/ry) 是 Node.js 的創造者，Node.js 開始於 2009 年。

Node 就是 Node.js ，正確名稱是 Node.js (字母 N 大寫) ，一般都簡稱 Node 。

在 Node 當中，每個檔案是一個模組 (module) ，與 Python 的模組概念一樣。Node 使用 `require()` 函式引入模組，像是 `const http = require('http');` 的用法引入 [http](https://nodejs.org/dist/latest-v10.x/docs/api/http.html) 模組。

Node 的全域物件 (Global objects) 是 `global` ，但在瀏覽器的 JavaScript 執行環境下則是 `window` 。另外，與瀏覽器的 JavaScript 最大差異，Node 有 [process](https://nodejs.org/dist/latest-v10.x/docs/api/process.html) 物件以及 [Buffer](https://nodejs.org/dist/latest-v10.x/docs/api/buffer.html) 物件，為了處理多程序和二進位資料，這兩種情況在瀏覽器中都不會發生。

* [Guides | Node.js](https://nodejs.org/en/docs/guides/)
* [Command Line Options | Node.js v10.x Documentation](https://nodejs.org/dist/latest-v10.x/docs/api/cli.html)
* [Global Objects | Node.js v10.x Documentation](https://nodejs.org/dist/latest-v10.x/docs/api/globals.html)
* [Index | Node.js v10.x Documentation](https://nodejs.org/dist/latest-v10.x/docs/api/)
* [Node.js Foundation · GitHub](https://github.com/nodejs)

## npm

npm 全名是 node package manager，用來管理 JavaScript 的套件 (packages) 。所謂套件，指的是一個目錄中有 package.json 檔案的資料夾。套件的用途是提供可重複使用的 (reusable) 程式碼，當作元件來使用。

npm 通常有三個意思

* npm 網站 [https://www.npmjs.com/](https://www.npmjs.com/)
* npm 的資料庫，package 的註冊清單
* npm 用戶端 CLI 程式

package 的安裝有兩種方式：locally or globally.

* 局部 (locally)：預設模式，會安裝在當前路徑下，名稱為 node_modules 的目錄中，通常是把套件當 Library 使用，局部安裝可以避免版本衝突的問題。
* 全域 (globally)：安裝在「作業系統」上，通常是有 CLI 程式的套件。

npm 的版本規範是用 Semantic Versioning (語意化版本)。

npm 有 scoped packages ，類似名稱空間 (namespace) 的概念。scope 是以「@」字元開頭，在「/」斜線之間，整個套件名稱為@scope/project-name 。請參閱 [14 - How to work with scoped packages | npm Documentation](https://docs.npmjs.com/getting-started/scoped-packages)

npm 當中定義了套件 (packages) 和模組 (module) ，兩者很容易搞混，套件不必是模組(非強制條件)，套件也可能只是 CLI package 。請參閱 [19 - Understanding packages and modules | npm Documentation](https://docs.npmjs.com/getting-started/packages)

* [The npm Blog — kik, left-pad, and npm](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm)
* [NPM &amp; left-pad: Have We Forgotten How To Program? - David Haney - Blogging my experiences as a developer and engineering manager.](https://www.davidhaney.io/npm-left-pad-have-we-forgotten-how-to-program/)

## 參考資料

* Shelley Powers 原著，楊尊一譯，Node 學習手冊，台北：碁峰資訊，2016。譯自：Learning Node: moving to the server side, 2nd Edition
* Tom Hughes-Croucher & Mike Wilson, Node: Up and Running, O'Reilly Media, 2012
