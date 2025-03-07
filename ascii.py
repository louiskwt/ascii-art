from PIL import Image
import argparse, math, os

ASCII_CHAR_SET = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@" # 91 Chars
MAX_HEIGHT = 60
MAX_WIDTH = 50

def weighted_brigtness_mapping(R: int, G: int, B: int) -> int:
    weigthed_r = 0.233 * R
    weigthed_g = 0.587 * G
    weighted_b = 0.114 * B
    return (weigthed_r + weigthed_g + weighted_b) // 3

def avg_brightness_mapping(R: int, G: int, B: int) -> int:
    return (R + B + G) // 3

def luminosity_brigtness_mapping(R: int, G: int, B: int) -> int:
    """
        an alternative to the weighted brigntess mapping that accounts for wider spectrum
    """
    return (0.2126 * R + 0.7152 * G + 0.0722 * B) // 3


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str, nargs="?", default=None)
parser.add_argument("-f", "--function", type=str, nargs="?", default=None)
parser.add_argument("-p", "--path", type=str, nargs="?", default=None)
args = parser.parse_args()

file_path = args.path
file_exist = os.path.exists(file_path)

if not file_exist:
    print("Enter a valid file path")

if not file_exist or not file_path:
    file_path = input("Enter a valid file name: ")

image = Image.open(file_path)
image = image.convert("RGB")
width, height = image.width, image.height
output = args.output
function_name = args.function

print("Successfully loaded image!")
print(f"Image size: {width} x {height}")

ratio = min(MAX_WIDTH / width, MAX_HEIGHT / height)

transformed_width, transformed_height = math.floor(width * ratio), math.floor(height * ratio)
resized_image = image.resize((transformed_width, math.floor(transformed_height * 1.65)))

print(f"Resized image size: {resized_image.width} x {resized_image.height}")

resized_width, resized_height = resized_image.width, resized_image.height

pixel_matrix = [[resized_image.getpixel((col, row)) for col in range(resized_width)] for row in range(resized_height)]

print("Successfully constructed pixel matrix!")

brightness_mapping_func = luminosity_brigtness_mapping

if function_name == "avg":
    brightness_mapping_func = avg_brightness_mapping
elif function_name == "weighted":
    brightness_mapping_func = weighted_brigtness_mapping

brightness_matrix = [[brightness_mapping_func(pixel[0], pixel[1], pixel[2]) for pixel in row] for row in pixel_matrix]
print("Successfully constructed brightness matrix!")

"""
255 rgb value : 65 characters

255 / 65 = ~3.9 

"""
ascii_matrix = brightness_matrix
for row in range(len(brightness_matrix)):
    for col in range(len(brightness_matrix[row])):
        char_index = min(max(math.floor(brightness_matrix[row][col] / 3.9), 0), len(ASCII_CHAR_SET) - 1)
        ascii_matrix[row][col] = ASCII_CHAR_SET[char_index] * 3 # stretch out the ascii art so that it's not squashed

# print out in terminal
for row in ascii_matrix:
    print("".join(row))

if output:
    with open(f"{output}.txt", "w") as f:
        for row in ascii_matrix:
            f.write("".join(row))
            f.write("\n") 
        f.close()