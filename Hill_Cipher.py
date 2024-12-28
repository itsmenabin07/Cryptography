# Hill Cipher Implementation

# Step 1: Input the key matrix and plaintext
import numpy as np

key_matrix = []
n = int(input("Enter the size of the key matrix (n x n): "))

print(f"Enter the {n}x{n} key matrix row by row (space-separated):")
for i in range(n):
    row = list(map(int, input().split()))
    key_matrix.append(row)

plaintext = input("Enter the plaintext: ").replace(" ", "").upper()

# Step 2: Adjust plaintext to fit the key matrix size
while len(plaintext) % n != 0:
    plaintext += "X"  # Padding with 'X' if plaintext size is not a multiple of n

# Step 3: Convert plaintext to numerical form (A=0, B=1, ..., Z=25)
plaintext_vector = []
for char in plaintext:
    plaintext_vector.append(ord(char) - ord('A'))

# Step 4: Split plaintext vector into blocks of size n
plaintext_blocks = [plaintext_vector[i:i + n] for i in range(0, len(plaintext_vector), n)]

# Step 5: Perform matrix multiplication and modulus operation to encrypt
ciphertext_vector = []
for block in plaintext_blocks:
    # Perform matrix multiplication and take modulo 26
    cipher_block = np.dot(key_matrix, block) % 26
    ciphertext_vector.extend(cipher_block)

# Step 6: Convert numerical ciphertext back to letters
ciphertext = ""
for num in ciphertext_vector:
    ciphertext += chr(num + ord('A'))

# Step 7: Print the ciphertext
print("Ciphertext:", ciphertext)
