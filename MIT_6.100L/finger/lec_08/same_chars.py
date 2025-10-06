"""
s1 and s2 are strings
Returns boolean True is a character in s1 is also in s2, and vice 
versa. If a character only exists in one of s1 or s2, returns False.
"""


def same_chars(s1, s2):
    """
    Returns True if s1 and s2 contain exactly the same set of characters,
    regardless of order or frequency.

    Parameters:
        s1 (str): First input string.
        s2 (str): Second input string.

    Returns:
        bool: True if set(s1) == set(s2), False otherwise.

    Time Complexity:
        O(n + m) — where n = len(s1), m = len(s2). Building sets is linear.

    Space Complexity:
        O(k) — where k is the number of unique characters (≤ 26 for lowercase).

    Auxiliary Space:
        O(k) — two sets stored in memory.

    Optimization Grade Insight:
        - Uses set comparison for constant-time equality check.
        - Ignores frequency — focuses purely on character presence.
        - Ideal for character-based identity checks, hashing, or token normalization.

    Example:
        >>> same_chars("abc", "cab")
        True
        >>> same_chars("abc", "def")
        False
    """
    return set(s1) == set(s2)


# Examples:
print(same_chars("abc", "cab"))       # ✅ True
print(same_chars("abccc", "caaab"))   # ✅ True
print(same_chars("abc", "abd"))         # ❌ False
print(same_chars("abcd", "cabaa"))    # ❌ False
print(same_chars("abcabc", "cabz"))   # ❌ False
print(same_chars("abc", "def"))       # ❌ False
