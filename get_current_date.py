# Here we are asking datetime library to import datetime function in our code :)
from datetime import datetime


# Now the datetime.now() will return current date and time as a datetime object
current_date = datetime.now()

# First we will convert datetime object to a string
# print('Today is: ' + current_date)

# TypeError: can only concatenate str (not "datetime.datetime") to str

# Before you can concatenate int into string

print('Today is: ' + str(current_date))
