#Lab 14: WAP to implement Diffie-Hellman algorithm.
import random

def generate_private_key(prime):
    """Generates a private key randomly less than the prime."""
    return random.randint(2, prime - 2)

def compute_public_key(base, private_key, prime):
    """Computes the public key using (base^private_key) % prime."""
    return pow(base, private_key, prime)

def compute_shared_secret(public_key, private_key, prime):
    """Computes the shared secret using (public_key^private_key) % prime."""
    return pow(public_key, private_key, prime)

def main():
    prime = int(input("Enter a prime number (P): "))
    base = int(input("Enter a base (G): "))
    
    # Alice and Bob generate their private keys
    alice_private = generate_private_key(prime)
    bob_private = generate_private_key(prime)
    
    # Compute public keys
    alice_public = compute_public_key(base, alice_private, prime)
    bob_public = compute_public_key(base, bob_private, prime)
    
    print(f"Alice's Private Key: {alice_private}")
    print(f"Bob's Private Key: {bob_private}")
    print(f"Alice's Public Key: {alice_public}")
    print(f"Bob's Public Key: {bob_public}")
    
    # Compute shared secret keys
    alice_shared_secret = compute_shared_secret(bob_public, alice_private, prime)
    bob_shared_secret = compute_shared_secret(alice_public, bob_private, prime)
    
    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")
    
    if alice_shared_secret == bob_shared_secret:
        print("Key Exchange Successful! Shared secret is identical.")
    else:
        print("Key Exchange Failed! Secrets do not match.")

if __name__ == "__main__":
    main()
