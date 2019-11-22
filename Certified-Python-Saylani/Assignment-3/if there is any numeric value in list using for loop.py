list=['tahaa','usman','ali',3,10,1,12.6,5.9]
for i in list:
    if type(i) == int:
        print(i,'is a numeric value in list')
    elif type(i) == float: 
        print(i,'is a numeric value in list')
    else:
        print(i,'This is not a numeric value')    