# capitalize = Converts the first character to upper case
cap = 'muhammad taha khan'
print(cap.capitalize())
# casefold = Converts string into lower case
cas = 'MUHAMMAD TAHA KHAN'
print(cas.casefold())
# center = The center() method will center align the string, using a specified character (space is default) as the fill character.
print(cap.center(50))
# count = Return the number of times the value "apple" appears in the string:
print(cas.count("A")) # A is written 5 times in cas variable

# encode = The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

print(cap.encode())

# endswith() = The endswith() method returns True if the string ends with the specified value, otherwise False.

print(cap.endswith('khan'))

# expandtabs = The expandtabs() method sets the tab size to the specified number of whitespaces.
check_expandtabs = 't\ta\th\ta'
print(check_expandtabs.expandtabs(10))

# find = The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

check_find = 'Hello'
print(check_find.find('l')) # It will print the index number of that character

# Format
# 1st way
check_format = 'For only {price:.2f} rupees!'
print(check_format.format(price = 50))
# 2nd way
check_format1 = 'My name is {name}, I am {age} years old!'.format(name = 'Tahaa', age = '21')
print(check_format1)
# 3rd way
check_format2 = 'My name is {0}, I am {1} years old!'.format('Tahaa', 21)
print(check_format2)
# There is only one difference in index and find. find returns -1 is no value is found and index throws error
index_check = 'HelloElliot1'
print(index_check.index('l',4,11))
# isalnum = isaplhanumeric?
isalnum = index_check.isalnum()
print(isalnum) # It's printing false because i was also giving spaces in between strings. no spaces. only alphanumeric

full_name = 'MuhammadTahaKhan'
full_name = full_name.isalpha() 
print(full_name) # here also, no spaces. Only alphabets

isdecimal_check = 'Tahaa'
isdecimal_check = isdecimal_check.isdecimal()
print(isdecimal_check)

num = '\u0030'
print(num.isdigit())

identifier = 'Tahaa_'
print(identifier.isidentifier()) 
 # A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

txt = 'Hello Elliot!'
print(txt.islower()) # false, because all is not lowercase

isnumeric = '565534'
print(isnumeric.isnumeric()) # error because these are string methods not int methods.

mrrobot = 'Bonsoir Elliot'
print(mrrobot.isprintable())

spaces = '   '
print(spaces.isspace()) # checks if there are all spaces > True

print(mrrobot.istitle()) # checks if all words starts with capital letters and returns true > True
print(mrrobot.isupper()) # it will return false because all are not uppercase > False

# join
names = ('Taha', 'Usman', 'AbdurRehman', 'Hussain','Maaz')
isjoin = '#'.join(names) 
print(isjoin)

#ljust
mrrobot = mrrobot.ljust(50,"o")
print(mrrobot)

mrrobot = mrrobot.lower() # it converts any case into lowercase

print(mrrobot)



# Remove spaces to the left of the string:

mrrobot = '               bonsoir elliot'
print(mrrobot.lstrip())

# removes spaces to the right of the string

mrrobot = 'bonsoir elliot                  '
print(mrrobot.rstrip())

# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

# The first element contains the part before the specified string.

# The second element contains the specified string.

# The third element contains the part after the string.

mrrobot = ' I use linux'
print(mrrobot.partition('use'))

# If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:

print(mrrobot.replace('use','love'))

# The replace() method replaces a specified phrase with another specified phrase.


# rfind

print(mrrobot.rfind('l')) # both are same, rfind prints -1 if value is not found
print(mrrobot.rindex('l')) # and rindex prints an error

# rjust

print(mrrobot.rjust(50))

# rpartition
print(mrrobot.rpartition('linux'))

# upper 
print(mrrobot.upper())

# rsplit
mrrobot = '          Elliot           '
mrrobot = mrrobot.rstrip()
print('I did five nine', mrrobot,'Our democracy has been hacked')

# split = changes string into list
mrrobot = 'Elliot, Darlene, Angela, MrRobot'
mrrobot = mrrobot.split()
print(mrrobot) 

# splitlines = add different lines into different list values
mrrobot = 'MrRobot was behind five nine \nYou should have stopped it! It was meant to happen'
print(mrrobot.splitlines())

# startswith == it check if the string starts with what has given inside these brackets
print(mrrobot.startswith('MrRobot')) 

# removes all the extra spaces
mrrobot = '                  MrRobot was behind five nine \nYou should have stopped it! It was meant to happen                '
print(mrrobot.strip())

# swapcases = lowercase will be upper and uppercase will be lowercase

print(mrrobot.swapcase())

#title = Make the first letter in each word upper case:
print(mrrobot.title())

# Zfill = Fill the string with zeros until it is 10 characters long:
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

# If the value of the len parameter is less than the length of the string, no filling is done.
mrrobot = 'Elliot'
print(mrrobot.zfill(10))