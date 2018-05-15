# Command-line

記錄 Windows 命令列 (Command-line) 的相關資訊。

* 目前在 Windows 系統上使用命令列請開啟「命令提示字元 (Command Prompt)」程式，也就是 "C:\Windows\System32\cmd.exe" 。
* Windows 系統上的命令是不區分大小寫 (case-insensitive)，而 Linux 系統則是有區分大小寫。
* Windows 系統上命令的參數 (parameter) 以斜線 (slash) 開頭，例如：`time /?`，而 Linux 系統則是以連字號 (hyphen) 開頭，例如：`date --help`。
* 我們可以將這些命令寫在一個副檔名為 .bat 或 .cmd 的檔案中，稱為批次檔 (batch files)，由 cmd.exe 依序執行檔案中的命令。相當於 Linux 中的 .sh 檔案由 Bash 執行。

## 系統命令清單

以下內容是用 cmd.exe (10.0.15063.0 版本) 的 HELP 命令取得。

 1. ASSOC          Displays or modifies file extension associations.
 2. ATTRIB         Displays or changes file attributes.
 3. BREAK          Sets or clears extended CTRL+C checking.
 4. BCDEDIT        Sets properties in boot database to control boot loading.
 5. CACLS          Displays or modifies access control lists (ACLs) of files.
 6. CALL           Calls one batch program from another.
 7. CD             Displays the name of or changes the current directory.
 8. CHCP           Displays or sets the active code page number.
 9. CHDIR          Displays the name of or changes the current directory.
10. CHKDSK         Checks a disk and displays a status report.
11. CHKNTFS        Displays or modifies the checking of disk at boot time.
12. CLS            Clears the screen.
13. CMD            Starts a new instance of the Windows command interpreter.
14. COLOR          Sets the default console foreground and background colors.
15. COMP           Compares the contents of two files or sets of files.
16. COMPACT        Displays or alters the compression of files on NTFS partitions.
17. CONVERT        Converts FAT volumes to NTFS.  You cannot convert the current drive.
18. COPY           Copies one or more files to another location.
19. DATE           Displays or sets the date.
20. DEL            Deletes one or more files.
21. DIR            Displays a list of files and subdirectories in a directory.
22. DISKPART       Displays or configures Disk Partition properties.
23. DOSKEY         Edits command lines, recalls Windows commands, and creates macros.
24. DRIVERQUERY    Displays current device driver status and properties.
25. ECHO           Displays messages, or turns command echoing on or off.
26. ENDLOCAL       Ends localization of environment changes in a batch file.
27. ERASE          Deletes one or more files.
28. EXIT           Quits the CMD.EXE program (command interpreter).
29. FC             Compares two files or sets of files, and displays the differences between them.
30. FIND           Searches for a text string in a file or files.
31. FINDSTR        Searches for strings in files.
32. FOR            Runs a specified command for each file in a set of files.
33. FORMAT         Formats a disk for use with Windows.
34. FSUTIL         Displays or configures the file system properties.
35. FTYPE          Displays or modifies file types used in file extension associations.
36. GOTO           Directs the Windows command interpreter to a labeled line in a batch program.
37. GPRESULT       Displays Group Policy information for machine or user.
38. GRAFTABL       Enables Windows to display an extended character set in graphics mode.
39. HELP           Provides Help information for Windows commands.
40. ICACLS         Display, modify, backup, or restore ACLs for files and directories.
41. IF             Performs conditional processing in batch programs.
42. LABEL          Creates, changes, or deletes the volume label of a disk.
43. MD             Creates a directory.
44. MKDIR          Creates a directory.
45. MKLINK         Creates Symbolic Links and Hard Links
46. MODE           Configures a system device.
47. MORE           Displays output one screen at a time.
48. MOVE           Moves one or more files from one directory to another directory.
49. OPENFILES      Displays files opened by remote users for a file share.
50. PATH           Displays or sets a search path for executable files.
51. PAUSE          Suspends processing of a batch file and displays a message.
52. POPD           Restores the previous value of the current directory saved by PUSHD.
53. PRINT          Prints a text file.
54. PROMPT         Changes the Windows command prompt.
55. PUSHD          Saves the current directory then changes it.
56. RD             Removes a directory.
57. RECOVER        Recovers readable information from a bad or defective disk.
58. REM            Records comments (remarks) in batch files or CONFIG.SYS.
59. REN            Renames a file or files.
60. RENAME         Renames a file or files.
61. REPLACE        Replaces files.
62. RMDIR          Removes a directory.
63. ROBOCOPY       Advanced utility to copy files and directory trees
64. SET            Displays, sets, or removes Windows environment variables.
65. SETLOCAL       Begins localization of environment changes in a batch file.
66. SC             Displays or configures services (background processes).
67. SCHTASKS       Schedules commands and programs to run on a computer.
68. SHIFT          Shifts the position of replaceable parameters in batch files.
69. SHUTDOWN       Allows proper local or remote shutdown of machine.
70. SORT           Sorts input.
71. START          Starts a separate window to run a specified program or command.
72. SUBST          Associates a path with a drive letter.
73. SYSTEMINFO     Displays machine specific properties and configuration.
74. TASKLIST       Displays all currently running tasks including services.
75. TASKKILL       Kill or stop a running process or application.
76. TIME           Displays or sets the system time.
77. TITLE          Sets the window title for a CMD.EXE session.
78. TREE           Graphically displays the directory structure of a drive or path.
79. TYPE           Displays the contents of a text file.
80. VER            Displays the Windows version.
81. VERIFY         Tells Windows whether to verify that your files are written correctly to a disk.
82. VOL            Displays a disk volume label and serial number.
83. XCOPY          Copies files and directory trees.
84. WMIC           Displays WMI information inside interactive command shell.

## 參考資料

* [Command-line reference A-Z | Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb490890(v=technet.10))
* [Windows Commands | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
* [Command-Line Reference | Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc754340(v=ws.11))
* [Windows Batch Scripting - Wikibooks, open books for an open world](https://en.wikibooks.org/wiki/Windows_Batch_Scripting)
