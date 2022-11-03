# import

row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

new_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

print(new_map[1])
position = input("Where do you want to put the treasure? ")
positionOne = int(position[0]) - 1
positionTwo = int(position[1]) - 1

# print(f"{positionOne}, {positionTwo}")
selected_row = new_map[positionTwo]
selected_row.pop(positionOne)
selected_row.insert(positionOne, "X")
print(f"{row1}\n{row2}\n{row3}")
