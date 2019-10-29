# province = input('What province do you live in: ')
# tax = 0


# 1st way of doing it
# if province.lower() == 'alberta':
#     tax = 0.05
# elif province.lower() == 'nunavat':
#     tax = 0.05
# elif province.lower() == 'ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print('Your tax is: ' + str(tax) + '%')    
# 
# 
# 2nd way of doing it

# province = input('What province do you live in: ')
# tax = 0

# if province == 'Alberta' or province == 'Nunavat':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print('Your tax is: ' + str(tax) + '%') 
# 
# 
# 3rd way of doing it using IN Operator
# 
# 
# province = input('What province do you live in: ')
# tax = 0

# if province in('Alberta','Nunavat','Ontario','Yukon'):
#     tax = 0.05
# else:
#     tax = 0.15
# print('Your tax is: ' + str(tax) + '%')                 