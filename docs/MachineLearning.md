# 機器學習 (Machine Learning)

機器學習有許多不同的形式，名稱也不相同，例如：樣式辨識 (pattern recognition) 、統計模式 (statistical modeling) 、資料探勘 (data mining) 、知識發現 (knowledge discovery) 、預測分析 (predictive analytics) 、資料科學自我調適系統 (adaptive systems) 、自我組織系統 (self-organizing systems) 等，這些都是機器學習的範疇。就技術面上來說，機器學習是人工智慧 (Artificial Intelligence, AI) 的一個分支領域。

演算法 (algorithm) 是一連串的指令告訴電腦該做什麼，必須是定義精確且毫不含糊的。如果你不能用演算法表達一件事理，就表示你可能還不明白這件事。科學家制定理論，工程師製造設備，電腦科學家提出演算法，而演算法正是串接方法論和機器兩者的共同展現。

傳統的方法我們是定義演算法，輸入數據資料產生輸出結果，但機器學習扭轉這種模式。機器學習會將一個演算法轉變成另一個演算法，結果是輸出一個演算法。機器學習需要大量的數據資料，機器才能學習到越多。機器學習能降低程式設計的複雜性，我們可以把機器學習看做是軟體程式的反組譯。

機器學習演算法稱為「學習器 (learners)」，是一種演算法。學習器在資訊處理生態系統中像是「食肉動物」，把大量的數據資料「吃」進來產生演算法。相對的草食動物則像是資料庫 (databases) 、資訊採集器 (crawlers) 、分析索引器 (indexers) 等。

過去電腦科學是確定性 (deterministically) 的思維，但機器學習則是需要統計的思維。意味著機器學習的結果不是萬無一失，但可能是在可以做到的範圍內是最好的，好到足以讓人滿意。工業革命是自動化人工的作業，資訊革命則是自動化腦力工作的作業，而機器學習則是「自動化機器」本身的新形態發展。

在機器學習領域，只要你給它足夠數量的適當資料進行學習，相同的機器學習演算法卻能夠應用在不同的領域。但問題是「一個學習器能夠做所有的事情嗎？」，足夠的數據資料(如何定義何謂足夠)可能是極為龐大，實際上僅能從有限的資料中學習，因此不同學習器會做出不同假設，這代表每種學習器只能做好某些事情，而不適用於各種情況。

## 介紹

機器學習依據學習方法可以分成 3 類：
* 監督式學習 (supervised learning)
* 非監督式學習 (unsupervised learning)
* 強化學習 (reinforcement learning)

五大學派：
* 符號理論學派
* 類神經網路學派
* 演化論學派
* 貝氏定理學派
* 類比推論學派

## 演算法

* 單純貝氏 (naïve Bayes)
* 類神經網路 (neural networks)

### 監督式學習

* 線性回歸 (linear regression)
* 決策樹 (desion trees)
* 支援向量機 (support vector machines, SVM)

### 非監督式學習

* K-means 分群 (clustering)

### 強化學習

* 交叉熵 (cross-entropy)

## 程式庫

* [scikit-learn](http://scikit-learn.org/)

## 參考資料

* Valentino Zocca 等著，劉立民、吳建華、陳開煇譯，Python 深度學習，新北市：博碩文化，2017。
* 佩德羅‧多明戈斯 (Pedro Domingos) 著，張正苓、胡玉城譯，大演算：機器學習的終極演算法將如何改變我們的未來，創造新紀元的文明？，台北市：三采文化，2016。譯自：The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World
