# JavaScript

JavaScript 簡稱 JS ，是一種程式語言，1995 年由布蘭登·艾克 (Brendan Eich) 發明，主要是用在網頁 (web page) 上，在瀏覽器上執行，早期是這樣沒錯。不過，在 2009 年的時候，Node.js 被瑞安·達爾 (Ryan Dahl) 創造出來了，現在 JS 也能在伺服器端上執行了。

其實在更早的時候，Netscape 也有把 JS 應用在 Netscape Enterprise Server 上，稱之為 Server-Side JavaScript，但這段歷史我沒有經過。唯一有印象的是，在 2004 年要學習 JS 的時候，中文的參考書籍非常稀少，瀏覽器也沒有「開發人員工具」，JS 程式 debug 就是用 alert 慢慢除錯 (據說可以用 Visual Studio 進行除錯)。以現在 2020 年來看，當時真是黑暗時代，很難想像 JS 會有今天的發展。

## 重點整理

* JavaScript 不是 Java，只是當年 Java 很紅，借用他的名字。原本命名為 LiveScript 。
* JS 的標準是 ECMAScript (簡稱 ES)，目前瀏覽器都有支援 2009 年訂定的 ES5 (第五版)。在 2015 年訂定了 ECMAScript 第六版 (ES6)，也稱為 ECMAScript 2015，之後則都是以西元年當作版本號碼，例如 ECMAScript 2020。詳細的版本資訊：[JavaScript Versions](https://www.w3schools.com/js/js_versions.asp)。
* JS 是手稿語言 (scripting language)，不同於像是 C++ 或 Java 的編譯語言 (Compiled language)。
* JS 是基於原型 (prototype-based) 的物件導向程式語言。不同於基於類別 (class-based) 的物件導向程式語言，例如 C++ 或 Java 有 class 語法，詳細可以參考：[Details of the object model - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Details_of_the_Object_Model)。
* 變數是區分大小寫 (case sensitive)，變數開頭可以是 $ 或 _，以及 Unicode 字元，也就是允許中文字(或其他文字)當變數名稱。

## 關鍵字 (keywords) & 保留字 (reserved words)

關鍵字是程式語言識別使用，不能拿來當作變數名稱。ES5 到 ES6 增加了 7 個關鍵字。

|     | ES6 (共 33 個) | ES5 (共 26 個) |
| --- | -------------- | -------------- |
| 1   | break          | break          |
| 2   | case           | case           |
| 3   | catch          | catch          |
| 4   | class          |                |
| 5   | const          |                |
| 6   | continue       | continue       |
| 7   | debugger       | debugger       |
| 8   | default        | default        |
| 9   | delete         | delete         |
| 10  | do             | do             |
| 11  | else           | else           |
| 12  | export         |                |
| 13  | extends        |                |
| 14  | finally        | finally        |
| 15  | for            | for            |
| 16  | function       | function       |
| 17  | if             | if             |
| 18  | import         |                |
| 19  | in             | in             |
| 20  | instanceof     | instanceof     |
| 21  | new            | new            |
| 22  | return         | return         |
| 23  | super          |                |
| 24  | switch         | switch         |
| 25  | this           | this           |
| 26  | throw          | throw          |
| 27  | try            | try            |
| 28  | typeof         | typeof         |
| 29  | var            | var            |
| 30  | void           | void           |
| 31  | while          | while          |
| 32  | with           | with           |
| 33  | yield          |                |

保留字是 JS 未來可能會使用的關鍵字，所以也不要盡量不要當作變數名稱。其中 ES5 的幾個保留字在 ES6 已經是關鍵字了。

|     | ES5 (共 16 個) | ES6 (共 8 個) |
| --- | -------------- | ------------- |
| 1   | class          |               |
| 2   | const          |               |
| 3   | enum           | enum          |
| 4   | export         |               |
| 5   | extends        |               |
| 6   | implements     | implements    |
| 7   | import         |               |
| 8   | interface      | interface     |
| 9   | let            |               |
| 10  | package        | package       |
| 11  | private        | private       |
| 12  | protected      | protected     |
| 13  | public         | public        |
| 14  | static         |               |
| 15  | super          |               |
| 16  | yield          |               |
| 17  |                | await         |

不能當作變數名稱的除了關鍵字和保留字，還有 null, true, false 這三個 (Null 和 Boolean 型別的值)。等等，注意 undefined (Undefined 型別的值) 不是關鍵字，所以 undefined 可以當作變數名稱！

## 內建型別 (built-in types) & 內建物件 (built-in objects)

內建型別的值稱為「原始值」(primitive values)，通常也把內建型別稱為「原始型別」，JS 的內建型別有 5 種：

| 內建型別  | 說明                        |
| --------- | --------------------------- |
| Undefined | 值就是 `undefined`          |
| Null      | 值就是 `null`               |
| Boolean   | 值有 `true` 跟 `false` 兩種 |
| Number    | IEEE 754 標準的雙精度浮點數 |
| String    | UTF-16 編碼的字串           |

這邊可以看到 JS 的型別相當簡單，數字就只有一種，沒有區分整數和浮點數，文字也沒有區分字元和字串。

內建物件如下：

|     | ES6 (共 25 個)    | ES5 (共 11 個) |
| --- | ----------------- | -------------- |
| 1   | Array             | Array          |
| 2   | ArrayBuffer       |                |
| 3   | Boolean           | Boolean        |
| 4   | DataView          |                |
| 5   | Date              | Date           |
| 6   | Error             | Error          |
| 7   | Function          | Function       |
| 8   | Generator         |                |
| 9   | GeneratorFunction |                |
| 10  | Iteration         |                |
| 11  | JSON              | JSON           |
| 12  | Map               |                |
| 13  | Math              | Math           |
| 14  | Number            | Number         |
| 15  | Object            | Object         |
| 16  | Promise           |                |
| 17  | Proxy             |                |
| 18  | Reflect           |                |
| 19  | RegExp            | RegExp         |
| 20  | Set               |                |
| 21  | String            | String         |
| 22  | Symbol            |                |
| 23  | TypedArray        |                |
| 24  | WeakMap           |                |
| 25  | WeakSet           |                |

全域物件 (global object) 是未執行 JS 就已經建立的物件，在瀏覽器當中全域物件就是 `window` ，全域物件包含一些屬性 (property)，存取的時候不需要指定全域物件，例如 Math 和 window.Math 是一樣的，ES5 的全域物件屬性如下：

* 值屬性，都是唯讀不能修改
  1. [NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN) 就是 "Not-a-Number"，不是一個數字。
  2. [Infinity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity) 正無限大的數字。
  3. [undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) 未定義的原始值。如果變數沒有給值，那這個變數的值就是 undefined 。
* 函式屬性
  1. [eval](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
  2. [parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
  3. [parseFloat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)
  4. [isNaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
  5. [isFinite](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isFinite)
  6. [decodeURI](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
  7. [decodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
  8. [encodeURI](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
  9. [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)
* 建構子屬性，基本上是內建物件的建構子
  1. [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
  2. [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
  3. [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
  4. [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
  5. [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
  6. [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
  7. [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
  8. [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
  9. [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
  10. [EvalError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/EvalError)
  11. [RangeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
  12. [ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
  13. [SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
  14. [TypeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
  15. [URIError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
* 其他屬性
  1. [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
  2. [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

## 運算子 (operators) & 運算式(expressions)

運算式 (expression) 是程式語言中會計算出值的語法，當中會用到運算子 (operator)。 JS 當中的運算子如下：

| 類型              | 一元 (unary)       | 二元 (binary)                           | 三元 (ternary) |
| ----------------- | ------------------ | --------------------------------------- | -------------- |
| 賦值 (assignment) |                    | = *=	/=	%=	+=	-=	<<=	>>=	>>>=	&=	^= \|= |                |
| 算術 (arithmetic) | ++ --              | + - * / %                               |                |
| 關係 (relational) |                    | < > <= >= instanceof in                 |                |
| 比較 (equality)   |                    | == != === !==                           |                |
| 位元 (bitwise)    | ~                  | & ^ \| << >> >>>                        |                |
| 邏輯 (logical)    | !                  | &&                                      |                |
| 其他              | delete void typeof | ,                                       | ?:             |


## 參考資料

* [ECMAScript Language Specification - ECMA-262 Edition 5.1](https://www.ecma-international.org/ecma-262/5.1/)
* [ECMAScript 2015 Language Specification &ndash; ECMA-262 6th Edition](http://www.ecma-international.org/ecma-262/6.0/)
* [ECMAScript® Language Specification](https://tc39.es/ecma262/)
* [JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [JavaScript Tutorial](https://www.w3schools.com/js/)
* [重新認識 JavaScript :: 2018 iT 邦幫忙鐵人賽](https://ithelp.ithome.com.tw/users/20065504/ironman/1259)
* [許國政 (Kuro)，*0 陷阱！0 誤解！8 天重新認識 JavaScript！*，台北：博碩文化，2019。](http://www.drmaster.com.tw/Bookinfo.asp?BookID=MP21913)
* [Unicode與JavaScript字串 | iThome](https://www.ithome.com.tw/voice/131688)
