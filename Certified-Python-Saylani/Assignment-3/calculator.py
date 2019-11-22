val1 = int(input('Enter first value: '))
val2 = int(input('Enter second value: '))
operator = input('Enter operator: ')

if operator == '+':
    val = val1 + val2
    print('Answer is: ', val)
elif operator == '-':
    val = val1 - val2
    print('Answer is: ', val)
elif operator == '*':
    val = val1 * val2
    print('Answer is: ', val)
elif operator == '/':
    val = val1 / val2
    print('Answer is: ', val)
elif operator == '**':
    val = val1 ** val2
    print('Answer is: ', val)    
else:
    print('Enter Correct Operator')            