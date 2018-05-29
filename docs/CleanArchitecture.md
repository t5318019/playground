# Clean Architecture

* 書籍：Robert C. Martin, [Clean Architecture: A Craftsman's Guide to Software Structure and Design](http://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166), Prentice Hall, 2017.
* [搞笑談軟工: [還少一本書] Clean Architecture](http://teddy-chen-tw.blogspot.tw/2017/11/clean-architecture.html)

## Part I: Introduction

設計 (design) 與架構 (architecture) 有沒有什麼不同？沒有。在不同的上下文 (context) 當中，架構指的是 Hight-level 的結構 (structure)，而設計指的是 Low-level 的細節 (details)，兩者的決策 (decision) 互相有關，架構與設計是整體的全部 (all part of the same whole)。

軟體架構的目標：_“The goal of software architecture is to minimize the human resources required to build and maintain the required system.”_

每個軟體系統提供兩種不同的價值 (value)：
* 行為 (behavior)：軟體讓機器依據需求做出想要的行為。
* 架構 (architecture)：軟體必須夠「軟」，能夠很輕易的改變行為，因此軟體必須很容易變動 (change)。變動有「範圍 (scope)」與「形狀 (shape)」兩種，軟體架構設計必須對於形狀的變動是未知的 (agnostic)。

## Part II: Starting with the Bricks: Programming Paradigms

軟體架構開始於程式碼 (code)，程式碼是用程式語言 (programming language) 編寫，從程式語言發明以來一直都有一些變革和改進，但重要的改變是：程式語言背後的設計典範 (paradigm)，典範是程式的方法 (ways of programming)，和程式的語言無關。典範告訴我們可以使用那些程式的結構 (structure)，以及什麼時候可以使用它。

至今有下列三種典範，這三種各自移除了程式設計師 (programmer) 可用的某部分能力，這些典範告訴我們不要做什麼，比告訴我們可以做什麼還要多。

### Structured programming

_Structured programming imposes discipline on direct transfer of control._

* 第一個被採用的典範，但不是第一個被發明的。
* 由 Edsger Wybe Dijkstra 發現於 1968 年。

### Object-oriented programming

_Object-oriented programming imposes discipline on indirect transfer of control._

* 第二個被採用的典範。
* 由 Ole Johan Dahl and Kristen Nygaard 發現於 1966 年。

### Functional programming

_Functional programming imposes discipline upon assignment._

* 最近才被採用，但是是最早被發明的典範。
* 由 Alonzo Church 發明於 1936 年。

## Part III: Design Principles

SRP: The Single Responsibility Principle

OCP: The Open-Closed Principle

LSP: The Liskov Substitution Principle

ISP: The Interface Segregation Principle

DIP: The Dependency Inversion Principle

## Part IV: Component Principles

### Component cohesion

REP: The Reuse/Release Equivalence Principle

CCP: The Common Closure Principle

CRP: The Common Reuse Principle

### Component Coupling

ADP: The Acyclic Dependencies Principle

SDP: The Stable Dependencies Principle

SAP: The Stable Abstractions Principle

## Part V: Architecture


## Part VI: Details


## Part VII: Appendix

