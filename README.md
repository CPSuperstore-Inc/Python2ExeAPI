# Python2ExeAPI
The API For The Online Python To Exe Service

# Usage
In Your Console, Issue The Following Command:
> python Python2ExeAPI.py <JSON_File>
  
<JSON_File> Is The Path To The JSON Config File. This Can Be Absolute, Or Relative.

# Exapmle JSON File
```
{
	"zipName": "tmp",
	"finalName": "Galaxy Wide Domination",
	"includeDirs": ["code"],
	"includeFiles": ["Galaxy Wide Domination.py"],
	"projectPath":  "D:/Programming/Python/GWD",
	"mainScriptName": "Galaxy Wide Domination",
	"dst": "D:/Programming/Python/GWD/build",
	"platform": [1],
	"oneFile": "on",
	"programIcon": "D:/Programming/Python/GWD/rescources/images/window/icon.ico",
	"showConsole": "off",
	"dumpFile": "on",
	"dumpFileEmail": "cpsuperstoreinc@gmail.com",
	"deleteOldBuild": 1,
	"dependencies":	
	{
		"createDirectories": 
		[
			"mods/unused", 
			"texturepacks"
		],
		"copyDirectory": 
		{
			"D:/Programming/Python/GWD/rescources": "rescources",
			"D:/Programming/Python/GWD/game_modifiers": "game_modifiers"
		},
		"copyFile":
		{
			"D:/Programming/Python/GWD/DOCUMENTATION/GWD Mod Language/GWD Mod Language.pdf": "/mods",
			"D:/Programming/Python/GWD/SampleMod.gwd": "/mods",
			"C:/Users/Christopher/Documents/Visual Studio 2010/Projects/ModManager/ModManager/bin/Debug/ModManager.exe": "/",
			"D:/Programming/Python/GWD/modExtractor.exe": "/"
		}
	}
}
```
# The Fields In The JSON File
| Field        | Description           |
| ------------- |:-------------:|
| zipName      | The Name Of The .Zip Folder Which Will Be Created Automaticaly. This Folder Will Contain All Of The Python Files, Which Are Sent To The Conversion Servers To Be Converted To Executable|
| finalName | The Name Of The .Zip Folder That Will Be Returned When The Conversion Has Been Completed |
| includeDirs | This Is A List Of Strings. The Strings Are The Differnet Folders To Include In The Conversion **PLEASE NOTE** Only Code Files Are Needed. Other Assets (ex. Images, Sounts, Etc.) Are Not Needed. If You Are Unsure, Include The Folder Anyways. It Will Be Better To Have Un-Needed Files, Than To Miss A Code File, And The Program Does Not Work |
| includeFiles | This Is The List Of Addidtional Files Which Need To Be Included **PLEASE NOTE** Only Code Files Are Needed. Other Assets (ex. Images, Sounts, Etc.) Are Not Needed. If You Are Unsure, Include The Folder Anyways. It Will Be Better To Have Un-Needed Files, Than To Miss A Code File, And The Program Does Not Work |
| projectPath | This Is The Path To The Directory Which Contains The Main Project File. Any Relative Path Is Assumed To Be Relative To This Folder |
| mainScriptName | This Is The Name Of The Main Python File **PLEASE NOTE** This MUST Be A .py File, And Not .pyc, .pyw, Or Any Other Type. **PLEASE NOTE** DO NOT END THE NAME WITH .py. It Is Implied |
| dst | This Is The Folder Where The Build Will Be Placed On Conversion Completion. The Conversion Will Be Returned As A .zip File Named `finalName` |
