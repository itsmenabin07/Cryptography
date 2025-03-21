#Lab 9: WAP to find additive inverse and multiplicative inverse.
import math

def additive_inverse(a, m):
    """Finds the additive inverse of a modulo m."""
    return (-a) % m

def multiplicative_inverse(a, m):
    """Finds the multiplicative inverse of a modulo m using Extended Euclidean Algorithm."""
    if math.gcd(a, m) != 1:
        return None  # No inverse exists if gcd(a, m) != 1
    
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def main():
    a = int(input("Enter a number: "))
    m = int(input("Enter modulus: "))
    
    add_inv = additive_inverse(a, m)
    print(f"Additive Inverse of {a} mod {m} is: {add_inv}")
    
    mul_inv = multiplicative_inverse(a, m)
    if mul_inv:
        print(f"Multiplicative Inverse of {a} mod {m} is: {mul_inv}")
    else:
        print(f"Multiplicative Inverse does not exist for {a} mod {m}.")

if __name__ == "__main__":
    main()