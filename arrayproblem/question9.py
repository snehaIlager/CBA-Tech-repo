import math

def inplace_merge(arr1, arr2):
    """
    Merges two sorted arrays in-place using the Gap method.
    Result: arr1 and arr2 contain the merged sorted values.
    """
    n = len(arr1)
    m = len(arr2)
    gap = math.ceil((n + m) / 2)

    def next_gap(gap):
        if gap <= 1:
            return 0
        return math.ceil(gap / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < n + m:
            # Get values at index i and j
            if j < n:
                a, b = arr1[i], arr1[j]
            elif i < n <= j:
                a, b = arr1[i], arr2[j - n]
            else:
                a, b = arr2[i - n], arr2[j - n]

            # Swap if needed
            if a > b:
                if j < n:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < n:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                else:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

            i += 1
            j += 1

        gap = next_gap(gap)

# Example usage
arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]
inplace_merge(arr1, arr2)

print("Merged arr1:", arr1)
print("Merged arr2:", arr2)
