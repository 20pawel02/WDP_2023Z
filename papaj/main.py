from PIL import Image
import numpy as np

im = Image.open("jan_pawel_2.png")

im = im.convert("L")
im = im.resize((128, 128))

char_map = "@%#*+=-:. "

ascii_image = ""
pixels = np.array(im)
for row in pixels:
    for pixel in row:
        ascii_image += char_map[pixel // 50]
    ascii_image += "\n"

print(ascii_image)

with open("jan_pawel_ii_ascii.txt", "w") as text_file:
    text_file.write(ascii_image)
