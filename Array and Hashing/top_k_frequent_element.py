def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Given an array of integers nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Pattern: Frequency counting + Bucket sort.
    """
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in counts.items():
        buckets[count].append(num)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Test
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(f"Input: nums = {nums1}, k = {k1}")
print(f"Output: {top_k_frequent(nums1, k1)}")

nums2 = [1]
k2 = 1
print(f"Input: nums = {nums2}, k = {k2}")
print(f"Output: {top_k_frequent(nums2, k2)}")