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

## 補充說明

* [PowerShell ISE 執行外部執行檔(.exe) 時出現 RemoteException NativeCommandError - Yowko&#39;s Notes](https://blog.yowko.com/powershell-ise-nativecommanderror/)

