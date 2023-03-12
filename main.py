from PIL import Image
import numpy as np
import os


for filename in os.listdir("imgs"):
    inputimage = f"imgs/{filename}"
    im = Image.open(inputimage, 'r')
    Pixel_values = np.array(im)
    ff = open("font.txt","a")
    letter = filename.replace(".png","")
    ff.write(f"\n// {letter}")
    ff.write("\n{\n")
    for row in Pixel_values:
        line = "    0b"
        for pixel in row:
            if pixel[3] == 0:
                line += "0"
            if pixel[3] == 255:
                line += "1"
        line += ",\n"
        ff.write(line)
    ff.write("},")
