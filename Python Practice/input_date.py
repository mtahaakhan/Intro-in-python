# ! Here we have imported datetime and timedelta functions from datetime library
from datetime import datetime,timedelta


# ! Here we are receiving input from user, when is your birthday?
birthday = input('When is your birthday (dd/mm/yyyy)? ')

# ! Here we are converting input into birthday_date
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')


# ! Here we are printing birthday date 
print('Birthday: ' + str(birthday_date))


# ! Here we are again just asking one day before from timedelta
one_day = timedelta(days=1)


birthday_eve = birthday_date - one_day

print('Day before birthday: ' + str(birthday_eve))

# ! Now we will see Error Handling if we receive birthday date in spaces or ashes.