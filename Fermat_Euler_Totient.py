#Lab 11: WAP to implement Fermat’s, Euler’s Theorem and Euler’s totient Function.
import math
import random

def fermat_primality_test(n, k=5):
    """Tests primality using Fermat's Little Theorem with k iterations."""
    if n <= 1:
        return False
    if n == 2:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def euler_totient(n):
    """Computes Euler's Totient function (phi(n))."""
    result = n
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result

def euler_theorem(a, n):
    """Verifies Euler’s Theorem: a^phi(n) ≡ 1 (mod n)."""
    phi_n = euler_totient(n)
    return pow(a, phi_n, n) == 1

def main():
    num = int(input("Enter a number for primality test (Fermat's Theorem): "))
    if fermat_primality_test(num):
        print(f"{num} is probably prime.")
    else:
        print(f"{num} is composite.")
    
    num_phi = int(input("Enter a number to compute Euler's Totient Function: "))
    print(f"Euler's Totient Function φ({num_phi}) = {euler_totient(num_phi)}")
    
    a = int(input("Enter base number for Euler's Theorem: "))
    n = int(input("Enter modulus for Euler's Theorem: "))
    if euler_theorem(a, n):
        print(f"Euler's Theorem holds: {a}^φ({n}) ≡ 1 (mod {n})")
    else:
        print(f"Euler's Theorem does NOT hold for {a} mod {n}.")

if __name__ == "__main__":
    main()
