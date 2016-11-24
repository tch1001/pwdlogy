import os;
import warnings

print("\n\n");
print("======================================================");
print(" ___             _  _                  ");
print("| _ \__ __ __ __| || | ___  __ _  _  _  ");
print("|  _/\ V  V // _` || |/ _ \/ _` || || |");
print("|_|   \_/\_/ \__,_||_|\___/\__, | \_, |");
print("                           |___/  |__/ ");
# 	print(".______   ____    __    ____  _______   __        ______     ___________    ____");
# 	print("|   _  \  \   \  /  \  /   / |       \ |  |      /  __  \   /  _____\   \  /   /");
# 	print("|  |_)  |  \   \/    \/   /  |  .--.  ||  |     |  |  |  | |  |  __  \   \/   / ");
# 	print("|   ___/    \            /   |  |  |  ||  |     |  |  |  | |  | |_ |  \_    _/  ");
# 	print("|  |         \    /\    /    |  '--'  ||  `----.|  `--'  | |  |__| |    |  |    ");
# 	print("| _|          \__/  \__/     |_______/ |_______| \______/   \______|    |__|    ");
print("======================================================");
print("\n\n");
print("Disclaimer: ")
print("Please do not use in military or secret service organizations, or for illegal purposes.");
print("The tool here is only used for educational purposes only.");
print("I will not be held responsible for any illegal activities conducted with this.");
print("Enjoy! :D\n\n");



fastMode = False
useCommon = True
useBirthday = True
useLeet = True
showAttempts = True
genDictName = "gen.txt"
keywordsFileName = "keywords.txt"
formatsFileName = "formats_default.conf"
birthdayFileName = "birthday.txt"
defaultSettingsFileName = "settings_default.conf"
commonFile = "commonPhrases.txt"
birthday = ''
birthdayList = []
	

specialCharList = ["!","?","@","*","$","#"]
numList = ['0','1','2','3','4','5','6','7','8','9']
characterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

keywordsList = []

commonFile = "commonPhrases.txt"

leetReplacements = [
('a','4'),
('e','3'),
('o','0')
]

writeFile = open(genDictName, 'w');
keywordsFile = open(keywordsFileName, 'r');
formatsFile = open(formatsFileName, 'r');


def leet(raw):
	for old,new in leetReplacements:
		raw = raw.replace(old,new)
	
	return raw


def attempt(word):
	if showAttempts:
		print("Attempting '"+word+"'");
	writeFile.write(word+"\n");	
	if(useLeet):
		leeted = leet(word)
		if leeted == word: 
			return;
		elif showAttempts:
			print("Attempting '"+leeted+"'");
		writeFile.write(leeted+"\n");

	
def originalWords(pwdFormat,prefix, index):
	if(index>=len(pwdFormat)):
		attempt(prefix);
		return;
	elif(pwdFormat[index] == '_'):
		originalWords(pwdFormat, prefix+"_", index+1);
	elif(pwdFormat[index] == 'k'):
		for word in keywordsList:
			originalWords(pwdFormat,prefix+word,index+1);
	elif(pwdFormat[index] == 'K'):
		for word in keywordsList:
			originalWords(pwdFormat,prefix+word.title(),index+1);
	elif(pwdFormat[index] == 'a'):
		for word in keywordsList:
			originalWords(pwdFormat,prefix+alternateWord(word,0),index+1);
			originalWords(pwdFormat,prefix+alternateWord(word,1),index+1);
	elif(pwdFormat[index] == 'b'):
		for birthday in birthdayList:
			for dates in birthday:
				originalWords(pwdFormat,prefix+dates,index+1);
	elif(pwdFormat[index] == 'B'):
		birthdayComplex(pwdFormat,prefix,index+1);
	elif(pwdFormat[index] == 's'):
		for specialChar in specialCharList:
			originalWords(pwdFormat,prefix+specialChar,index+1);
	elif(pwdFormat[index] == 'n'):
		for number in numList:
			originalWords(pwdFormat,prefix+number,index+1);
	elif(pwdFormat[index] == 'r'):
		for word in keywordsList:
			originalWords(pwdFormat,prefix+word[::-1],index+1);
	elif(pwdFormat[index] == 'R'):
		for word in keywordsList:
			originalWords(pwdFormat,prefix+word[::-1].title(),index+1);
	elif(pwdFormat[index] == 'c'):
		for character in characterList:
			originalWords(pwdFormat,prefix+character,index+1);
	elif(pwdFormat[index] == 'C'):
		for character in characterList:
			originalWords(pwdFormat,prefix+character.title(),index+1);

				

def birthdayComplex(pwdFormat,prefix, index):
	for wholeBirthday in birthdayList:
		for birthday in wholeBirthday:
			originalWords(pwdFormat,prefix+birthday, index+1);
		for birthday in wholeBirthday:
			for birthday2 in wholeBirthday:
				originalWords(pwdFormat,prefix+birthday+birthday2, index+1);
		for birthday in wholeBirthday:
			for birthday2 in wholeBirthday:
				for birthday3 in wholeBirthday:
					originalWords(pwdFormat,prefix+birthday+birthday2+birthday3,index+1);
		for birthday in wholeBirthday:
			for birthday2 in wholeBirthday:
				for birthday3 in wholeBirthday:
					for birthday4 in wholeBirthday:
						originalWords(pwdFormat,prefix+birthday+birthday2+birthday3+birthday4, index+1);
def alternateWord(word, cap):
	index = 0;
	temp = "";
	for character in word:
		if index%2==cap:
			temp+=character.upper()
		else:
			temp+=character.lower()
		index+=1;
	return temp;


def includeCommon():
	for line in open(commonFile, 'r'):
		keywordsList.append(line.replace("\n",""));		
if(useCommon=='y'):
	includeCommon()

def removeDuplicates(l):
	cleanlist = []
	[cleanlist.append(x) for x in l if x not in cleanlist]
	return cleanlist
#====================================================
def help():
	print("");
	print("Commands:");
	print("set             -- change settings");
	print("start           -- generate wordlist");
	print("settings        -- display current settings");
	print("save            -- save current settings");
	print("load            -- load settings from file");
	print("functions       -- display available functions");
	print("help            -- display help menu");
	print("credits         -- display credits");
	print("custom          -- custom parameters");
	print("exit/quit       -- exit console");
	print("");
	
def start():
	for line in keywordsFile:
		line = line.replace("\n","");
		if(line.replace(" ","").replace("	","") == ''):
			continue
		if(line[0] == "#"):
			continue
		keywordsList.append(line);
	
	if(useCommon):
		includeCommon()
	if(useBirthday):
		birthdayFile = open(birthdayFileName, 'r');
		global birthdayList
		for birthday in birthdayFile:
			birthday = birthday.replace("\n","");	
			if(birthday.replace(" ","").replace("	","") == ''):
				continue
			if birthday[0] == '#':
				continue
			tempList = []
			tempList.append(birthday[0:2])
			tempList.append(birthday[2:4])
			tempList.append(birthday[6:8])
			tempList.append(birthday[4:8])
			birthdayList.append(tempList)
		
	for line in formatsFile:
		line = line.replace("\n","");
		if(line.replace(" ","").replace("	","") == ''):
			continue
		if line[0] == '#':
			continue
		elif line == 'fast:break:slow' and fastMode:
			break;
		elif line == 'fast:break:slow':
			continue
		print("");
		global useLeet
		if(line.find('l')!=-1 or line.find('L')!=-1):
			useLeet = True
			print("Generating format ["+line+"]");
			line=line.replace("l","");
			line=line.replace("L","");
			originalWords(line,"",0);
		else:
			useLeet = False
			print("Generating format ["+line+"]");
			originalWords(line,"",0);
	print("=====DONE=====\n\n");
	exit();

def settings(str):
	if(str == 'all'):
		settings('files');
		settings('util');
		settings('fast');
		settings('charsets');
	elif(str == 'files'):
		print("");
		print("---Files---");
		print('Generated Dictionary Name:    '+genDictName);
		print('Keywords File:                '+keywordsFileName);
		print("Common Phrases File:          "+commonFile);
		print("Formats File:                 "+formatsFileName);
		print("Birthdays File:               "+birthdayFileName);
		print("");
	elif(str == 'util'):
		print("");
		print("---Utilities---");
		print("Use Birthay:                        %s" % useBirthday);
		print("Show Attempts:                      %s" % showAttempts);
		print("Include Common Phrases in Keywords: %s" % useCommon);
		print("");
	elif(str == 'fast'):
		print("");
		print("---Fast Mode---");
		print("Fast Mode:       %s" % fastMode);
		print("Fast Mode disables operations that might take long ~ O(n^2)")
		print("When using large a list of keywords, enable Fast Mode\n");
		print("Note: Password list will also contain less passwords");
		print("Tip: Stick to a smaller list of keywords. Don't spam keywords");
		print("");
	elif(str == 'charsets'):
		settings('spchar')
		settings('num')
		settings('char')
		settings('l33t')
	elif(str == 'spchar'):
		print("");
		print("---Special Characters---");
		print("Special Characters Set:");
		print(specialCharList);
		print("");
	elif(str == 'num'):
		print("");
		print("---Numbers---");
		print("Numbers Set:");
		print(numList);
		print("");
	elif(str == 'char'):
		print("");
		print("---Alphabet---");
		print("Character Set:");
		print(characterList);
		print("");
	elif(str == 'l33t'):
		print("");
		print("---L33t---");
		print("L33t Replacements:");
		for leet in leetReplacements:
			print(leet);
		print("");
	elif(str == 'help'):
		print("");
		print("usage: settings <descriptor>");
		print("");
		print("---Descriptors:---");
		print("all             -- all settings");
		print("files           -- I/O file settings");
		print("util            -- utilities settings");
		print("fast            -- fast mode settings");
		print("charsets        -- all sets settings");
		print("spchar          -- special character set settings");
		print("num             -- number set settings");
		print("char            -- character set settings");
		print("l33t            -- l33t set settings");
		print("help            -- display help menu");
		print("");
		
def set(mystr, value):
	if mystr == 'help' and value.replace(" ", "") == '':
		print("\nusage: set <setting> <value>\n");
		print("---Settings---");
		print("genDictName         -- Generated Dictionary File Name");
		print("keywordsFile        -- Keywords File Name");
		print("commonPhrases       -- Common Phrases File Name");
		print("formatsFile         -- Formats File Name");
		print("birthdaysFile        -- Birthdays File Name");
		print("useBirthday         -- Use birthday");
		print("showAttempts        -- display generated words on console");
		print("includeCommon       -- Use common phrases");
		print("fastMode            -- Use Fast Mode");
		print("spchar              -- Special Characters set");
		print("numbers             -- Numbers set");
		print("alphabet            -- Alphabets set");
		print("l33t                -- L33t set");
		print("help                -- display help menu");
		print("");
	elif mystr == 'gendictname':
		mystr = 'genDictName'
		if(value.replace(" ", "") == ''):
			print("\nusage: set genDictName <filename>\n");
		else:
			global genDictName
			genDictName = value
			print("");
			print(mystr + " set to '" + str(genDictName)+"'");
			print("");
	elif mystr == 'keywordsfile':
		mystr = 'keywordsFile'
		if(value.replace(" ", "") == ''):
			print("\nusage: set keywordsFile <filename>\n");
		else:
			global keywordsFile
			keywordsFile = value
			print("");
			print(mystr + " set to '" + str(keywordsFile)+"'");
			print("");
	elif mystr == 'commonphrases':
		mystr = 'commonPhrases'
		if(value.replace(" ", "") == ''):
			print("\nusage: set commonPhrases <filename>\n");
		else:
			global commonFile
			commonFile = value
			print("");
			print(mystr + " set to '" + str(commonFile)+"'");
			print("");
	elif mystr == 'formatsfile':
		mystr = 'formatsFile'
		if(value.replace(" ", "") == ''):
			print("\nusage: set formatsFile <filename>\n");
		else:
			global formatsFileName
			formatsFileName = value
			print("");
			print(mystr + " set to '" + str(formatsFileName)+"'");
			print("");
	elif mystr == 'birthaysfile':
		mystr = 'birthdaysFile'
		if(value.replace(" ", "") == ''):
			print("\nusage: set commonPhrases <filename>\n");
		else:
			global birthdaysFileName
			birthdaysFileName = value
			print("");
			print(mystr + " set to '" + str(birthdaysFileName)+"'");
			print("");
	elif mystr == 'usebirthday':
		mystr = 'useBirthday'
		if(value.replace(" ", "") == ''):
			print("\nusage: set useBirthday <True/False>\n");
		else:
			global useBirthday
			useBirthday = string2bool(value)
			print("");
			print(mystr + " set to '" + str(useBirthday)+"'");
			print("");
	elif mystr == 'showattempts':
		mystr = 'showAttempts'
		if(value.replace(" ", "") == ''):
			print("\nusage: set showAttempts <True/False>\n");
		else:
			global showAttempts
			showAttempts = string2bool(value)
			print("");
			print(mystr + " set to '" + str(showAttempts)+"'");
			print("");
	elif mystr == 'includecommon':
		mystr = 'includeCommon'
		if(value.replace(" ", "") == ''):
			print("\nusage: set includeCommon <True/False>\n");
		else:
			global useCommon
			useCommon = string2bool(value)
			print("");
			print(mystr + " set to '" + str(useCommon)+"'");
			print("");
	elif mystr == 'fastmode':
		mystr = 'fastMode'
		if(value.replace(" ", "") == ''):
			print("\nusage: set fastMode <True/False>\n");
		else:
			global fastMode
			fastMode = string2bool(value)
			print("");
			print(mystr + " set to '" + str(fastMode)+"'");
			print("");
	elif mystr == 'spchar':
		mystr = 'spchar'
		global specialCharList
		if(value.replace(" ", "") == ''):
			print("\nusage: set spchar <action>\n");
			print("---Actions---");
			print("add        -- add a new entries");
			print("remove     -- remove existing entries");
			print("clear      -- clear all entries\n");
		elif value == 'add':
			stringIn = input("\nValues to add (comma-separated): ")
			vals = stringIn.split(',')
			specialCharList.extend(vals)
			specialCharList = removeDuplicates(specialCharList)
			print("\nAdded entries successfully\n");
		elif value == 'remove':
			stringIn = input("\nValues to remove (comma-separated): ")
			vals = stringIn.split(',')
			print("");
			for item in vals:
				if(item in specialCharList):
					specialCharList.remove(item)
					print("Removed '"+item+"' successfully.");
				else:
					print("'"+item+"' does not exist");
			print("");
		elif value == 'clear':
			specialCharList = []
			print("\nAll entries cleared\n");
	elif mystr == 'numbers':
		global numList
		if(value.replace(" ", "") == ''):
			print("\nusage: set numbers <action>\n");
			print("---Actions---");
			print("add        -- add a new entries");
			print("remove     -- remove existing entries");
			print("clear      -- clear all entries\n");
		elif value == 'add':
			stringIn = input("\nValues to add (comma-separated): ")
			vals = stringIn.split(',')
			numList.extend(vals)
			numList = removeDuplicates(numList)
			print("\nAdded entries successfully\n");
		elif value == 'remove':
			stringIn = input("\nValues to remove (comma-separated): ")
			vals = stringIn.split(',')
			print("");
			for item in vals:
				if(item in numList):
					numList.remove(item)
					print("Removed '"+item+"' successfully.");
				else:
					print("'"+item+"' does not exist");
			print("");
		elif value == 'clear':
			numList = []
			print("\nAll entries cleared\n");
	elif mystr == 'alphabet':
		global characterList
		if(value.replace(" ", "") == ''):
			print("\nusage: set alphabet <action>\n");
			print("---Actions---");
			print("add        -- add a new entries");
			print("remove     -- remove existing entries");
			print("clear      -- clear all entries\n");
		elif value == 'add':
			stringIn = input("\nValues to add (comma-separated): ")
			vals = stringIn.split(',')
			characterList.extend(vals)
			characterList = removeDuplicates(characterList)
			print("\nAdded entries successfully\n");
		elif value == 'remove':
			stringIn = input("\nValues to remove (comma-separated): ")
			vals = stringIn.split(',')
			print("");
			for item in vals:
				if(item in characterList):
					characterList.remove(item)
					print("Removed '"+item+"' successfully.");
				else:
					print("'"+item+"' does not exist");
			print("");
		elif value == 'clear':
			characterList = []
			print("\nAll entries cleared\n");
	elif mystr == 'l33t':
		global leetReplacements
		if(value.replace(" ", "") == ''):
			print("\nusage: set l33t <action>\n");
			print("---Actions---");
			print("add        -- add a new entries");
			print("remove     -- remove existing entries");
			print("clear      -- clear all entries\n");
		elif value == 'add':
			stringIn = input("\nSingle Replacement to Add (comma-separated): ")
			vals = stringIn.split(',')
			leetReplacements.append(tuple(vals))
			leetReplacements = removeDuplicates(leetReplacements)
			print("\nAdded entries successfully\n");
		elif value == 'remove':
			stringIn = input("\nSingle Replacement to remove (comma-separated): ")
			vals = stringIn.split(',')
			print("");
			removed = False
			for old,new in leetReplacements:
				if(old == vals[0] and new == vals[1]):
					print("Removed '"+str(vals)+"' successfully.");
					leetReplacements.remove(tuple(vals))
					removed = True
			if(not removed):
				print(str(vals) + " does not exist");
			print("");
		elif value == 'clear':
			leetReplacements = []
			print("\nAll entries cleared\n");
def save(mystr):
	if(mystr == 'help'):
		print("");
		print("usage: save <filename>\n");
		print("<filename> will be the name of the settings file you want to create\n");
		print("WARNING: THIS MIGHT OVERRIDE ANY EXISTING FILE");
		print("(Choose a filename that does not exist in your directory)");
		print("");
	elif(mystr.replace(' ','') == ''):
		print("");
		print("Filename cannot be empty");
		print("");
	else:	
		saveFile = open(mystr, 'w');
		saveFile.write('fastMode '+str(fastMode)); saveFile.write("\n");
		saveFile.write('useCommon '+str(useCommon)); saveFile.write("\n");
		saveFile.write('useBirthday '+str(useBirthday)); saveFile.write("\n");
		saveFile.write('useLeet '+str(useLeet)); saveFile.write("\n");
		saveFile.write('showAttempts '+str(showAttempts)); saveFile.write("\n");
		saveFile.write('genDictName '+str(genDictName)); saveFile.write("\n");
		saveFile.write('keywordsFileName '+str(keywordsFileName)); saveFile.write("\n");
		saveFile.write('formatsFileName '+str(formatsFileName)); saveFile.write("\n");
		saveFile.write('commonFileName '+str(commonFile)); saveFile.write("\n");
		saveFile.write('specialCharList '); 
		for specialChar in specialCharList:
			saveFile.write(specialChar);
			saveFile.write(' ');
		saveFile.write("\n");
		saveFile.write("numList ");
		for num in numList:
			saveFile.write(num);
			saveFile.write(' '); 
		saveFile.write("\n");
		saveFile.write("characterList ");
		for charac in characterList:
			saveFile.write(charac);
			saveFile.write(' ');
		saveFile.write('\n');
		for old,new in leetReplacements:
			saveFile.write("leetReplacements ");
			saveFile.write(old + " " + new);
			saveFile.write("\n");
def string2bool(mystr):
	return mystr.lower() in ('true');
def load(mystr):
	if(mystr == 'help'):
		print("\nusage: load <filename>\n");
		print("<filename> will be the name of the settings file you want to load\n");
	elif(mystr.replace(' ','') == ''):
		print("");
		print("Filename cannot be empty");
		print("");
	else:
		loadFile = open(mystr, 'r');
		global leetReplacements
		leetReplacements = []
		for line in loadFile:
			line = line.replace("\n", "");
			if(line[0] == '#'):
				continue
			if(line.replace(" ","").replace("	","") == ''):
				continue
			elif line.split()[0] == 'fastMode':
				global fastMode
				if string2bool(line.split()[1]):
					fastMode = True
				else:
					fastMode = False
			elif line.split()[0] == 'useCommon':
				global useCommon
				if string2bool(line.split()[1]):
					useCommon = True
				else:
					useCommon = False
			elif line.split()[0] == 'useBirthday':
				global useBirthday
				if string2bool(line.split()[1]):
					useBirthday = True
				else:
					useBirthday = False
			elif line.split()[0] == 'useLeet':
				global useLeet
				if string2bool(line.split()[1]):
					useLeet = True
				else:
					useLeet = False
			elif line.split()[0] == 'showAttempts':
				global showAttempts
				if string2bool(line.split()[1]):
					showAttempts = True
				else:
					showAttempts = False
			elif line.split()[0] == 'genDictName':
				global genDictName
				genDictName = line.split()[1];
				global writeFile
				writeFile = open(genDictName, 'w');
			elif line.split()[0] == 'keywordsFileName':
				global keywordsFileName
				keywordsFileName = line.split()[1];
				global keywordsFile
				keywordsFile = open(keywordsFileName, 'r');
			elif line.split()[0] == 'formatsFileName':
				global formatsFileName
				formatsFileName = line.split()[1];
				global formatsFile				
				formatsFile = open(formatsFileName, 'r');
			elif line.split()[0] == 'commonFileName':
				global commonFile
				commonFile = line.split()[1];
			elif line.split()[0] == 'specialCharList':
				line = line.split()[1:]
				global specialCharList
				specialCharList = line
			elif line.split()[0] == 'numList':
				line = line.split()[1:]
				global numList
				numList = line
			elif line.split()[0] == 'characterList':
				line = line.split()[1:]
				global characterList
				characterList = line
			elif line.split()[0] == 'leetReplacements':
				line = line.split()[1:]
				leetReplacements.append(tuple(line))

def displayFunction(page):
	counter = 0;
	startPrinting = False
	functionsFile = open('functions.txt','r');
	for line in functionsFile:
		line = line.replace('\n','')
		if line == '++++':
			if not startPrinting:
				counter+=1
				if(counter == page):
					startPrinting = True
					print('');
					continue
			else:
				startPrinting = False
		if(startPrinting):
			print(line)
			
def functions(mystr):
	if(mystr == 'help'):
		print("");
		print("usage: functions <descriptor>");
		print("");
		print("---Descriptors:---");
		print("all             -- description of all functions");
		print("list            -- list all functions");
		print("<function>      -- description of the function");
		print("                   (refer to list to see all functions)");
		print("help            -- display help menu");
		print("");
	elif(mystr == 'list'):
		print("\n'k' for keywords");
		print("'K' for keywords w/ first letter cap");
		print("'a' for alternate cap");
		print("'b' for simple birthday");
		print("'B' for complex birthday");
		print("'s' for special character");
		print("'n' for number");
		print("'r' for reversed keyword");
		print("'R' for reversed keyword w/ first letter cap");
		print("'c' for single letter");
		print("'C' for single capital letter");
		print("'_' for underscore (between strings)");
		print("'l' for l33t (the whole word)\n");
		print("To find out more about each function and their examples,\nuse the following command:");
		print("\nfunctions <function>\n\n");
	elif(mystr == 'help'):
		functions('help')
	elif mystr == 'all':
		functions('k')
		functions('K')
		functions('a')
		functions('b')
		functions('B')
		functions('s')
		functions('n')
		functions('r')
		functions('R')
		functions('c')
		functions('C')
		functions('_')
		functions('l')
	elif mystr == 'k':
		displayFunction(1)
	elif mystr == 'K':
		displayFunction(2)
	elif mystr == 'a':
		displayFunction(3)
	elif mystr == 'b':
		displayFunction(4)
	elif mystr == 'B':
		displayFunction(5)
	elif mystr == 's':
		displayFunction(6)
	elif mystr == 'n':
		displayFunction(7)
	elif mystr == 'r':
		displayFunction(8)
	elif mystr == 'R':
		displayFunction(9)
	elif mystr == 'c':
		displayFunction(10)
	elif mystr == 'C':
		displayFunction(11)
	elif mystr == '_':
		displayFunction(12)
	elif mystr == 'l':
		displayFunction(13)
def credits():
	print("\n\n");
	print("======================================================");
	print(" ___             _  _                  ");
	print("| _ \__ __ __ __| || | ___  __ _  _  _  ");
	print("|  _/\ V  V // _` || |/ _ \/ _` || || |");
	print("|_|   \_/\_/ \__,_||_|\___/\__, | \_, |");
	print("                           |___/  |__/ ");

# 	print(".______   ____    __    ____  _______   __        ______     ___________    ____");
# 	print("|   _  \  \   \  /  \  /   / |       \ |  |      /  __  \   /  _____\   \  /   /");
# 	print("|  |_)  |  \   \/    \/   /  |  .--.  ||  |     |  |  |  | |  |  __  \   \/   / ");
# 	print("|   ___/    \            /   |  |  |  ||  |     |  |  |  | |  | |_ |  \_    _/  ");
# 	print("|  |         \    /\    /    |  '--'  ||  `----.|  `--'  | |  |__| |    |  |    ");
# 	print("| _|          \__/  \__/     |_______/ |_______| \______/   \______|    |__|    ");
	print("======================================================");
	print("Created by: ");
	print(" _       _     __  _____  _____  __  ");
	print("| |     | |   /  ||  _  ||  _  |/  | ");
	print("| |_ ___| |__ `| || |/' || |/' |`| | ");
	print("| __/ __| '_ \ | ||  /| ||  /| | | | ");
	print("| || (__| | | || |\ |_/ /\ |_/ /_| |_");
	print(" \__\___|_| |_\___/\___/  \___/ \___/");
	print("\n\n");
def custom(mystr):
	if mystr=='help':
		print("");
		print("usage: custom <filename>");
		print("\n<filename> will be the name of the file you want to store your custom formats");
		print("The file will contain all the default formats, and is for you to add on the formats you wish to use");
		print("It is recommended that you leave the 'formats_default.conf' file untouched,");
		print("Changing it might result in incomplete formats and will affect the effectiveness of this program");
		print("\nFor more information on adding formats of your own, please visit the README.md or github");
		print("Use the command 'set formatsFile <filename>' to change the formats file for a session");
		
		print("\nWARNING: This will override any existing file.");
		print("");
	else:
		print("\nWARNING: This will override any existing file.");
		customFile = open(mystr,'w');
		customFile.write("#  default formats for password generation"); customFile.write("\n");
		customFile.write("#  This is a custom formats file for you to edit"); customFile.write("\n");
		customFile.write("#             for full effectiveness, please consider adding on"); customFile.write("\n");
		customFile.write("#             instead of replacing the any existing formats"); customFile.write("\n");
		customFile.write("#  ====================================================================="); customFile.write("\n");
		customFile.write("#  To use this list as the formatsFile"); customFile.write("\n");
		customFile.write("#  Use the 'set formatsFile <filename>' to change the formatsFile"); customFile.write("\n");
		customFile.write("#  refer to README.md or github for more details"); customFile.write("\n"); customFile.write("\n");
		customFile.write("k"); customFile.write("\n");
		customFile.write("K"); customFile.write("\n");
		customFile.write("kn"); customFile.write("\n");
		customFile.write("Kn"); customFile.write("\n");
		customFile.write("ks"); customFile.write("\n");
		customFile.write("Ks"); customFile.write("\n");
		customFile.write("knn"); customFile.write("\n");
		customFile.write("Knn"); customFile.write("\n");
		customFile.write("kns"); customFile.write("\n");
		customFile.write("Kns"); customFile.write("\n");
		customFile.write("ksn"); customFile.write("\n");
		customFile.write("Ksn"); customFile.write("\n");
		customFile.write("kss"); customFile.write("\n");
		customFile.write("Kss"); customFile.write("\n");
		customFile.write("knnn"); customFile.write("\n");
		customFile.write("Knnn"); customFile.write("\n");
		customFile.write("knns"); customFile.write("\n");
		customFile.write("Knns"); customFile.write("\n");
		customFile.write("knsn"); customFile.write("\n");
		customFile.write("Knsn"); customFile.write("\n");
		customFile.write("knss"); customFile.write("\n");
		customFile.write("Knss"); customFile.write("\n");
		customFile.write("ksnn"); customFile.write("\n");
		customFile.write("Ksnn"); customFile.write("\n");
		customFile.write("ksns"); customFile.write("\n");
		customFile.write("Ksns"); customFile.write("\n");
		customFile.write("kssn"); customFile.write("\n");
		customFile.write("Kssn"); customFile.write("\n");
		customFile.write("ksss"); customFile.write("\n");
		customFile.write("Ksss"); customFile.write("\n");
		customFile.write("knnns"); customFile.write("\n");
		customFile.write("Knnns"); customFile.write("\n");
		customFile.write("knnss"); customFile.write("\n");
		customFile.write("Knnss"); customFile.write("\n");
		customFile.write("lk"); customFile.write("\n");
		customFile.write("lK"); customFile.write("\n");
		customFile.write("lkn"); customFile.write("\n");
		customFile.write("lKn"); customFile.write("\n");
		customFile.write("lks"); customFile.write("\n");
		customFile.write("lKs"); customFile.write("\n");
		customFile.write("lknn"); customFile.write("\n");
		customFile.write("lKnn"); customFile.write("\n");
		customFile.write("lkns"); customFile.write("\n");
		customFile.write("lKns"); customFile.write("\n");
		customFile.write("lksn"); customFile.write("\n");
		customFile.write("lKsn"); customFile.write("\n");
		customFile.write("lkss"); customFile.write("\n");
		customFile.write("lKss"); customFile.write("\n");
		customFile.write("lknnn"); customFile.write("\n");
		customFile.write("lKnnn"); customFile.write("\n");
		customFile.write("lknns"); customFile.write("\n");
		customFile.write("lKnns"); customFile.write("\n");
		customFile.write("lknsn"); customFile.write("\n");
		customFile.write("lKnsn"); customFile.write("\n");
		customFile.write("lknss"); customFile.write("\n");
		customFile.write("lKnss"); customFile.write("\n");
		customFile.write("lksnn"); customFile.write("\n");
		customFile.write("lKsnn"); customFile.write("\n");
		customFile.write("lksns"); customFile.write("\n");
		customFile.write("lKsns"); customFile.write("\n");
		customFile.write("lkssn"); customFile.write("\n");
		customFile.write("lKssn"); customFile.write("\n");
		customFile.write("lksss"); customFile.write("\n");
		customFile.write("lKsss"); customFile.write("\n");
		customFile.write("lknnns"); customFile.write("\n");
		customFile.write("lKnnns"); customFile.write("\n");
		customFile.write("lknnss"); customFile.write("\n");
		customFile.write("lKnnss"); customFile.write("\n");
		customFile.write("kB "); customFile.write("\n");
		customFile.write("KB"); customFile.write("\n");
		customFile.write("B"); customFile.write("\n");
		customFile.write("r"); customFile.write("\n");
		customFile.write("R"); customFile.write("\n");
		customFile.write("rn"); customFile.write("\n");
		customFile.write("Rn"); customFile.write("\n");
		customFile.write("rnn"); customFile.write("\n");
		customFile.write("Rnn"); customFile.write("\n");
		customFile.write("rns"); customFile.write("\n");
		customFile.write("Rns"); customFile.write("\n");
		customFile.write("rnnn"); customFile.write("\n");
		customFile.write("Rnnn"); customFile.write("\n");
		customFile.write("fast:break:slow"); customFile.write("\n");
		customFile.write("#  This indicates the separation of faster combination from slower combinations"); customFile.write("\n");
		customFile.write("#  Enabling Fast-Mode will cause wordlist generation to stop here"); customFile.write("\n");
		customFile.write("kk"); customFile.write("\n");
		customFile.write("Kk"); customFile.write("\n");
		customFile.write("kkn"); customFile.write("\n");
		customFile.write("Kkn"); customFile.write("\n");
		customFile.write("kks"); customFile.write("\n");
		customFile.write("Kks"); customFile.write("\n");
		customFile.write("kknn"); customFile.write("\n");
		customFile.write("Kknn"); customFile.write("\n");
		customFile.write("kkns"); customFile.write("\n");
		customFile.write("Kkns"); customFile.write("\n");
		customFile.write("kksn"); customFile.write("\n");
		customFile.write("Kksn"); customFile.write("\n");
		customFile.write("kkss"); customFile.write("\n");
		customFile.write("Kkss"); customFile.write("\n");
		customFile.write("kknnn"); customFile.write("\n");
		customFile.write("Kknnn"); customFile.write("\n");
		customFile.write("kknns"); customFile.write("\n");
		customFile.write("Kknns"); customFile.write("\n");
		customFile.write("kknsn"); customFile.write("\n");
		customFile.write("Kknsn"); customFile.write("\n");
		customFile.write("kknss"); customFile.write("\n");
		customFile.write("Kknss"); customFile.write("\n");
		customFile.write("kksnn"); customFile.write("\n");
		customFile.write("Kksnn"); customFile.write("\n");
		customFile.write("kksns"); customFile.write("\n");
		customFile.write("Kksns"); customFile.write("\n");
		customFile.write("kkssn"); customFile.write("\n");
		customFile.write("Kkssn"); customFile.write("\n");
		customFile.write("kksss"); customFile.write("\n");
		customFile.write("Kksss"); customFile.write("\n");
		customFile.write("kknnns"); customFile.write("\n");
		customFile.write("Kknnns"); customFile.write("\n");
		customFile.write("kknnss"); customFile.write("\n");
		customFile.write("Kknnss"); customFile.write("\n");
		customFile.write("lkk"); customFile.write("\n");
		customFile.write("lKk"); customFile.write("\n");
		customFile.write("lkkn"); customFile.write("\n");
		customFile.write("lKkn"); customFile.write("\n");
		customFile.write("lkks"); customFile.write("\n");
		customFile.write("lKks"); customFile.write("\n");
		customFile.write("lkknn"); customFile.write("\n");
		customFile.write("lKknn"); customFile.write("\n");
		customFile.write("lkkns"); customFile.write("\n");
		customFile.write("lKkns"); customFile.write("\n");
		customFile.write("lkksn"); customFile.write("\n");
		customFile.write("lKksn"); customFile.write("\n");
		customFile.write("lkkss"); customFile.write("\n");
		customFile.write("lKkss"); customFile.write("\n");
		customFile.write("lkknnn"); customFile.write("\n");
		customFile.write("lKknnn"); customFile.write("\n");
		customFile.write("lkknns"); customFile.write("\n");
		customFile.write("lKknns"); customFile.write("\n");
		customFile.write("lkknsn"); customFile.write("\n");
		customFile.write("lKknsn"); customFile.write("\n");
		customFile.write("lkknss"); customFile.write("\n");
		customFile.write("lKknss"); customFile.write("\n");
		customFile.write("lkksnn"); customFile.write("\n");
		customFile.write("lKksnn"); customFile.write("\n");
		customFile.write("lkksns"); customFile.write("\n");
		customFile.write("lKksns"); customFile.write("\n");
		customFile.write("lkkssn"); customFile.write("\n");
		customFile.write("lKkssn"); customFile.write("\n");
		customFile.write("lkksss"); customFile.write("\n");
		customFile.write("lKksss"); customFile.write("\n");
		customFile.write("lkknnns"); customFile.write("\n");
		customFile.write("lKknnns"); customFile.write("\n");
		customFile.write("lkknnss"); customFile.write("\n");
		customFile.write("lKknnss"); customFile.write("\n");
		customFile.write("kkB"); customFile.write("\n");
		customFile.write("KkB"); customFile.write("\n");
		customFile.write("lkkB"); customFile.write("\n");
		customFile.write("lKkB"); customFile.write("\n");
		print("\n'"+mystr+"' formats file created successfully.\n")

defaultFile = open('default.conf', 'r')
for line in defaultFile:
	if line[0] == '#':
		continue
	if line.split("=")[0].replace(" ","") == 'settings':
		defaultSettingsFileName = line.split("=")[1].replace(" ","")
	elif line.split("=")[0].replace(" ","") == 'format':
		formatsFileName = line.split("=")[1].replace(" ","")

usrInput = ""
load(defaultSettingsFileName)
while(True):
	usrInput = input("pwdlogy > ").lower()
	if(len(usrInput.split())==1):
		usrInput = usrInput.replace(' ','').replace('	','')
	if(usrInput == '' or usrInput.replace(' ','') == '' or usrInput.replace('	','') == ''):
		pass
	elif(usrInput == 'set'):
		set('help','')
	elif(usrInput == 'start'):
		start()
	elif(usrInput == 'settings'):
		settings("help")
	elif(usrInput == 'save'):
		save('help')
	elif(usrInput == 'load'):
		load('help')
	elif(usrInput.replace(' ','') == 'functions'):
		functions('help')
	elif(usrInput == 'help'):
		help()
	elif(usrInput == 'credits'):
		credits()
	elif(usrInput == 'custom'):
		custom('help')
	elif(usrInput == 'exit' or usrInput == 'quit'):
		exit()
		
	elif(usrInput == 'cd'):
		print("");
		print("Sorry, unable to change directory while program is running");
		print("");
	elif(usrInput.split()[0] == 'clear' or usrInput.split()[0] == 'ls'
		or usrInput.split()[0] == 'pwd' or usrInput.split()[0] == 'whoami' or usrInput.split()[0] == 'cat'
		or usrInput.split()[0] == 'vi' or usrInput.split()[0] == 'cp' or usrInput.split()[0] == 'mv'
		or usrInput.split()[0] == 'rm' or usrInput.split()[0] == 'more' or usrInput.split()[0] == 'man'
		or usrInput.split()[0] == 'find' or usrInput.split()[0] == 'grep' or usrInput.split()[0] == 'rmdir'
		or usrInput.split()[0] == 'mkdir' or usrInput.split()[0] == 'vim' or usrInput.split()[0] == 'nano'):
			os.system(usrInput);
			
	elif(usrInput == 'settings all'):
		settings('all')
	elif(usrInput == 'settings files'):
		settings('files')
	elif(usrInput == 'settings util'):
		settings('util')
	elif(usrInput == 'settings fast'):
		settings('fast')
	elif(usrInput == 'settings charsets'):
		settings('charsets')
	elif(usrInput == 'settings spchar'):
		settings('spchar')
	elif(usrInput == 'settings num'):
		settings('num')
	elif(usrInput == 'settings char'):
		settings('char')
	elif(usrInput == 'settings l33t'):
		settings('l33t')
	elif(usrInput == 'settings help'):
		settings('help')
		
	elif(usrInput.split()[0] == 'functions'):
		functions(usrInput.split()[1])
		
	elif(usrInput.split()[0] == 'save'):
		save(usrInput.split()[1]);
		print("Saved "+usrInput.split()[1]+" successfully.\n");
	elif(usrInput.split()[0] == 'load'):
		load(usrInput.split()[1]);
		print("Loaded "+usrInput.split()[1]+" successfully.\n");
	elif(usrInput.split()[0] == 'custom'):
		custom(usrInput.split()[1]);
	elif(usrInput.split()[0] == 'set' and len(usrInput.split())==2):
		set(usrInput.split()[1], "");
	elif(usrInput.split()[0] == 'set' and len(usrInput.split())==3):
		set(usrInput.split()[1], usrInput.split()[2]);


