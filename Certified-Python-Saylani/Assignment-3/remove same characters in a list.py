list = ['p','y','t','t','h','o','o','n']
i = 0
duplicate_list = []

for x in list:
    if list.index(x) == i:
        duplicate_list += x
    i += 1
print(duplicate_list)        