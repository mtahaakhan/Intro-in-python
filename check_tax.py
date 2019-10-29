# Here i am getting input in price variable and converting it into float value

price = float(input('How much did you pay: '))

# 1st way of doing this
if price >= 1.00:
    tax = 0.70
else:
    tax = 0
print('Your tax is ',tax)        


# 2nd way of doing this
if price >= 1.00:
    tax = 0.70
    print('Your tax is ',tax)
else:
    tax = 0
    print('Your tax is ',tax)
            