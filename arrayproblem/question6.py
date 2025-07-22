def find_largest_consecutive_subarray(arr):
    """
    Finds the length of the largest subarray with consecutive integers.
    The subarray must be contiguous and contain no duplicates.
    """

    n = len(arr)
    max_len = 0

    for i in range(n):
        min_val = arr[i]
        max_val = arr[i]
        visited = set()
        visited.add(arr[i])

        for j in range(i + 1, n):
            # Duplicate element — break
            if arr[j] in visited:
                break

            visited.add(arr[j])
            min_val = min(min_val, arr[j])
            max_val = max(max_val, arr[j])

            # Check if current subarray forms consecutive sequence
            if max_val - min_val == j - i:
                curr_len = j - i + 1
                max_len = max(max_len, curr_len)

    return max_len

# Example usage
arr = [10, 12, 11, 14, 13, 16, 15]
print("Length of largest subarray with consecutive integers:", find_largest_consecutive_subarray(arr))
