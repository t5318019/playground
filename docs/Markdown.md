# Markdown

## 介紹

Markdown 是一種格式語法(第一個字母M大寫)，用來簡化 HTML 的編並增加可讀性。 

* [Daring Fireball: Markdown](https://daringfireball.net/projects/markdown/)
* [Markdown - Wikipedia](https://en.wikipedia.org/wiki/Markdown)
* [Markdown 語法說明](http://markdown.tw/)

### 客製化

GitHub Flavored Markdown (簡稱GFM)是 Github 使用的語法。

* [Mastering Markdown · GitHub Guides](https://guides.github.com/features/mastering-markdown/)
* [A formal spec for GitHub Flavored Markdown | GitHub Engineering](https://githubengineering.com/a-formal-spec-for-github-markdown/)
* [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)

### 標準化

[CommonMark](http://commonmark.org/) 試圖解決各個客製化 Markdown 語法的定義問題。

### 語法設計哲學

Markdown 是設計用來容易閱讀和容易編寫的語法，不過可讀性 (Readability) 是第一優先。一個 Markdown 文件看起來不應該像有標記 (mark up) 的樣子。

Markdown 的語法靈感主要來自於純文字電子郵件 (plain text email) ，還有受到 [Setext][1], [atx][2], [Textile][3], [reStructuredText][4], [Grutatext][5], [EtText][6] 的影響。

[1]: http://docutils.sourceforge.net/mirror/setext.html
[2]: http://www.aaronsw.com/2002/atx/
[3]: http://textism.com/tools/textile/
[4]: http://docutils.sourceforge.net/rst.html
[5]: http://www.triptico.com/software/grutatxt.html
[6]: http://ettext.taint.org/doc/

Markdown 的設計傾向用於 Web 的寫作格式，但不是用來取代 HTML。

HTML 是文件發佈的格式，而 Markdown 是文件編寫的格式。

## 語法重點

段落 (paragraph) 用一或多個空白行分開，會轉換成 HTML 的`<p>`元素。

標題 (header) 有兩種風格，一種是 Setext-style，段落下方用等號 (=) 和連字符號 (-) 分別表示`<h1>`元素和`<h2>`元素。另一種是 atx-style，段落開頭用一至六個數字符號 (#) 表示`<h1>`元素到`<h6>`元素。atx-style 看來比較好用。

區塊引用文字 (blockquote) 用角括號 (>) 開頭，會轉換成 HTML 的`<blockquote>`元素。

重點文字 (emphasis) 用星號 (*) 或底線 (_) 將文字包起來(劃定)，會轉換成 HTML 的`<em>`元素。

清單 (list) 分為無序 (unodered) 清單和有序 (ordered) 清單二種。無序清單用星號 (*) 、加號 (+) 或連字符號 (-) 開頭，有序清單則用數字包含小數點開頭。

超連結 (link) 用方括號和括弧 (parenthesis) ，像這樣

    [連結的文字](http://example.com/ "可有可無的標題")

會轉換成 HTML 的

    <a href="http://example.com" title="可有可無的標題">連結的文字</a>

圖片 (image) 類似超連結的語法，像這樣

    ![圖片的替代文字](http://example.com/img.jpg "可有可無的標題")

會轉換成 HTML 的

    <img src="http://example.com/img.jpg" alt="圖片的替代文字" title="可有可無的標題" />

超連結和圖片還有另一種 reference-style 的語法，比較複雜一些請參考語法文件。上述的語法是 inline-style。

程式碼 (code) 用反引號 (`) 包起來，如果是程式碼區塊則用四個空白縮排，或一個Tab縮排。
