# Python

[Python](https://www.python.org/) 是一種程式語言 (programming language)，由 [Guido van Rossum](https://twitter.com/gvanrossum) 所創造，有關 Python 的一些問題可以參考 [Python Frequently Asked Questions](https://docs.python.org/3/faq/index.html) 。

我是在 2009 年開始學習 Python，當時用的是 Python 2.5.4 版本，配合 Django 1.1 開發 Web Application。那時選用 Python 的原因是 Google App Engine 有支援，於是想說來學習新的程式語言看看。不過，在 2009 年的時候，Python 不像現在 2018 年那麼流行，參考資料和書籍相對少 (手指數的出來)，那時中文參考書有：

* Mark Lutz原著，陳建勳譯、蘇秉豐編，Python學習手冊‧第三版，台北：歐萊禮，2008。譯自：Learning Python, 3rd Edition. O'Reilly Media. _(入門經典，俗稱「老鼠書」，中文已經絕版)_
* 黃書逸，Python 3技術手冊，台北：碁峰，2009。

從 2012 年開始舉辦 PyCon Taiwan 年會，日後台灣有關 Python 研討會也越來越多。而 Python 相關的中文書與翻譯書大概從 2015 年開始如雨後春筍般的出現，現在加上人工智慧、機器學習的火紅，很多都使用 Python 開發，Python 在台灣也越來越熱門了，滿高興有更多人認識與學習 Python 這個程式語言。

Python 主要是用 C 實作的 CPython ，還有其他實作方式像是：[Jython](http://www.jython.org/), [IronPython](http://ironpython.net/), [PyPy](http://pypy.org/), [Python for .NET](https://pythonnet.github.io/) ，沒有特別說明一般都是用 CPython 。

## Python 2 or Python 3

Python 目前有 2 和 3 兩個版本，其中 Python 3.0 也稱為 Python 3000 或 Py3k，學習與使用上應該要用哪一個呢？(請參考下列資訊)

* [Python2orPython3 - Python Wiki](https://wiki.python.org/moin/Python2orPython3)
* [Python 2.x或3.x？ | iThome](https://www.ithome.com.tw/voice/104207)
* [PEP 3000 -- Python 3000 | Python.org](https://www.python.org/dev/peps/pep-3000/)
* [PEP 3099 -- Things that will Not Change in Python 3000 | Python.org](https://www.python.org/dev/peps/pep-3099/)
* [What’s New In Python 3.0 &#8212; Python 3.7.0 documentation](https://docs.python.org/3/whatsnew/3.0.html)

從 2008 年發佈第一個 [Python 3.0](https://www.python.org/download/releases/3.0/) 到現在已經過了 10 年，Python 3 的發展已趨於成熟 (包含相關可使用的程式庫)，而且 Python 2 的最後一版 [Python 2.7](https://www.python.org/dev/peps/pep-0373/) 也即將在 2020 年停止更新，現在絕對是可以學習與使用 Python 3 。

Python 2 和 Python 3 兩個版本是可以同時安裝在一個作業系統上，像是在 Ubuntu 系統上，目前 `python` 指令是 Python 2，而 `python3` 指令則是 Python 3。

Python 2 原始碼檔案的預設編碼是 ASCII ，但在 Python 3 的預設編碼則是 UTF-8 。原始碼檔案若要指定與預設不同的編碼方式，可以在檔案一開始加上特別的註解，稱為「編碼宣告(encoding declaration)」，像這樣：

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

## The Zen of Python

Python 程式語言的設計原則和哲學，定義在 [PEP 20 -- The Zen of Python | Python.org](https://www.python.org/dev/peps/pep-0020/) 共 19 條，有助於我們理解和學習 Python。你可以在互動模式中用 `import this` 顯示，或是執行 `python3 -c "import this"`，內容如下：

    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

PEP 20 列出 19 條箴言 (據說有 20 條但只記錄 19 條，最後一條還沒寫)，有沒有那些特別重要？是否有先後順序？搜尋結果看來是沒有。其中「比較好 (better than)」出現了 8 次，這幾句是程式設計的判斷依據。

Python 的設計哲學會在程式語言本身的語法 (Syntax) 和語意 (Semantics) 上表現。以下為中文翻譯，參考「Python 專家實踐指南: 搭乘專業開發者的學習便車」書本第 45 頁的內容。

    美比醜好。
    直接比間接好。
    簡單比複雜好。
    複雜比複雜化好。
    平鋪比套疊好。
    稀比密好。
    可讀性重要。
    特殊案例不足以破壞規矩。
    但實務重於純粹。
    別讓錯誤悄悄逃走。
    除非表明要安靜。
    面對含糊時堅拒猜測。
    應該有一個，最好只有一個，明顯的作法。
    然而這種做法，開始並不明顯，除非你是那個荷蘭佬。
    現在開始總比不作為好。
    但不作為通常比"馬上做"好。
    難以解釋的實作不好。
    容易解釋的實作也許不錯。
    命名空間是個好主意，多來幾個吧！

## 資料模型 (Data model)

* Python 中所有的資料都是物件 (object)，或是物件之間的關係。
* 每個物件都具有唯一身分 (identity)、型別 (type)、值 (value) 。
    * 唯一身分 (identity) 可由 `id()` 函式取得，對於 CPython 而言是物件的記憶體位置。
    * 型別可由 `type()` 函式取得
* 物件建立之後，不可改變物件的唯一身分與型別。
* 物件分成「可變更(mutable)」和「不可變更(immutable)」兩種，指的是物件的值是否可變更，由物件的型別決定。
* 判斷兩個物件是否相同 (同一個記憶體位置)，可以使用 `is` 運算子進行比較。
* 物件不需要明確地摧毀，Python 使用垃圾回收 (garbage collection) 記憶體管理機制。
* 某些物件可以包含其他物件，稱為容器 (container)。

### 標準型別的階層架構 (Standard type hierarchy)

Python 定義了需多內建的型別，各型別之間其實是有關連的階層架構，這裡指的是概念上，而不是物件導向上面的繼承關係。

* None
* NotImplemented
* Ellipsis
* numbers.Number
    * numbers.Integral
        * Integers (int)
        * Booleans (bool)
    * numbers.Real (float)
    * numbers.Complex (complex)
* Sequences
    * Immutable sequences
        * Strings
        * Tuples
        * Bytes
    * Mutable sequences
        * Lists
        * Byte Arrays
* Set types
    * Sets
    * Frozen sets
* Mappings
    * Dictionaries
* Callable types
    * User-defined functions
    * Instance methods
    * Generator functions
    * Coroutine functions
    * Asynchronous generator functions
    * Built-in functions
    * Built-in methods
    * Classes
    * Class Instances
* Modules
* Custom classes
* Class instances
* I/O objects (also known as file objects)
* Internal types
    * Code objects
    * Frame objects
    * Traceback objects
    * Slice objects
    * Static method objects
    * Class method objects

## Styles and Conventions

* [PEP 7 -- Style Guide for C Code | Python.org](https://www.python.org/dev/peps/pep-0007/)
* [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
* [PEP 257 -- Docstring Conventions | Python.org](https://www.python.org/dev/peps/pep-0257/)

### PEP 8

Guido 對程式碼的見解：閱讀程式碼比撰寫還要多。Style Guide 讓程式碼的風格一致，目的是改善程式碼的可讀性，也就是 PEP 20 中的 _Readability counts. (可讀性是重要的)_ 。

* 縮排 (indentation) 用 4 個空格 (space)。
* 懸掛縮排 (hanging indentation)，意思是除了第一行外，同一個段落的其他行都縮排。
* 縮排使用「空格」字元比較好，而不要使用 tab 字元 (除非舊有的程式碼是用 tab 方式)。
    * Python 3 不允許 space 和 tab 混用。
    * Python 2 允許 space 和 tab 混用，但應該將 tab 都改用 space 替代。
* 限制每行最多 79 字元的長度。
    * docstring 或註解 (comment) 應限制在 72 字元的長度。
    * 限制每行的字元數，優點是程式碼可以並排 (side-by-side) 顯示。而且在 code review 時可以方便地瀏覽。
    * 編輯器支援自動換行 (word wrap) 可能讓程式碼換行後的可讀性變差。編輯器視窗應設定為 80 字元。
    * 每行長度可以從 80 字元增加到 100 字元 (也就是限制 99 字元)。
    * 續行請使用反斜線 (backslash) 字元： \
* 換行 (line break) 請在二元運算子 (binary operator) 之前換行，依循數學方程式的慣例。
* 空行 (blank line)
    * Top-level function 和 class 前面需要 2 個空行。
    * 類別的方法前面需要 1 個空行。
    * 使用空行分隔程式碼中的邏輯部分。
* 原始碼檔案編碼
    * Python 2 使用 ASCII 編碼。
    * Python 3 使用 UTF-8 編碼。
    * 原始碼檔案編碼和預設相同，不應該加上編碼宣告。
* import
    * 每一行應該匯入一個 module。
    * 總是在原始碼檔案開頭 import 模組。在模組註解、docstring 之後，在模組的全域變數、常數之前。
    * 依下列分組，每組之間用 1 個空行。
        * Standard library
        * Third party library
        * Local application/library
    * 建議採用 absolute import 。
    * relative import 有明確的 (explicit) 和隱含的 (implicit) 兩種方式，不要使用 implicit relative import (在 Python 3 已經移除)。
    * 避免使用 wildcard import ，像是 `from <module> import *` 這樣的方式，因為這會造成名稱的不明確。
* Module-level "dunders" (開頭 2 個底線的變數)，在模組註解、docstring 之後，在模組 import 之前。
* 在 Python 當中，字串用單引號和雙引號是相同的，依可讀性決定用哪一種 (例如避免使用反斜線的跳脫字元)。
* Docstring 的 3 個引號，使用 3 個雙引號。

## 其他

* [The Python Language Reference &#8212; Python 3.7.0 documentation](https://docs.python.org/3/reference/index.html)
* [Glossary &#8212; Python 3.7.0 documentation](https://docs.python.org/3/glossary.html)
* [The History of Python](http://python-history.blogspot.com/)
* [Tanya Schlusser, Kenneth Reitz, The Hitchhiker's Guide to Python: Best Practices for Development, O'Reilly Media, 2016](http://shop.oreilly.com/product/0636920042921.do)
