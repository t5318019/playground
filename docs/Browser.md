# Browser

瀏覽器 (broser) 是瀏覽網頁 (webpage) 的軟體，瀏覽器更正確的用詞應該是「網頁瀏覽器 (web broser)」。你是使用哪一種網路瀏覽器？這個網站可以顯示：[What Browser? – Google](https://whatbrowser.org/) 或 [瀏覽器巡禮 – Google](http://www.whatbrowser.org/intl/zh-TW/) 。

## How

* [How Browsers Work: Behind the scenes of modern web browsers - HTML5 Rocks](https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/)
* [Inside look at modern web browser (part 1) | Web | Google Developers](https://developers.google.com/web/updates/2018/09/inside-browser-part1)
* [Inside look at modern web browser (part 2) | Web | Google Developers](https://developers.google.com/web/updates/2018/09/inside-browser-part2)
* [Inside look at modern web browser (part 3) | Web | Google Developers](https://developers.google.com/web/updates/2018/09/inside-browser-part3)
* [Inside look at modern web browser (part 4) | Web | Google Developers](https://developers.google.com/web/updates/2018/09/inside-browser-part4)
* [《來做個網路瀏覽器吧！》文章列表 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10197966)
* [How the Puffin Browser Works – Coding Neutrino – Medium](https://medium.com/coding-neutrino-blog/how-the-puffin-browser-works-440c91cece8f)
* [Modern Web 2016 - Servo平行瀏覽器引擎（the Servo Parallel Browser Engine） | iThome](https://www.ithome.com.tw/video/108438)

## Browser Engine

「瀏覽器引擎 (browser engine)」是瀏覽器的主要元件，目的是將 HTML, CSS 與網頁資源轉換成 UI 的畫面，也稱之為「排版引擎 (layout engine)」 或 「繪圖引擎 (rendering engine)」，下列是各廠牌使用的瀏覽器引擎：

* Firefox: [Gecko](https://developer.mozilla.org/en-US/docs/Mozilla/Gecko)，[取得原始碼](https://github.com/mozilla/gecko-dev)
    * 實驗性的平行化引擎：[Servo](https://servo.org/)，[取得原始碼](https://github.com/servo/servo)
* Internet Explorer: Trident, Microsoft Edge: EdgeHTML
* Safari: [WebKit](https://webkit.org/)，[取得原始碼](https://webkit.org/getting-the-code/)：`git clone git://git.webkit.org/WebKit.git WebKit`
* Google Chrome: [Blink](https://www.chromium.org/blink)，屬於 Chromium 專案，[取得原始碼](https://chromium.googlesource.com/chromium/src.git)：`git clone https://chromium.googlesource.com/chromium/src Chromium`

## JavaScript Engine

* Firefox: [SpiderMonkey](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey)
* Microsoft Edge, Internet Explorer: Chakra，[ChakraCore](https://github.com/Microsoft/ChakraCore)
* Safari: Nitro，也就是 [SquirrelFish Extreme](https://webkit.org/blog/214/introducing-squirrelfish-extreme/)
* Google Chrome: [V8](https://v8.dev/)，[取得原始碼](https://chromium.googlesource.com/v8/v8.git)：`git clone https://chromium.googlesource.com/v8/v8 V8`
