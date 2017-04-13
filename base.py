arr=[["first","secon33","thirth6666","fourth666","fifth6666"],
     ["22222","222","333","11","444"],
     ["1123","1231","1231","12","231231"],
     ["123","123","123","1231","1231"],
     ["1231","125555555555555555531","12312","12312","12312"],
    ]
arr1=[]
arr2=[]
for x in range(len(arr[0])):
    print('')
    print(max([arr[y][x] for y in range(len(arr))]))
    arr2.append(len(max([arr[y][x] for y in range(len(arr))])))

print (arr2)

