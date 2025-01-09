# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/description/

def nth_catalan(n):
    """
    Calculate the nth Catalan number using the most efficient method.
    Uses dynamic programming with space optimization and handles potential overflow.

    Args:
        n (int): The index of the Catalan number to calculate (n >= 0)
    Returns:
        int: The nth Catalan number
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    # Handle base cases
    if n <= 1:
        return 1

    # Use single variable instead of array to optimize space
    catalan = 1

    # Calculate using optimized multiplicative formula
    # C(n) = C(n-1) * 2(2n-1)/(n+1)
    for i in range(n):
        catalan = catalan * 2 * (2 * i + 1) // (i + 2)

    return catalan


def test_catalan():
    """Test function to verify correctness for first few Catalan numbers"""
    expected = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
    for i, exp in enumerate(expected):
        result = nth_catalan(i)
        assert result == exp, f"Failed for n={i}: expected {exp}, got {result}"
    print("All tests passed!")


# Example usage
if __name__ == "__main__":
    test_catalan()
    # Calculate some larger values
    print(f"C(15) = {nth_catalan(15)}")  # 9,694,845
    print(f"C(20) = {nth_catalan(20)}")  # 6,564,120,420
