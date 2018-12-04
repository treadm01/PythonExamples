# not fully operational

from random import randint
from time import time


def QuickSort(arr, left, right, p):
    if len(arr) > 0: 
        pivot = arr[p]
        edge = len(arr)-1
        
        if p != edge:
            if right == p:
                p += 1
                left = p
                right = edge
         
            elif right >= left:
                while arr[left] < pivot:
                    left += 1

                while arr[right] > pivot:
                    right -= 1

                if right >= left:
                    temp = arr[right]
                    arr[right] = arr[left]
                    arr[left] = temp
            else:
                arr[p] = arr[right]
                arr[right] = pivot
                left = p+1
                right = edge

            QuickSort(arr, left, right, p)
    return arr


if __name__ == '__main__':
    lst = []
    for i in range(15):
        lst.append(randint(0,1000))
    print(lst)
    start_time = time()
    print(QuickSort(lst, 1, len(lst)-1, 0))
    end_time = time()
    print("Elapsed time: %.8f seconds" % (end_time - start_time))
