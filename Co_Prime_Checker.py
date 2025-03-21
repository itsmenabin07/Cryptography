#Lab 13: WAP to check if given two numbers are co-prime or not.
import math

def are_coprime(a, b):
    """Checks if two numbers are co-prime (i.e., gcd(a, b) = 1)."""
    return math.gcd(a, b) == 1

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if are_coprime(a, b):
        print(f"{a} and {b} are co-prime.")
    else:
        print(f"{a} and {b} are not co-prime.")

if __name__ == "__main__":
    main()
