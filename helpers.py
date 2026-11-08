"""
CPGE Math & Engineering Utility Tools
A collection of Python functions for basic numerical math and algorithms.
"""

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def matrix_transpose(matrix):
    """Transpose a 2D matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

if __name__ == "__main__":
    print("Fibonacci first 10:", fibonacci(10))
    print("Is 17 prime?:", is_prime(17))
  
