# Ruby Programming Language

[Ruby](https://www.ruby-lang.org/) 是來自日本的程式語言，發明者是[松本行弘 (Yukihiro Matsumoto)](https://matz.rubyist.net/)。在 2007 年因為 Ruby on Rails (簡稱 RoR ) 的風潮，第一次聽到這個語言，沒有深入使用，現在因為想展開第二曲線 (The Second Curve)，選了這個 **程式設計師的摯友 (A Programmer's Best Friend)** 來學習 (這是官網的標題)。

> Ruby 的設計精神：Ruby is designed to make programmers happy.

也就是說，用了 Ruby 會更快樂！在松本行弘的書上也說，Ruby 可以提高生產力，看來不錯，要試試看才知道。自己想到一個問題：學習 Ruby 程式到有生產力，我需要花多少時間？

學習一個程式語言到具有生產力，大概需要：
1. 程式語言的語法，如資料型別、判斷、迴圈。
2. 程式語言的組織架構，如模組、副程式。
3. 相關程式庫和套件管理系統。
4. 如何除錯 debug。
5. 如何發行佈署。

以每天投入 2 小時，有沒有可能在 30 天內學會 Ruby 用來生產軟體呢？ 對於有經驗的程式開發者，我想應該不難吧。

## 從 0 到 1

先安裝 Ruby，自己的系統是 Microsoft Windows 10，所以使用 [RubyInstaller](https://rubyinstaller.org/) ，下載 Ruby+Devkit 2.7.X (x64) 安裝程式，目前已經有 Ruby 3.0 ，考量套件相容等因素，對於學習者來說別自找麻煩(太新的東西不要用)。

第一個程式「Hello, World!」，程式碼如下(可以開啟 Interactive Ruby 輸入執行)：

```ruby
puts "Hello, World!"
```

`puts` 是一個 function，用途是把字串印出來，並且在字串後面加上換行 (newline)。除了用 `puts` 印東西，還可以用 `print` 和 `p` 。

寫到這邊發現一個問題，`puts` 是和 Python 的 `print` 類似的內建函式嗎？不需要引入任何程式庫就可以使用了嗎？

的確，原來是 Ruby 直譯器會自動載入 [Kernel](https://docs.ruby-lang.org/en/2.7.0/Kernel.html) 模組，`puts`, `print`, `p` 都是 Public Instance Method。

如果想要知道 Ruby 執行時有哪些模組可用，請呼叫 `Module.constants` 這個 Public Class Method 檢視，Kernel 就是其中之一。

回到 `puts`, `print`, `p` 這三個 function，差別在於：

* `puts` 等於是呼叫 `$stdout.puts`，`$stdout` 是全域變數之一，代表目前的 STDOUT。(要知道有哪些全域變數，直接呼叫 `global_variables` 可以知道)
* `print` 是 Kernel 模組的方法之一，把物件輸出到 `$stdout`。
* `p` 也是 Kernel 模組的方法之一，呼叫每個物件的 `inspect` 方法。

這邊提到 `$stdout` 這個變數， Ruby 的變數不用是「$」開頭 (但 PHP 就必須是)，錢符號 (dollar sign) 代表是「全域變數」，相當好的語言設計，看名稱就知道範疇。


## Ruby 程式語言重點

* 動態語言 (dynamic language)，變數使用前不需要先宣告。
* 手稿語言 (scripting language)，不需要編譯。
* 完全地物件導向！所有東西都是物件。不像其他語言有非物件的基本型別。
* 呼叫函式或方法，可以不需要括弧。因為 Ruby 設計上不允許直接存取物件的屬性，需要透過存取方法 (accessor method)，換句話說，取得物件的屬性等於呼叫getter，忽略括弧吧！

# 參考資料
* David Flanagan and Yukihiro Matsumoto, The Ruby Programming Language, O'Reilly Media, 2008
* [Documentation for Ruby 2.7.0](https://docs.ruby-lang.org/en/2.7.0/)