from PIL import Image
import math

image = Image.open("test2.png")
image = image.convert("RGB")
width, height = image.width, image.height

print("Successfully loaded image!")
print(f"Image size: {width} x {height}")

MAX_HEIGHT = 60
MAX_WIDTH = 80
ratio = min(MAX_WIDTH/width, MAX_HEIGHT/height)

transformed_width, transformed_height = math.floor(width * ratio), math.floor(height * ratio)
resized_image = image.resize((transformed_width, math.floor(transformed_height * 1.65)))

print(f"Resized image size: {resized_image.width} x {resized_image.height}")

resized_width, resized_height = resized_image.width, resized_image.height

pixel_matrix = []

print("Successfully constructed pixel matrix!")
for row in range(resized_height):
    matrix = []
    for col in range(resized_width):
        matrix.append(resized_image.getpixel((col, row)))
    pixel_matrix.append(matrix)

# print("Iterating through pixel contents:")

brightness_matrix = [[math.floor((pixel[0] + pixel[1] + pixel[2]) / 3) for pixel in row] for row in pixel_matrix]
print("Successfully constructed brightness matrix!")

ASCII_CHARACTER = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # 65 Chars
"""
255 rgb value : 65 characters

255 / 65 = ~3.9 

"""
ascii_matrix = brightness_matrix
for row in range(len(brightness_matrix)):
    for col in range(len(brightness_matrix[row])):
        char_index = min(max(math.floor(brightness_matrix[row][col] / 3.9), 0), len(ASCII_CHARACTER) - 1)
        ascii_matrix[row][col] = ASCII_CHARACTER[char_index] * 3 # stretch out the ascii art so that it's not squashed

for row in ascii_matrix:
    print("".join(row))