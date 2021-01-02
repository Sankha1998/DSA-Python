def selectionsort(arr):
    len_arr = len(arr)
    for i in range(len_arr-1):
        min_index=i
        for j in range(i+1,len_arr):
            if arr[min_index]>arr[j]:
                min_index = j

        arr[i],arr[min_index]  = arr[min_index],arr[i]


arr= [72,50,10,44,8,20,100]

selectionsort(arr)
print(arr)