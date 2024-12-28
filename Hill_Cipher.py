# Hill Cipher Implementation


import numpy as np

key_matrix = []
n = int(input("Enter the size of the key matrix (n x n): "))

print(f"Enter the {n}x{n} key matrix row by row (space-separated):")
for i in range(n):
    row = list(map(int, input().split()))
    key_matrix.append(row)

plaintext = input("Enter the plaintext: ").replace(" ", "").upper()


while len(plaintext) % n != 0:
    plaintext += "X"  


plaintext_vector = []
for char in plaintext:
    plaintext_vector.append(ord(char) - ord('A'))


plaintext_blocks = [plaintext_vector[i:i + n] for i in range(0, len(plaintext_vector), n)]


ciphertext_vector = []
for block in plaintext_blocks:

    cipher_block = np.dot(key_matrix, block) % 26
    ciphertext_vector.extend(cipher_block)


ciphertext = ""
for num in ciphertext_vector:
    ciphertext += chr(num + ord('A'))


print("Ciphertext:", ciphertext)
