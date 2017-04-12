arr=[["first","second","thirth","fourth","fifth"],
     ["22","777777","333","1","444"],
     ["333","1231","1231","12","231231"],
     ["4444","12ffffffffffff3","123","1231","1231"],
     ["5555","1231","12312","12312","12312"],
    ]
arr1=[]

for x in range(len(arr[0])):
    print('')
    arr1.append(max([len(arr[y][x]) for y in range(len(arr))]))

for x in arr:
    print('')
    for i in range(len(x)):
        print(x[i], ' '*(arr1[i]-len(x[i])), end='')
