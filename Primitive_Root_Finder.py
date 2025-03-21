#Lab 12: WAP to find primitive root of any given number.
import math

def euler_totient(n):
    """Computes Euler's Totient function φ(n)."""
    result = n
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result

def get_factors(n):
    """Returns all prime factors of a number."""
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors

def is_primitive_root(g, n):
    """Checks if g is a primitive root of n."""
    phi_n = euler_totient(n)
    factors = get_factors(phi_n)
    
    for factor in factors:
        if pow(g, phi_n // factor, n) == 1:
            return False
    return True

def find_primitive_root(n):
    """Finds the smallest primitive root of n."""
    phi_n = euler_totient(n)
    
    for g in range(2, n):
        if is_primitive_root(g, n):
            return g
    return -1  # No primitive root found

def main():
    n = int(input("Enter a number to find its primitive root: "))
    primitive_root = find_primitive_root(n)
    if primitive_root != -1:
        print(f"The smallest primitive root of {n} is {primitive_root}.")
    else:
        print(f"No primitive root found for {n}.")

if __name__ == "__main__":
    main()
