#Pwdlogy

A victims'-profile-based wordlist generating tool for social engineers and security researchers!

**Disclaimer:**
**Please do not use in military or secret service organizations, or for illegal purposes. The tool here is only used for educational purposes only. I will not be held responsible for any illegal activities conducted with this. Enjoy!** 
##Installation
Pwdlogy is based on the programming language python. As such, Python will need to be installed. 
###Linux/Mac
To start using pwdlogy, change directory into the project folder.

    cd pwdlogy-master

Then use the following command to run the python script

 

    python pwdlogy.py

You will see a console like this

    pwdlogy > 

### Windows
Sorry, pwdlogy currently does not run on windows.

##Commands

###set             -- change settings
The `set` command allows you to change the settings for each list generation session. 

    usage: set <setting> <value>

The available settings include:

#####genDictName         -- Generated Dictionary File Name
#####keywordsFile        -- Keywords File Name
#####commonPhrases       -- Common Phrases File Name
#####formatsFile         -- Formats File Name
#####birthdaysFile        -- Birthdays File Name
#####useBirthday         -- Use birthday
#####showAttempts        -- display generated words on console
#####includeCommon       -- Use common phrases
#####fastMode            -- Use Fast Mode
#####spchar              -- Special Characters set
#####numbers             -- Numbers set
#####alphabet            -- Alphabets set
#####l33t                -- L33t set
#####help                -- display help menu

###start           -- generate wordlist
Calling `start` will cause pwdlogy to begin and the wordlist generated will be in the same directory with the name determined by the variable `genDictName`

###settings        -- display current settings

    usage: settings <descriptor>

Descriptors

#####all             -- all settings
#####files           -- I/O file settings
#####util            -- utilities settings
#####fast            -- fast mode settings
#####charsets        -- all sets settings
#####spchar          -- special character set settings
#####num             -- number set settings
#####char            -- character set settings
#####l33t            -- l33t set settings
#####help            -- display help menu

###save            -- save current settings

    usage: save <filename>

`<filename>`  will be the name of the settings file you want to create

WARNING: This might override any existing file with the same name
(Choose a filename that does not exist in your directory)
###load            -- load settings from file

    usage: load <filename>

`<filename>` will be the name of the settings file you want to load


###functions       -- display available functions

    usage: functions <descriptor>

Descriptors

#####all                         -- description of all functions
#####list            -- list all functions
#####`<function>`      -- description of the function (refer to list to see all functions)
#####help            -- display help menu

###help            -- display help menu
###credits         -- display credits
###custom          -- custom parameters

    usage: custom <filename>

`<filename>` will be the name of the file you want to store your custom formats
The file will contain all the default formats, and is for you to add on the formats you wish to use
It is recommended that you leave the 'formats_default.conf' file untouched,
Changing it might result in incomplete formats and will affect the effectiveness of this program

For more information on adding formats of your own, please visit the README.md or github
Use the command 'set formatsFile <filename>' to change the formats file for a session

WARNING: This will override any existing file.

###exit/quit       -- exit console

    usage: exit
    usage: quit

##Dependencies
 - Python

## 
**Disclaimer:**
**Please do not use in military or secret service organizations, or for illegal purposes. The tool here is only used for educational purposes only. I will not be held responsible for any illegal activities conducted with this. Enjoy!** 
####**Happy Social Engineering and Password Cracking!**

