# Windows PowerShell

## 介紹

Windows PowerShell (簡稱 PowerShell) 是一種命令列殼層 (shell) 和指令碼語言， PowerShell 採用 cmdlet (讀作 command-let) 的概念，由動詞 (verb) 和名詞 (noun) 組成的指令。PowerShell 設計用來改善命令提示字元 (Command Prompt) 和腳本 (scripting) 環境

* [Getting Started with Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/getting-started/getting-started-with-windows-powershell)
* [Understanding Important Windows PowerShell Concepts](https://docs.microsoft.com/en-us/powershell/scripting/getting-started/fundamental/understanding-important-windows-powershell-concepts)
* [Compatibility Aliases](https://docs.microsoft.com/en-us/powershell/scripting/getting-started/cookbooks/appendix-1---compatibility-aliases)
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
