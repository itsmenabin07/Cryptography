# Rail-Fence Cipher Implementation without Functions

message = input("Enter the message: ").replace(" ", "").upper()
rails = int(input("Enter the number of rails: "))

rail_matrix = [["" for _ in range(len(message))] for _ in range(rails)]
direction_down = False
row = 0

for col in range(len(message)):
    rail_matrix[row][col] = message[col]
    if row == 0 or row == rails - 1:
        direction_down = not direction_down
    row += 1 if direction_down else -1

encrypted_message = ""
for i in range(rails):
    for j in range(len(message)):
        if rail_matrix[i][j] != "":
            encrypted_message += rail_matrix[i][j]

rail_matrix = [["" for _ in range(len(message))] for _ in range(rails)]
direction_down = False
row = 0

for col in range(len(message)):
    rail_matrix[row][col] = "*"
    if row == 0 or row == rails - 1:
        direction_down = not direction_down
    row += 1 if direction_down else -1

index = 0
for i in range(rails):
    for j in range(len(message)):
        if rail_matrix[i][j] == "*" and index < len(encrypted_message):
            rail_matrix[i][j] = encrypted_message[index]
            index += 1

decrypted_message = ""
row = 0
direction_down = False
for col in range(len(message)):
    decrypted_message += rail_matrix[row][col]
    if row == 0 or row == rails - 1:
        direction_down = not direction_down
    row += 1 if direction_down else -1

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
