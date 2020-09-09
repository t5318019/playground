# Windows PowerShell

## 介紹

Windows PowerShell (簡稱 PowerShell) 是一種命令列殼層 (shell) 和指令碼語言， PowerShell 採用 cmdlet (讀作 command-let) 的概念，由動詞 (verb) 和名詞 (noun) 組成的指令。PowerShell 設計用來改善命令提示字元 (Command Prompt) 和腳本 (scripting) 環境

* [Getting Started with Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/getting-started/getting-started-with-windows-powershell)
* [Understanding Important Windows PowerShell Concepts](https://docs.microsoft.com/en-us/powershell/scripting/getting-started/fundamental/understanding-important-windows-powershell-concepts)
* [Compatibility Aliases](https://docs.microsoft.com/en-us/powershell/scripting/samples/appendix-1---compatibility-aliases)
* [Microsoft.PowerShell.Core](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core)
* [Microsoft.PowerShell.Management](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management)
* [GitHub - PowerShell/PowerShell: PowerShell for every system!](https://github.com/powershell/powershell)
* [PowerShell Team Blog | Automating the world one-liner at a time…](https://blogs.msdn.microsoft.com/powershell/)



## 使用

* Windows PowerShell Console ，也就是 [PowerShell.exe](https://docs.microsoft.com/en-us/powershell/scripting/core-powershell/console/powershell.exe-command-line-help) 。
* Windows PowerShell Integrated Scripting Environment (簡稱 ISE)，也就是 [powershell_ise.exe](https://docs.microsoft.com/en-us/powershell/scripting/core-powershell/ise/introducing-the-windows-powershell-ise) 。

## 基本命令

* `Get-Help` 顯示說明 (Help)
* `Update-Help` 下載並安裝最新的說明文件，需要以系統管理員身分執行 (Run as administrator) 才能完成
* `Get-Command` 顯示所有已安裝的命令 (command)
* `Get-History` 列出目前 session 所有的命令歷史紀錄
* `Clear-History` 刪除目前 session 所有的命令歷史紀錄

## 觀念

* PowerShell 和其他 Shell 最大的差異是，處理的是物件 (object) 而不是文字 (text)。物件是一種結構化的資訊，因此使用 PowerShell 時，不需要像過去使用文字處理擷取我們需要的資訊。
* PowerShell 是建構在 NET Common Language Runtime (CLR) 之上，因此接收和回傳 .NET 物件。
* PowerShell 設計上有別名 (alias)，預設有相容性別名，讓 Bash 和 cmd.exe 使用者方便學習 PowerShell，例如 cd 就是 Set-Location 的別名。
* PowerShell 會處理 console 的輸入和輸出顯示，cmdlet 的開發者不需要自己處理輸入的引數 (arguments)，也不需要處理輸出的格式。
* PowerShell 的管線 (pipeline) 傳輸的是物件而不是文字。

## 變數

* [About Variables](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_variables)
* PowerShell 的變數用錢幣符號 ($) 開頭，很像 PHP 的樣子。
* 變數不區分大小寫，$A 和 $a 是同一個。(如同 Windows 的風格，像檔名路徑也是不區分大小寫。)
* 變數名稱沒有限制，數字、字母、空白、特殊字元都可以，長度也沒有限制，只要你記得住就可以。
* 如果變數名稱有空白和特殊字元，請用花括號包住變數名稱，像這樣 `${ }` 是一個空白字元的變數名稱。
* 變數不需要宣告就可以使用。
* 變數是鬆散型別 (loosely typed)，可以儲存任何型別的物件。
* 強制變數的型別，用方括號指定型別，像這樣 `[int]$number = 123`，則任何指定給 `$number` 都會轉型為整數。
* 變數的預設值是 `$null` 。
* 刪除變數的值可以使用 `Clear-Variable` cmdlet，或是指定變數為 `$null` 。刪除變數則用 `Remove-Variable` cmdlet。
* 變數分成三種類型：
  * 使用者變數 (User-created variables)：使用者自己建立的變數。
  * 自動變數 (Automatic variables)：由 PowerShell 建立，不能被修改變更。
  * 喜好變數 (Preference variables)：儲存使用者喜好設定，由 PowerShell 建立，使用者可以自己變更。
* 單引號中的變數不會解析取值，雙引號中的變數會解析取值，像 PHP 中的字串那樣。
* 取得目前 session 中的變數，存在於 `Variable:` 磁碟中，用指令列出所有變數與值 `Get-ChildItem Variable:`。 
* 變數的範圍都是在它建立的範圍之中，如果要存取其他範圍，則需要範圍修飾詞 (scope modifier)。

## 補充說明

* [PowerShell ISE 執行外部執行檔(.exe) 時出現 RemoteException NativeCommandError - Yowko&#39;s Notes](https://blog.yowko.com/powershell-ise-nativecommanderror/)

