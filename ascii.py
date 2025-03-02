from PIL import Image
import math

image = Image.open("test.jpg")
width, height = image.width, image.height

print("Successfully loaded image!")
print(f"Image size: {width} x {height}")

MAX_HEIGHT = 200
MAX_WIDTH = 100
ratio = min(MAX_WIDTH/width, MAX_HEIGHT/height)

transformed_width, transformed_height = math.floor(width * ratio), math.floor(height * ratio)
resized_image = image.resize((transformed_width, transformed_height), Image.Resampling.LANCZOS)

print(f"Resized image size: {resized_image.width} x {resized_image.height}")

resized_width, resized_height = resized_image.width, resized_image.height

pixel_matrix = []

# ... 
# ...
# ...
print("Successfully constructed pixel matrix!")
for row in range(resized_height):
    matrix = []
    for col in range(resized_width):
        matrix.append(resized_image.getdata()[row * resized_width + col])
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
        ascii_matrix[row][col] = ASCII_CHARACTER[char_index] * 3

for row in ascii_matrix:
    for col in row:
        print(col, end="")
 