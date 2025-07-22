def sort_binary_array(arr):
    zero_count = arr.count(0)
    one_count = len(arr) - zero_count

    # Rebuild array: all 0s first, then 1s
    sorted_arr = [0] * zero_count + [1] * one_count
    return sorted_arr

# Example
arr = [1, 0, 1, 1, 0, 0, 1]
print("Sorted binary array:", sort_binary_array(arr))
