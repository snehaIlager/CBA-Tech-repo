def find_duplicate(nums):
    """
    Uses Floyd's Tortoise and Hare (Cycle Detection) algorithm
    to find the duplicate number in the array.
    Assumes: 
      - Array has n+1 integers with values from 1 to n.
      - Only one duplicate exists but may be repeated.
    """

    # Step 1: Find the intersection point in the cycle
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Step 2: Find the entrance to the cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example usage
arr = [1, 3, 4, 2, 2]
print("Duplicate element is:", find_duplicate(arr))
