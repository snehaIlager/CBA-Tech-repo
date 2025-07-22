def print_all_subarrays_with_zero_sum(arr):
    from collections import defaultdict

    # Dictionary to store the cumulative sum and indices
    sum_map = defaultdict(list)
    result = []

    # Initialize sum and store sum 0 at index -1
    curr_sum = 0
    sum_map[0].append(-1)

    for i, num in enumerate(arr):
        curr_sum += num

        if curr_sum in sum_map:
            for start_index in sum_map[curr_sum]:
                result.append((start_index + 1, i))

        sum_map[curr_sum].append(i)

    # Print all subarrays
    for start, end in result:
        print(f"Subarray from index {start} to {end}: {arr[start:end+1]}")

# Example usage
arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
print_all_subarrays_with_zero_sum(arr)
