country = input('Which country are you from ?')

if country.lower() == 'pakistan':
    print('You must like cricket then!')
else:
    print('You are not a Pakistani then')




province = input('What province do you live in: ')
tax = 0

if province == 'Alberta' or province == 'Nunavat':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print('Your tax is: ' + str(tax) + '%')     