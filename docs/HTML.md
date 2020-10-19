# HyperText Markup Language (HTML)

## 網頁表單 (Forms)

網頁上的表單提供使用者輸入資料，可以傳送給伺服器端的程式處理，這是網頁的重要功能。

使用者操作表單的元素稱為控制項 (controls)。每個控制項都應該有名稱 (name) 和值 (value) 兩個特性 (attribute)，其中 value 是指定控制項的初始值 (initial value)，因為使用者輸入資料會改變值，因此控制項設定的 value 是初始值。注意，控制項的名稱是不區分大小寫。

控制項在 HTML 當中是 input 元素，設定不同 type 特性則建立不同類型的輸入欄位，預設是 text，HTML 定義以下 type：

* text: 單行的文字輸入，多行則用 textarea 元素。
* password: 文字輸入，但隱藏文字的顯示(用*取代)，用於敏感資料的輸入，例如密碼欄位。
* checkbox: 核取方塊。
* radio: 選項按鈕。
* submit: 送出按鈕，用來將表單送出。
* reset: 重設按鈕，將表單的控制項重設回預設值。
* file: 檔案。
* hidden: 隱藏資訊，不顯示給使用者。
* image: 把影像當成送出按鈕。
* button: 按鈕(push button)。

除了 input 元素之外，表單還有以下元素可以使用：

* button: 按鈕，與 input 按鈕功能相同，但 button 元素可以有 HTML 內容，因此可以設計豐富的顯示內容。
* select: 下拉式選單，類似 ComboBox ，提供選項 (option) 讓使用者選擇。
* textarea: 多行的文字輸入。沒有 value 特性，初始值是元素的內容。

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

## 參考資料
* [HTML Standard](https://html.spec.whatwg.org/)