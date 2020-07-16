@echo off
rem This program use MSBuild to build WiX Toolset.
rem It requires .NET Framework 3.5 SP1, Visual Studio 2015 and administrator privileges.
rem Reference: http://wixtoolset.org/development/building-wix/

set MSBuild="C:\Program Files (x86)\MSBuild\14.0\Bin\MSBuild.exe"
git clone https://github.com/wixtoolset/wix3.git
cd wix3
git checkout wix3103rtm
tools\bin\NuGet.exe update -self

%MSBuild% tools\OneTimeWixBuildInitialization.proj
%MSBuild%