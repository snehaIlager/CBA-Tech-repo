#Find pair with given sum in the array
def find_pair(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return(complement , num)
        seen.add(num)
    return None

arr = [10 , 5, 2 , 3, -1]
target = 4

result = find_pair(arr,target)
if result:
    print("Pair found:", result)
else:
    print("No pair found")