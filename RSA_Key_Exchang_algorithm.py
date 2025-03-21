#Lab-15
# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to get a valid prime number from the user
def get_prime(prompt):
    while True:
        try:
            num = int(input(prompt))
            if is_prime(num):
                return num
            else:
                print("The number entered is not prime. Please enter a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Euclidean Algorithm to find GCD
def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b 
    return a

# Extended Euclidean Algorithm to find modular inverse
def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Function to find modular inverse of a under modulo mod
def multiplicative_inverse(a, mod):
    g, x, _ = extended_euclidean(a, mod)
    if g == 1:
        return x % mod  # Ensure positive inverse
    return None

# RSA Key Generation
def rsa_key_generation():
    # Ask user for two distinct prime numbers
    p = get_prime("Enter a prime number (p): ")
    q = get_prime("Enter another prime number (q, different from p): ")
    
    while p == q:
        print("p and q must be different. Please enter another prime number.")
        q = get_prime("Enter a different prime number (q): ")

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = 3
    while euclidean_gcd(e, phi_n) != 1:
        e += 2

    # Compute the modular inverse of e
    d = multiplicative_inverse(e, phi_n)

    print(f"Chosen primes: p={p}, q={q}")
    return (e, n), (d, n)  # Public key (e, n), Private key (d, n)

# RSA Encryption function
def rsa_encrypt(message, key):
    e, n = key
    return [pow(ord(char), e, n) for char in message]

# RSA Decryption function
def rsa_decrypt(ciphertext, key):
    d, n = key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Generate RSA keys
public_key, private_key = rsa_key_generation()

message = input("Enter a message to encrypt: ")

# Encrypt and decrypt message
encrypted = rsa_encrypt(message, public_key)
decrypted = rsa_decrypt(encrypted, private_key)

# Display results
print(f"\nPublic Key: {public_key}")
print(f"Private Key: {private_key}")
print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")
