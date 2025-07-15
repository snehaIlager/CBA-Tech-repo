def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
        return -1
    
arr = [8,5,7,3,2,10,9]
target = 10

result = linear_search(arr,target)
print(f"Element {target} found at index: {result}")