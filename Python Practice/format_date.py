# Here we are asking datetime library to import datetime function in our code :)
from datetime import datetime

# Here we are getting date time object in today variable
today = datetime.now()

# Here we are getting just formats from datetime objects
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))
print('Hour: ' + str(today.hour))
print('Minutes: ' + str(today.minute))
print('Second: ' + str(today.second))


