# CKEditor

* [CKEditor](https://ckeditor.com/) 是線上版的所見及所得(What You See Is What You Get, WYSIWYG) 的 HTML 編輯器。
* 作者是 Frederico Caldeira Knabben，最初編輯器的名稱叫做 FCKeditor ，其中 FCK 是作者的縮寫。
* FCKeditor 不是一個太好念的英文名稱 (F?ck editor)，在第三版的時候重新命名為現在的「[CKEditor](https://docs-old.ckeditor.com/FCKeditor_3.x/Design_and_Architecture/Rebranding)」，CK 代表 「Content and Knowledge」。
* 原始碼：[CKEditor Ecosystem · GitHub](https://github.com/ckeditor)

## 文件

* [CKEditor 5 documentation](https://ckeditor.com/docs/ckeditor5/latest/)
* [CKEditor 4 documentation](https://ckeditor.com/docs/ckeditor4/latest/)
* [CKEditor 3.x - CKSource Docs](https://docs-old.ckeditor.com/CKEditor_3.x)

## Note

### CKEditor 選單使用「貼上」功能，出現「Press Ctrl+V to paste. Your browser doesn‘t support pasting with the toolbar button or context menu option.」訊息。

IE 會出現「Do you want to allow this webpage to access your clipboard?」確認視窗，但 Chrome, Firefox 不會顯示確認訊息，而直接出現『 請按下「Ctrl+V」貼上。您的瀏覽器不支援工具列按鈕或是內容功能表選項。』訊息。

這個問題是由於瀏覽器的安全限制，避免 JavaScript 任意存取系統剪貼簿的內容，有安全和隱私的疑慮。
