def factorial(n):
    # O(n) time complexity and O(n) space complexity due to recursion
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage
n = 5
print(f"Factorial of {n}: {factorial(n)}")