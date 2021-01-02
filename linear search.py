

def linear_search(arr,length,item):
    for i in range(0,length):
        if arr[i]==item:
            return i
    return -1



def linear_occurrence(arr,length,item):
    counter = 0
    for i in range(0,length):
        if arr[i] == item:
            counter += 1
        else:
            continue
    return counter

def linear_occurrencewithindex(arr,length,item):
    occurencelist = []
    for i in range(0,length):
        if arr[i] == item:
            occurencelist.append(str(i))
        else:
            pass
    return occurencelist



arr = [10,25,8,20,40,15,25,10,7,10]
item = int(input('Enter the number to search: '))
length = len(arr)



indexofitem = linear_search(arr,length,item)

if indexofitem == -1:
    print("Item Not Found")
else:
    print("Value was found in {}".format(indexofitem))


item_occurrence = linear_occurrence(arr,length,item)

if item_occurrence == 0:
    print("item not found")
else:
    print("item was found {} times".format(item_occurrence))


item_occurrence_with_index = linear_occurrencewithindex(arr,length,item)

if len(item_occurrence_with_index) == 0:
    print("item not found")
else:
    indexes = ' '.join(item_occurrence_with_index)
    print("{} this item is found in {} indexes total {} times".format(item,indexes,len(item_occurrence_with_index)))