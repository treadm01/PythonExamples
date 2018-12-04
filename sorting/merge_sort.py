from random import randint
from time import time

def merge(arr, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        a = arr[:middle]
        b = arr[middle:]
        merge_sort(a)
        merge_sort(b)
        return merge(arr, a, b)
        
if __name__ == '__main__':
    lst = []
    for i in range(30):
        lst.append(randint(0,1000))
    start_time = time()
    print(merge_sort(lst))
    end_time = time()
    print("Elapsed time: %.8f seconds" % (end_time - start_time))

    
    
    
