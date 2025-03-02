from PIL import Image
import math

image = Image.open("test.jpg")
width, height = image.width, image.height

print("Successfully loaded image!")
print(f"Image size: {width} x {height}")

pixel_matrix = []

# ... 
# ...
# ...
print("Successfully constructed pixel matrix!")
for row in range(height):
    matrix = []
    for col in range(width):
        matrix.append(image.getdata()[row * width + col])
    pixel_matrix.append(matrix)

# print("Iterating through pixel contents:")

print("Successfully constructed brightness matrix!")
brightness_matrix = pixel_matrix

for row in range(len(pixel_matrix)):
    for col in range(len(pixel_matrix[row])):
        brightness_matrix[row][col] = math.floor((pixel_matrix[row][col][0] + pixel_matrix[row][col][1] + pixel_matrix[row][col][2]) / 3) 

# for row in brightness_matrix:
#     for col in row:
#         print(col)

ASCII_CHARACTER = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # 65 Chars
"""
255 rgb value : 65 characters

255 / 65 = ~3.9 

"""
ascii_matrix = brightness_matrix
for row in range(len(brightness_matrix)):
    for col in range(len(brightness_matrix[row])):
        char_index = math.floor(brightness_matrix[row][col] / 3.9) - 1
        ascii_matrix[row][col] = ASCII_CHARACTER[char_index]

for row in ascii_matrix:
    for col in row:
        print(col, end="")
    print("\n", end="")