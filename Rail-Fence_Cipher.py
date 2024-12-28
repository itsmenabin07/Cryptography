# Rail-Fence Cipher Implementation without Functions

# Step 1: Input the message and number of rails
message = input("Enter the message: ").replace(" ", "").upper()
rails = int(input("Enter the number of rails: "))

# Step 2: Create the rail matrix for encryption
rail_matrix = [["" for _ in range(len(message))] for _ in range(rails)]
direction_down = False
row = 0

# Step 3: Populate the rail matrix with the message
for col in range(len(message)):
    rail_matrix[row][col] = message[col]
    if row == 0 or row == rails - 1:
        direction_down = not direction_down
    row += 1 if direction_down else -1

# Step 4: Read the encrypted message from the rail matrix
encrypted_message = ""
for i in range(rails):
    for j in range(len(message)):
        if rail_matrix[i][j] != "":
            encrypted_message += rail_matrix[i][j]

# Step 5: Create the rail matrix for decryption
rail_matrix = [["" for _ in range(len(message))] for _ in range(rails)]
direction_down = False
row = 0

# Step 6: Mark positions in the matrix for decryption
for col in range(len(message)):
    rail_matrix[row][col] = "*"
    if row == 0 or row == rails - 1:
        direction_down = not direction_down
    row += 1 if direction_down else -1

# Step 7: Fill the marked positions with the encrypted message
index = 0
for i in range(rails):
    for j in range(len(message)):
        if rail_matrix[i][j] == "*" and index < len(encrypted_message):
            rail_matrix[i][j] = encrypted_message[index]
            index += 1

# Step 8: Read the decrypted message from the rail matrix
decrypted_message = ""
row = 0
direction_down = False
for col in range(len(message)):
    decrypted_message += rail_matrix[row][col]
    if row == 0 or row == rails - 1:
        direction_down = not direction_down
    row += 1 if direction_down else -1

# Step 9: Print the results
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
