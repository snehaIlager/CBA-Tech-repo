def max_len_equal_0s_1s(arr):
    """
    Finds the maximum length subarray with equal number of 0s and 1s.
    Converts 0s to -1s and uses prefix sum + hashmap to track max length.
    """

    # Convert 0s to -1s
    transformed = [-1 if x == 0 else 1 for x in arr]

    prefix_sum = 0
    max_len = 0
    sum_map = {}  # sum : first index

    for i, val in enumerate(transformed):
        prefix_sum += val

        if prefix_sum == 0:
            max_len = i + 1

        if prefix_sum in sum_map:
            max_len = max(max_len, i - sum_map[prefix_sum])
        else:
            sum_map[prefix_sum] = i

    return max_len

# Example usage
arr = [0, 1, 0, 1, 0, 1, 1]
print("Max length of subarray with equal 0s and 1s:", max_len_equal_0s_1s(arr))
