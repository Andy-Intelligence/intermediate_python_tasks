

def arrCompare(arr1,arr2):
    if arr1 is None or arr2 is None:
        return print(False)


    if (sorted(arr1) == sorted([i**2 for i in arr2])) or (sorted(arr2) == sorted([i**2 for i in arr1])):
        return print(True)

    return print(False)


arrCompare([1,2,3,4], [1,4,9,16])


num = list(map(lambda i:i*10,[i for i in range(1,6)]))
print(num)