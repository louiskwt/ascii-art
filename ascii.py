from PIL import Image

image = Image.open("test.jpg")
size = image.size

print("Successfully loaded image!")
print(f"Image size: {size[0]} x {size[1]}")

