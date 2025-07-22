def merge_unique(arr1, arr2):
    return sorted(set(arr1 + arr2))

def merge_common(arr1, arr2):
    return sorted(set(arr1).intersection(arr2))

def stable_merge(arr1, arr2):
    i = j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

def merge_diff(arr1, arr2):
    return sorted([x for x in arr1 if x not in set(arr2)])

arr1 = [1, 3, 5, 7]
arr2 = [2, 3, 5, 6]

print("Unique merge:", merge_unique(arr1, arr2))
print("Common elements:", merge_common(arr1, arr2))
print("Stable merge:", stable_merge(arr1, arr2))
print("Diff (arr1 - arr2):", merge_diff(arr1, arr2))
