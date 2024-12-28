# Playfair Cipher Implementation

# Step 1: Input the key and plaintext
plaintext = input("Enter the plaintext: ").replace(" ", "").upper()
key = input("Enter the key: ").replace(" ", "").upper()

# Step 2: Prepare the key matrix
key = key.replace("J", "I")  # Replace 'J' with 'I' as per Playfair Cipher rules
key_matrix = []
seen = set()

# Construct the 5x5 matrix
for char in key:
    if char not in seen and char.isalpha():
        seen.add(char)
        key_matrix.append(char)
for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Add remaining letters, skipping 'J'
    if char not in seen:
        seen.add(char)
        key_matrix.append(char)

# Reshape the key matrix into a 5x5 grid
key_matrix = [key_matrix[i:i + 5] for i in range(0, 25, 5)]

# Step 3: Prepare the plaintext
# Replace 'J' with 'I' and ensure pairs don't have repeating letters
plaintext = plaintext.replace("J", "I")
prepared_text = ""
i = 0
while i < len(plaintext):
    if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
        prepared_text += plaintext[i] + "X"
        i += 1
    else:
        prepared_text += plaintext[i] + plaintext[i + 1]
        i += 2

# Step 4: Encrypt using Playfair rules
ciphertext = ""
for i in range(0, len(prepared_text), 2):
    a, b = prepared_text[i], prepared_text[i + 1]

    # Find positions of the pair in the key matrix
    pos_a = [(r, c) for r, row in enumerate(key_matrix) for c, val in enumerate(row) if val == a][0]
    pos_b = [(r, c) for r, row in enumerate(key_matrix) for c, val in enumerate(row) if val == b][0]

    # Apply Playfair cipher rules
    if pos_a[0] == pos_b[0]:  # Same row
        ciphertext += key_matrix[pos_a[0]][(pos_a[1] + 1) % 5]
        ciphertext += key_matrix[pos_b[0]][(pos_b[1] + 1) % 5]
    elif pos_a[1] == pos_b[1]:  # Same column
        ciphertext += key_matrix[(pos_a[0] + 1) % 5][pos_a[1]]
        ciphertext += key_matrix[(pos_b[0] + 1) % 5][pos_b[1]]
    else:  # Rectangle rule
        ciphertext += key_matrix[pos_a[0]][pos_b[1]]
        ciphertext += key_matrix[pos_b[0]][pos_a[1]]

# Output the ciphertext
print("Ciphertext:", ciphertext)
