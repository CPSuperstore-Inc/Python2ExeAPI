# Python2ExeAPI
The API For The Online Python To Exe Service

# Usage
In Your Console, Issue The Following Command:
> python Python2ExeAPI.py <JSON_File>
  
`<JSON_File>` Is The Path To The JSON Config File. This Can Be Absolute, Or Relative.

# Exapmle JSON File 
(This Is The JSON File Used To Create A Build Of Galaxy Wide Domination)
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
| platform | This Is A List Of Platforms To Create The Package For. See Below For The List Of Opersting Systems, And The ID To Use |
| oneFile | Set To `"on"` If The Project Should Be Compiled Down Into A Single Executable, Or `"off"` If It Should Be Compiled Into A Series Of Files |
| programIcon | The Path To THe Program's Icon **PLEASE NOTE** This MUST Be A .ico File. To Convert Image Files To .ico, I Like To Use [X-Icon Editor](http://www.xiconeditor.com/) |
| showConsole | Set To `"on"` If The Project Should Open The Terminbal Window When Run, Or `"off"` If It Should hide the console window (Additional Windows Created By Libraries Like Pygame, CV2, Or TkInter Will Still Show) |
| dumpFile | Set To `"on"` If The Project Should Create A Dump File On A Crash, Or `"off"` If It Should Not Create A Dump File |
| dumpFileEmail | This Is The Email That The Dump File Will Be Sent To On Program Crash. If `dumpFile` Is Set To `off`, Leave This Field As An Empty String |
| deleteOldBuild | Set To `1` If The Project Should Delete The Old Build When It Has Finished Converting If It Exists, Or `0` If It Should Not Overwrite The Build |
| dependencies | This Contains More JSON. See The *Dependency Fields* Table Below, For More Information |

# Platform/Operating System ID Lookup
| ID        | OS           |
| ------------- |:-------------:|
| 1 | Widnows |
| 2 | Ubuntu *(Not Released Yet)* |
| 3 | Mac OSx *(Not Released Yet)* |

# Dependency Fields
| Field        | Description           |
| ------------- |:-------------:|
| createDirectories | This Is The List Of Directories To Copy Over To Create In The Final Build, Relative To The Build Path |
| copyDirectory | This Binds The Absolute Paths Of Directories, To The Relative Path In The Build To Copy To |
| copyFile | This Binds The Absolute Paths Of Files, To The Relative Path In The Build To Copy To |
