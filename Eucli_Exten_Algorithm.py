#Lab 7: WAP to implement Euclidean and Extended Euclidean algorithm.
def euclidean_gcd(a, b):
    """Function to find GCD using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def extended_euclidean(a, b):
    """Function to find GCD and coefficients x, y using the Extended Euclidean algorithm."""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_euclidean(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y


# Example usage
def get_valid_integer(prompt):
    """Function to safely get a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


a = get_valid_integer("Enter first number: ")
b = get_valid_integer("Enter second number: ")

gcd = euclidean_gcd(a, b)
print(f"GCD of {a} and {b} using Euclidean algorithm: {gcd}")


gcd_ext, x, y = extended_euclidean(a, b)
print(f"GCD of {a} and {b} using Extended Euclidean algorithm: {gcd_ext}")
print(f"Coefficients x and y: {x}, {y} (i.e., {a}*{x} + {b}*{y} = {gcd_ext})")
