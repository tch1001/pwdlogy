#Pwdlogy - Powerful Target Specific Passwords Profiler

A target specific wordlist generating tool for social engineers and security researchers! You can create wordlists based on keywords about the person's interests, favourite food, games, closed ones' birthday and names, and even combine them with special characters and numbers to create a highly-target-specific wordlist! It is also fully customisable so you can add your own special characters, numbers, keywords, birthdays, create your own settings, and even password formats. Hope you find this tool useful!

Link to Blog: [tch1001.wordpress.com](https://tch1001.wordpress.com/)

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
##How to Use

 1. Find out the victim's name, username, hobbies, sports team, favourite food, and everything you can find out about him that might appear in his/her password
 2. Find out as much as possible about his pets, family, friends (e.g. their name, birthday, and any keyword that might appear in his/her password
 3. Place all the keywords (not the birthdays) into the `keywords.txt` file, with each keyword separated by a next line.
 4. Place all the birthdays into the `birthday.txt` file, with each password being in the format (DDMMYYYY) and separated by a next line.
 5. If you are fairly new to this tool, enter `start` and navigate to the `gen.txt` file (or whatever file if you have changed the settings) to see the generated wordlist. `Go to 8`
 6. If you wish to use custom settings, use the `custom` command and follow the instructions displayed. Edit the custom formats file and when you are done, run the command `start` to begin generating the wordlist.
 7. Check the `gen.txt` file to see the generated wordlist.
 8. The wordlist generated will contain possible passwords of your victim. Use the wordlist with any password cracker. Good luck!
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

###Formats
Pwdlogy makes use of formats specifiers to generate wordlists. For example, we have the following sets of info.

    Birthday = [['01','02','03','2003']] 
    //Format DD,MM,YY,YYY
    Keywords = ['hi','bye']

Then if we have the format as `kk`, we will create this list

    hihi
    hibye
    byehi
    byebye
Note that all of the generated strings have the format
 `<keyword><keyword>`, which is abbreviated as `kk`.
 Another example: If we have the format `kb`, which stands for simple birthday (there is a complex birthday too! Read more about it with the `functions B` command), then the generated wordlist will be
 

    hi01
    hi02
    hi03
    hi2003
    bye01
    bye02
    bye03
    bye2003
Basically, the strings above are all the possibilities of the format `<keyword><simple birthday>`, abbreviated as `kb`.

The default formats which are in-built are

    k
    lk
    K
    lK
    ks
    Ks
    kb
    Kb
    kB 
    KB
    b
    B
    r
    R
    fast:break:slow
    kk
    Kk
    kks
    Kks
    kkss
    Kkss

Note: The `fast:break:slow` is a break in the file to show that the section on the bottom runs slower [`O(n^2)`]. When `fastMode` is enabled, the program will exclude the formats on the bottom.

The list of formats are not proven to be ideal, and please feel free to change it. It is recommended that to do so,

 1. Use the `custom <filename>` command to create a duplicate of the default formats.
 2. In the new file, append formats you believe will be useful.
 3. Run the program with the `python pwdlogy.py` command.
 4. Change the `formatsFile` to your new custom formats file with the `set formatsFile <filename>` command.
 5. Generate the wordlist with the `start` command.
 6. When you rerun the script, `formatsFile` will be back to the default formats file name. In other words, the `set formatsFile <filename>` command only sets the `formatsFile` for that particular session and will not affect the defaults.
 7. To change the defaults, read the section on **changing defaults**.


 
###exit/quit       -- exit console

    usage: exit
    usage: quit

###Changing Defaults
To change defaults (which is not recommended unless you are very sure of what you are doing and have some experience with this tool), follow the steps below:

 1. Go to the `default.conf` file and open it with a text editor of your choice.
 2. You will see the following:
`format = formats_default.conf`
`settings = settings_default.conf`
 3. To change it, simple replace the existing filename with the filename of your own formats or settings file.
 4. E.g.
`format = my_own_format.conf`
`settings = my_own_settings.conf`
 5. Now just rerun the program with `python pwdlogy.py`  and the new settings and formats will be in place!

## 
**Disclaimer:**
**Please do not use in military or secret service organizations, or for illegal purposes. The tool here is only used for educational purposes only. I will not be held responsible for any illegal activities conducted with this. Enjoy!** 
##Dependencies
 - Python


####**Happy Social Engineering and Password Cracking!**


