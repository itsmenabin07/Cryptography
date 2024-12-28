# Caesar Cipher Implementation

plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))


ciphertext = ""


for char in plaintext:

    if char.isupper():

        ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    
    elif char.islower():
    
        ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
       
        ciphertext += char


print("Ciphertext:", ciphertext)
