# Here we are asking datetime library to import datetime function in our code :)
from datetime import datetime, timedelta

# Now the datetime.now() will return current date and time as a datetime object
today = datetime.now()

# We have done this in last example.
print('Today is: ' + str(today))


# Now we will use timedelta 

# Here, from timedelta we are getting yesterdays date time
one_day = timedelta(days=1)
yesterday = today - one_day

print('Yesterday was: ' + str(yesterday))

# Here, from timedelta we are getting last weeks date time
one_week = timedelta(weeks=1)
last_week = today - one_week

print('Last week was: ' + str(last_week))
