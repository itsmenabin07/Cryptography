# Caesar Cipher Implementation

plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

# Initialize an empty string for the ciphertext
ciphertext = ""

# Loop through each character in the plaintext
for char in plaintext:
    # Check if the character is an uppercase letter
    if char.isupper():
        # Perform the shift and wrap around using modulo
        ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    # Check if the character is a lowercase letter
    elif char.islower():
        # Perform the shift and wrap around using modulo
        ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        # Leave non-alphabetic characters unchanged
        ciphertext += char

# Print the resulting ciphertext
print("Ciphertext:", ciphertext)
