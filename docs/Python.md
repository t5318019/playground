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

Python 2 原始碼檔案的預設編碼是 ASCII ，但在 Python 3 的預設編碼則是 UTF-8 。原始碼檔案若要指定與預設不同的編碼方式，可以在檔案一開始加上特別的註解，像這樣：

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

PEP 20 列出 19 條箴言 (據說有 20 條但只記錄 19 條)，有沒有那些特別重要？是否有先後順序？搜尋結果看來是沒有。其中「比較好 (better than)」出現了 8 次，這幾句是程式設計的判斷依據。

Python 的設計哲學會在程式語言本身的語法 (Syntax) 和語意 (Semantics) 上表現。

## 資料模型 (Data Model)

* Python 中所有的資料都是物件 (object)，或是物件之間的關係。
* 每個物件都具有唯一身分 (identity)、型別 (type)、值 (value) 。
    * 唯一身分 (identity) 可由 id() 函式取得，對於 CPython 而言是物件的記憶體位置。
    * 型別可由 type() 函式取得。
* 物件分成「可變更(mutable)」和「不可變更(immutable)」兩種，指的是物件的值是否可變更，由物件的型別決定。

## Styles and Conventions

* [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
* [PEP 257 -- Docstring Conventions | Python.org](https://www.python.org/dev/peps/pep-0257/)

## 其他

* [The Python Language Reference &#8212; Python 3.7.0 documentation](https://docs.python.org/3/reference/index.html)
* [Glossary &#8212; Python 3.7.0 documentation](https://docs.python.org/3/glossary.html)
* [The History of Python](http://python-history.blogspot.com/)
