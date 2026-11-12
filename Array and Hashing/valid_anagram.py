def is_anagram(s,t):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Pattern: Frequency counting of each character.
    """
    s_counts = {}
    t_counts = {}

    for char in s:
        s_counts[char] = s_counts.get(char, 0) + 1
    for char in t:
        t_counts[char] = t_counts.get(char, 0) + 1

    return s_counts == t_counts

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Test
s1 = "anagram"
t1 = "nagaram"
print(f"Input: s = {s1}, t = {t1}")
print(f"Output: {is_anagram(s1, t1)}")

s2 = "rat"
t2 = "car"
print(f"Input: s = {s2}, t = {t2}")
print(f"Output: {is_anagram(s2, t2)}")
    