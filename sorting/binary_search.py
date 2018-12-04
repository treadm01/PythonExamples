def binary_search(arr, find):
    middle = len(arr) // 2
    if find == arr[middle]:
        return True
    elif len(arr) == 1:
        return False
    elif find > arr[middle]:
        return binary_search(arr[middle:], find)
    else:
        return binary_search(arr[:middle], find)

if __name__ == '__main__':
    print(binary_search([1,2,3,5,8], 6))
    print(binary_search([5], 5))
