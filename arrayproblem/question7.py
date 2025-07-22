def max_len_subarray_with_sum(arr, K):
    """
    Finds the maximum length of a subarray with a given sum K.
    Uses prefix sum and hashmap for optimal performance.
    """

    prefix_sum = 0
    max_len = 0
    sum_map = {}  # Stores: prefix_sum → first index

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If subarray from 0 to i has the required sum
        if prefix_sum == K:
            max_len = i + 1

        # If (prefix_sum - K) is seen before, subarray from that index+1 to i has sum = K
        if (prefix_sum - K) in sum_map:
            max_len = max(max_len, i - sum_map[prefix_sum - K])

        # Store first occurrence of prefix_sum
        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = i

    return max_len

# Example usage
arr = [1, -1, 5, -2, 3]
K = 3
print("Max length subarray with sum", K, ":", max_len_subarray_with_sum(arr, K))
