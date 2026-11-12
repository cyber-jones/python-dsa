def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two
    numbers such that they add up to target.

    Pattern: Hash map for O(1) lookup
    """
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Test
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {two_sum(nums1, target1)}")

nums2 = [3, 2, 4]
target2 = 6
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {two_sum(nums2, target2)}")

nums3 = [3, 3]
target3 = 6
print(f"Input: nums = {nums3}, target = {target3}")
print(f"Output: {two_sum(nums3, target3)}")