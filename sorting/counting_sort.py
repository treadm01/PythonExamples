from random import randint
from time import time

def counting_sort(arr):
    k = max(arr)+1 # get the upper bound
    dct = {}
    srt = arr.copy()

    for i in range(k):
            dct[i] = 0
            
    for i in range(len(arr)):
        if arr[i] in dct:
            dct[arr[i]] += 1

    for i in range(k-1):
        dct[i+1] += dct[i]

    for i in range(len(arr)):
        srt[dct[arr[i]]-1] = arr[i]
        dct[arr[i]] -= 1
    return srt

if __name__ == '__main__':
    lst = []
    for i in range(15):
        lst.append(randint(0,1000))
    print(lst)
    print(counting_sort(lst))
