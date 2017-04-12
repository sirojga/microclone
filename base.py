arr=[["first","second","thirth","fourth","fifth"],
     ["22222","222","333","11","444"],
     ["1123","1231","1231","12","231231"],
     ["123","123","123","1231","1231"],
     ["1231","1231","12312","12312","12312"],
    ]
arr1=[]
arr2=[]
for x in range(len(arr[0])):
    print('')
    arr2.append(len(max([arr[y][x] for y in range(len(arr))])))

print (arr2)

