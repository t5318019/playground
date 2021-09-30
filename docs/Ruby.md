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

## Ruby 程式語言重點

* 完全地物件導向！所有東西都是物件。不像其他語言有非物件的基本型別。
* 呼叫函式或方法，可以不需要括弧。因為 Ruby 設計上不允許直接存取物件的屬性，需要透過存取方法 (accessor method)，換句話說，取得物件的屬性等於呼叫getter，忽略括弧吧！

# 參考資料
* David Flanagan and Yukihiro Matsumoto, The Ruby Programming Language, O'Reilly Media, 2008
