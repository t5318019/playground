# Markdown

## 介紹

Markdown 是一種格式語法(第一個字母M大寫)，用來簡化 HTML 的編並增加可讀性。 

* [Daring Fireball: Markdown](https://daringfireball.net/projects/markdown/)
* [Markdown - Wikipedia](https://en.wikipedia.org/wiki/Markdown)
* [Markdown 語法說明](http://markdown.tw/)
* [Markdown Guide](https://www.markdownguide.org/)

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

段落 (paragraph) 用一或多個空白行分開，會轉換成 HTML 的`<p>`元素。段落前面不應該縮排！沒有空白行分開的會在同一個段落裡面。

若要在段落中強制換行 (line break)，則在段落結尾處插入二個以上的空白，並換行 (enter鍵)，會轉換成 HTML 的`<br />`元素。

標題 (header) 有兩種風格，一種是 Setext-style，段落下方使用(也就是換行加上)等號 (=) 和連字符號 (-) 分別表示`<h1>`元素和`<h2>`元素。另一種是 atx-style，段落開頭用一至六個數字符號 (#) 表示`<h1>`元素到`<h6>`元素,
記得數字符號和標題文字之間要有空白或 Tab。atx-style 看來比較好用。

區塊引用文字 (blockquote) 使用 email-style 的角括號 (>) 開頭，像是電子郵件裡面轉寄郵件內容的方式，可以在引用文字的每一行開頭都加入角括號，或是只在引用的段落開頭加入角括號，會轉換成 HTML 的`<blockquote>`元素。區塊引用文字可以是巢狀 (nested) 多層，也可以在區塊中使用其他 Markdown 語法。

重點文字 (emphasis) 用星號 (*) 或底線 (_) 將文字包起來(劃定)，會轉換成 HTML 的`<em>`元素。

強調的文字用二個星號 (*) 或底線 (_) 將文字包起來(劃定)，會轉換成 HTML 的`<strong>`元素。

清單 (list) 有無序 (unodered) 清單和有序 (ordered) 清單二種，Markdown 都有支援。無序清單用星號 (*) 、加號 (+) 或連字符號 (-) 開頭，會轉換成 HTML 的`<ul>`和`<li>`元素。有序清單則用數字包含小數點開頭，會轉換成 HTML 的`<ol>`和`<li>`元素，要注意的是 Markdown 的有序清單數字和轉換後的 HTML 清單沒有關係，有序清單的數字總是從1開始。記得清單項目的內容與 Markdown 開頭的語法之間要有空白或 Tab。

超連結 (link) 用方括號和括弧 (parenthesis) ，像這樣

    [連結的文字](http://example.com/ "可有可無的標題")

會轉換成 HTML 的

    <a href="http://example.com" title="可有可無的標題">連結的文字</a>

圖片 (image) 類似超連結的語法，開頭多一個驚嘆號，像這樣

    ![圖片的替代文字](http://example.com/img.jpg "可有可無的標題")

會轉換成 HTML 的

    <img src="http://example.com/img.jpg" alt="圖片的替代文字" title="可有可無的標題" />

超連結和圖片還有另一種 reference-style 的語法，比較複雜一些請參考語法文件，上述的語法是 inline-style。

程式碼 (code) 用反引號 (\`) 包起來，如果是程式碼區塊則用四個空白縮排，或一個Tab縮排。記得程式碼區塊的前後要多一個空白行區隔前後段落。

水平線 (horizontal rule) 是在一行裡面插入三個以上的星號 (*) 、連字符號 (-) 或底線 (_) ，會轉換成 HTML 的`<hr />`元素。

## 其他重點

可以在 Markdown 文件裡面內嵌 (inline) HTML 的標籤 (tag)。對於區塊元素 (Block-level Element) 的標籤來說，起始標籤和結束標籤前後要多一個空白行，而且不應該縮排。而內嵌元素 (Text-level Element) 的話，直接在 Markdown 的段落裡面使用就可以了。

大於 (>) 、小於 (<) 、ampersand 符號 (&) 等等，在 Markdown 文件中不需要編寫成 HTML 的字元實體 (character entity)。

在文件當中要使用 Markdown 語法定義的字元，必須在字元前面加上反斜線 (\\)，有下列字元要跳脫：

    \   反斜線 (backslash)
    `   反引號 (backtick)
    *   星號 (asterisk)
    _   底線 (underscore)
    {}  花括號 (curly braces)
    []  方括號 (square brackets)
    ()  括弧 (parentheses)
    #   數字符號 (hash mark)
	+   加號 (plus sign)
	-   減號 (minus sign)，連字符號 (hyphen)
    .   點 (dot)
    !   驚嘆號 (exclamation mark)
