from time import time

def Sequential_Search(arr, find):
    index = -1
    found = False
    for i in range(len(arr)):
        if arr[i] == find:
            found = True
            index = i
    return (found, index)


if __name__ == '__main__':
    start_time = time()
    print(Sequential_Search([54, 26, 93, 17, 77, 31, 44, 55, 20], 4))
    end_time = time()
    print("Elapsed time: %.8f seconds" % (end_time - start_time))
