def contains_duplicate(nums) -> bool:
    """
    Given an array of integers nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

    Pattern: Set membership. Detect whether any value appears twice.
    """
    return len(nums) != len(set(nums))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Test
nums1 = [1, 2, 3, 1]
print(f"Input: nums = {nums1}")
print(f"Output: {contains_duplicate(nums1)}")

nums2 = ["apple", "banana", "cherry", "apple"]
print(f"Input: nums = {nums2}")
print(f"Output: {contains_duplicate(nums2)}")