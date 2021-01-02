def bubblesort(arr):
    n = len(arr)
    for i in range(1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


arr = [2,15,1,11,7,-2,15,12,0]



print('beforesort{}'.format(arr))

print('aftersort{}'.format(bubblesort(arr)))