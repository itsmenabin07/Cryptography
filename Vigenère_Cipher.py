# Vigenère Cipher Implementation without Functions

message = input("Enter the message: ")
key = input("Enter the key: ")

key_full = ""
key_index = 0
for char in message:
    if char.isalpha():  # Only extend the key for letters
        key_full += key[key_index % len(key)]
        key_index += 1
    else:
        key_full += char  # Non-alphabetic characters retain their position

encrypted_message = ""
for i in range(len(message)):
    char = message[i]
    if char.isupper():
        encrypted_message += chr((ord(char) + ord(key_full[i]) - 2 * ord('A')) % 26 + ord('A'))
    elif char.islower():
        encrypted_message += chr((ord(char) + ord(key_full[i]) - 2 * ord('a')) % 26 + ord('a'))
    else:
        encrypted_message += char  # Non-alphabetic characters remain unchanged

decrypted_message = ""
for i in range(len(encrypted_message)):
    char = encrypted_message[i]
    if char.isupper():
        decrypted_message += chr((ord(char) - ord(key_full[i]) + 26) % 26 + ord('A'))
    elif char.islower():
        decrypted_message += chr((ord(char) - ord(key_full[i]) + 26) % 26 + ord('a'))
    else:
        decrypted_message += char  # Non-alphabetic characters remain unchanged

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
