# HyperText Markup Language (HTML)

HTML 是組成一個網頁 (web page) 最基礎的語言，一個簡單的 HTML 文件大概長這樣：

```html
<!DOCTYPE html>
<html>

<head>
    <title>網頁的標題，表示這個文件的名稱。</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://necolas.github.io/normalize.css/8.0.1/normalize.css">
    <style>
        body {
            background-color;
            color: white;
        }
    </style>
</head>

<body>
    head 元素是描述 body 資訊的資料，而 body 是網頁的內容。
    <!--這是評論文字，不會顯示在網頁上-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</body>

</html>
```

這裡的範例是 HTML5 的規範，和前一個版本 HTML 4.01 的差異有：

* 第一行的 DOCTYPE 就是只有一種：`<!DOCTYPE html>`。
* link 和 style 元素不需要設定 type，預設類型就是 `type="text/css">`。
* script 元素不需要設定 type，預設類型就是 `type="text/javascript">`。

## 網頁表單 (Forms)

網頁上的表單提供使用者輸入資料，可以傳送給伺服器端的程式處理，這是網頁的重要功能。

使用者操作表單的元素稱為控制項 (controls)。每個控制項都應該有名稱 (name) 和值 (value) 兩個特性 (attribute)，其中 value 是指定控制項的初始值 (initial value)，因為使用者輸入資料會改變值，因此控制項設定的 value 是初始值。注意，控制項的名稱是不區分大小寫。

控制項在 HTML 當中是 input 元素，設定不同 type 特性則建立不同類型的輸入欄位，預設是 text，HTML 定義以下 type：

* text: 單行的文字輸入，多行則用 textarea 元素。
* password: 文字輸入，但隱藏文字的顯示(用*取代)，用於敏感資料的輸入，例如密碼欄位。
* checkbox: 核取方塊。
* radio: 選項按鈕。
* submit: 送出按鈕，用來將表單提交。
* reset: 重設按鈕，將表單的控制項重設回預設值。
* file: 檔案。
* hidden: 隱藏資訊，不顯示給使用者。
* image: 把影像當成送出按鈕。
* button: 按鈕(push button)。

除了 input 元素之外，表單還有以下元素可以使用：

* button: 按鈕，與 input 按鈕功能相同，但 button 元素可以有 HTML 內容，因此可以設計豐富的顯示內容，button 可以設定 3 種 type: submit, button, reset 。
* select: 下拉式選單，類似 ComboBox ，提供選項 (option) 讓使用者選擇。select 元素的內容包含 option 元素或 optgroup 元素，option 可以透過 selected 特性設定預設是否選取。
* textarea: 多行的文字輸入。沒有 value 特性，初始值是元素的內容。
* fieldset 元素和 legend 元素，用來組織結構。

HTML5 的 input 元素新增以下 type：

* color: 顏色，預設是黑色 (#000000)。
* date: 日期，年、月、日。
* datetime-local: 日期時間，年、月、日、小時、分鐘、秒。
* email: 電子郵件。
* month: 月份輸入，注意除了月份，也包含西元年的資訊。
* number: 數字，整數或浮點數。
* range: 滑杆，設定一個數字範圍，讓使用者滑動選取。
* search: 用於搜尋的文字輸入。
* tel: 電話號碼。
* time: 時間，小時、分鐘、秒。
* url: 網址，絕對 URL。
* week: 第幾週，也包含西元年的資訊。

控制項的標題使用 label 元素，可以將控制項置於 label 的內容，或是透過 for 特性設定到控制項的 id 特性，注意 label 的 for 是對應到 id 而不是 name。

禁用 (disable) 控制項請設定 disabled 特性，這會讓控制項失效，使用者將不能操作(變更值或選取)。可以禁用的元素有： button, input, group, optgroup, select, textarea

若控制項需要不能修改，請設定 readonly 特性，則控制項的值會是唯讀，可以唯讀的元素有 input 和 textarea 共 2 個。

元素 disable 和 readonly 相同的地方是使用者不能操作，差別在於 disable 的元素不會跟表單提交，但 readonly 會隨表單提交。

最後談 form 元素，以上元素都應該在 form 的內容當中。透過設定 form 的 method 特性可以設定 2 種表單提交的方法：

* method="get"，以 HTTP GET 方式傳送表單資料。
* method="post"，以 HTTP POST 方式傳送表單資料。

表單資料需要編碼送出，指定 enctype 特性設定編碼方式，分別是：

* enctype="application/x-www-form-urlencoded"，預設值，以 RFC 1738 編碼。
* enctype="multipart/form-data"，以 RFC 2388 編碼。

表單要送給伺服器的 URL 位置則是設定 action 特性。

## 參考資料
* [HTML Standard](https://html.spec.whatwg.org/)
* [HTML: HyperText Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML)
