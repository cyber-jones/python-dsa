def group_anagrams(strs: list[str]) -> list[str]:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    Pattern: Character count as a canonical representation.
    """
    anagrams = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)
    return list(anagrams.values())

"""
Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""

# Test
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Input: strs = {strs1}")
print(f"Output: {group_anagrams(strs1)}")