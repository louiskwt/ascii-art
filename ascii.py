from PIL import Image

image = Image.open("test.jpg")
width, height = image.width, image.height

print("Successfully loaded image!")
print(f"Image size: {width} x {height}")

pixel_matrix = []

# ... 
# ...
# ...

for row in range(height):
    matrix = []
    for col in range(width):
        matrix.append(image.getdata()[row * width + col])
    pixel_matrix.append(matrix)

print("Iterating through pixel contents:")

for row in pixel_matrix:
    for pixel in row:
        print(pixel)
          

