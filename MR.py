#Lab 10: WAP to test primality based on Miller Rabin Algorithm.
import random

def miller_rabin(n, k=5):
    """Perform the Miller-Rabin primality test on n using k iterations."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

def main():
    num = int(input("Enter a number to test for primality: "))
    if miller_rabin(num):
        print(f"{num} is probably prime.")
    else:
        print(f"{num} is composite.")

if __name__ == "__main__":
    main()