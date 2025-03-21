#Lab 8: WAP to simulate the functioning of S-box and Key Generation.
import random

def generate_key(key_size=16):
    """Generates a random key of given size in bytes."""
    return [random.randint(0, 200) for _ in range(key_size)]

def substitute_sbox(input_bytes, sbox):
    """Substitutes bytes using the given S-box."""
    return [sbox[b] for b in input_bytes]

def create_sbox():
    """Creates a simple S-box by shuffling values 0-255."""
    sbox = list(range(256))
    random.shuffle(sbox)
    return sbox

def main():
    # Generate a random S-box
    sbox = create_sbox()
    print("Generated S-box:", sbox)
    
    # Generate a random key
    key = generate_key()
    print("Generated Key:", key)
    
    # Substitute key using S-box
    substituted_key = substitute_sbox(key, sbox)
    print("Substituted Key:", substituted_key)

if __name__ == "__main__":
    main()
