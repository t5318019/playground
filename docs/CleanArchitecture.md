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

軟體架構開始於程式碼 (code)，程式碼是用程式語言 (programming language) 編寫，從程式語言發明以來一直都有一些變革和改進，但重要的改變是：程式語言背後的設計典範 (paradigm)，典範是寫程式的方法 (ways of programming)，和寫程式用的語言無關。典範告訴我們可以使用那些程式的結構 (structure)，以及什麼時候可以使用它。

至今有下列三種典範，這三種各自移除了程式設計師 (programmer) 可用的某部分能力，這些典範告訴我們不要做什麼，比告訴我們可以做什麼還要多。

### Structured programming

_Structured programming imposes discipline on direct transfer of control._

* 第一個被採用的典範，但不是第一個被發明的。
* 由 Edsger Wybe Dijkstra 發現於 1968 年，著名文章：Go To Statement Considered Harmful.
* Böhm 和 Jacopini 在 1966 年證明所有程式可以由三種結構所建構： sequence, selection, iteration。

### Object-oriented programming

_Object-oriented programming imposes discipline on indirect transfer of control._

* 第二個被採用的典範。
* 由 Ole Johan Dahl and Kristen Nygaard 發現於 1966 年。
* The combination of data and functions.
* 封裝 (encapsulation)，繼承 (inheritance)，多型 (polymorphism)。

### Functional programming

_Functional programming imposes discipline upon assignment._

* 最近才被採用，但是是最早被發明的典範。
* 由 Alonzo Church 發明於 1936 年。

## Part III: Design Principles

優良的軟體系統來自於無瑕的程式碼 (Good software systems begin with clean code.) ，「SOLID 原則」告訴我們如何建造「堅固的積木 (bricks)」，如何將 functions 和 data 分組規劃成 groupings (書上用 "classes" 稱之，但不是物件導向中類別的意思)，以及這些 groupings 要如何互相連接。

### SRP: The Single Responsibility Principle

An active corollary to Conway's law: The best structure for a software system is heavily influenced by social structure of the organization that uses it to that each softeare module has one, and only one, reason to change.

* A module should have one, and only one, reason to change.
* A module should be responsible to one, and only one, user or stakeholder.
* A module should be responsible to one, and only one, actor.

SRP 是 SOLID 中最多人不明白的原則，大概是名稱造成的誤解。不是指「A function should do one, and only one, thing.」，雖然很常在重構的文章中看到這句話，可是 SRP 不是這個意思。

SRP 是指「A module should be responsible to one, and only one, actor.」，其中 module 指的是 functions 和 data structures 凝聚性的集合，通常是指一個程式碼檔案 (source file)。

凝聚性 (cohesive) 意味著 SRP，也就是說一個程式碼必須對應一個行動者 (actor)。

### OCP: The Open-Closed Principle

Bertrand Meyer 於 1988 年在 Object-Oriented Software Construction 書中寫到： A software artifict should be open for extension but closed for modification.

### LSP: The Liskov Substitution Principle

Barbara Liskov 於 1988 年的 Data Abstraction and Hierarchy 文章中所提出的 subtype 概念。

What is wanted here is something like the following substitution property: If for each object o1 of type S there is an object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2 then S is a subtype of T.

### ISP: The Interface Segregation Principle

This principle advises software designers to avoid depending on things that they don't use.

Depending on something that carries baggage that you don't need can cause tou troubles that you didn't expect.

ISP is a language issue, rather than an architecture issue.

對架構上而言，如果一個系統依賴於一個框架，而這個框架又依賴於一個資料庫，那麼當資料庫變動時，勢必也需要變動依賴於它的框架與系統。更糟的是，如果資料庫發生失效 (failure)，那麼框架與系統也都會失效。

### DIP: The Dependency Inversion Principle

The code that implements high-level policy should not depend on the code that implements low-level details. Rather, details should depend on policies.

## Part IV: Component Principles

Components are the units of deployment. They are the smallest entities that can be deployed as part of a system.

### Component Cohesion

設計上，我們必須決定哪些 classes 要放在一個元件裡 (也就是元件的內聚力)，有下列 3 個原則：

#### REP: The Reuse/Release Equivalence Principle

The granule of reuse is the granule of release.

#### CCP: The Common Closure Principle

Gather into components those classes that change for the same reasons and at the same times. Separate into different components those classes that change at different times and for different reasons.

The CCP is the component form of the SRP.

#### CRP: The Common Reuse Principle

Don't force users of a component to depend on things they don't need.

The CRP is the generic version of the ISP.

### Component Coupling

元件與元件之間的關係如何設計，有下列 3 個原則：

#### ADP: The Acyclic Dependencies Principle

Allow no cycles in the component dependency graph.

#### SDP: The Stable Dependencies Principle

Depend in the direction of stability.

#### SAP: The Stable Abstractions Principle

A component should be as abstract as it is stable.

## Part V: Architecture


## Part VI: Details


## Part VII: Appendix

