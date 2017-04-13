<<<<<<< HEAD
arr=[["first","secon33","thirth6666","fourth666","fifth6666"],
     ["22222","222","333","11","444"],
     ["1123","1231","1231","12","231231"],
     ["123","123","123","1231","1231"],
     ["1231","125555555555555555531","12312","12312","12312"],
=======
arr=[["first","second","thirth","fourth","fifth"],
     ["22","777777","333","1","444"],
     ["333","1231","1231","12","231231"],
     ["4444","12ffffffffffff3","123","1231","1231"],
     ["5555","1231","12312","12312","12312"],
>>>>>>> 896d011082a8dd4d98b31d7486d1931f78173cda
    ]
arr1=[]

for x in range(len(arr[0])):
    print('')
<<<<<<< HEAD
    print(max([arr[y][x] for y in range(len(arr))]))
    arr2.append(len(max([arr[y][x] for y in range(len(arr))])))

print (arr2)
=======
    arr1.append(max([len(arr[y][x]) for y in range(len(arr))]))
>>>>>>> 896d011082a8dd4d98b31d7486d1931f78173cda

for x in arr:
    print('')
    for i in range(len(x)):
        print(x[i], ' '*(arr1[i]-len(x[i])), end='')
