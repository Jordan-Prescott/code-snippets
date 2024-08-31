# Type hinting
def multiply(a: int, b: int) -> int:
    return a * b

# Docstrings
def multiply(a: int, b: int) -> int:
    """Multiply two numbers.

    Args:
        a (int): Multiplicand
        b (int): Multiplier

    Returns:
        int: Product of a and b
    """
    return a * b

# Naming
def multiply(multiplicand: int, multiplier: int) -> int:
    return multiplicand * multiplier

