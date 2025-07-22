#Check if subarray wit 0 sum is exists or not
def has_zero_sum_subarray(arr):
    prefix_sum = 0
    seen_sums = set()

    for num in arr:
     prefix_sum += num

     if prefix_sum == 0 or prefix_sum in seen_sums or num == 0:
        return True
     
     seen_sums.add(prefix_sum)

    return False