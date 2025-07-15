def binary_search(arr, searchnumber):
    low = 0
    highest = len(arr) - 1

    while low <= highest:
        mid = (low + highest)
        if arr[mid] == searchnumber:
            return mid
        elif arr[mid] < searchnumber:
            low = mid + 1
        else:
            highest = mid - 1
            return -1
        
arr = [1,2,3,4,5,6,7,8]
print("index of",binary_search(arr,2))
