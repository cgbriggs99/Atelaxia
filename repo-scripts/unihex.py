#!/usr/bin/python3

import os
import sys
import argparse
from PIL import Image as img

"""
This module converts image files into unihex format for Minecraft fonts.
This can be done using the parse_file function.
"""

def to_hex_size(number, length) :
    """
Convert a number to a hex string with the given length in bytes.

Parameters
----------
number: The number to convert.
length: The length in bytes that you want the number to be.
"""
    out = []
    vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
            'c', 'd', 'e', 'f']
    try :
        conv = int(number)
    except ValueError :
        conv = int(number, 16)
    for i in range(length * 2) :
        out.append(vals[conv % 16])
        conv //= 16
    # Need to reverse it.
    return "".join(reversed(out))

def parse_file(fname, cutoff = 0x7f, keep_dark = True) :
    """
Parse an image file and return the hex representation as a string.

Parameters
----------
fname: A string representing the name of the file.
cutoff: The cutoff for empty pixels. Defaults to 0x7f.
keep_dark: Whether the cutoff makes dark pixels clear, or light pixels clear.
    Defaults to True, which makes light pixels clear and keeps dark pixels.
"""
    image = img.open(fname)
    assert(image.width <= 32 and image.height <= 16)

    out = []
    for i in range(image.height) :
        row = 0
        for j in range(image.width) :
            # Convert to bits.
            row *= 2
            value = sum(image.getpixel((j, i))) / len(image.getpixel((j, i)))
            if (value >= cutoff and not keep_dark) or \
                        (value <= cutoff and keep_dark) :
                row += 1
        if image.width % 8 != 0 :
            for j in range(8 - (image.width % 8)) :
                row *= 2
        # Append the number converted to zero-extended hex.
        out.append(to_hex_size(row, image.width // 8))
    if image.height < 16 :
        for i in range(16 - image.height) :
            # Do this because I'm lazy, and it shouldn't affect performance
            # on small data sets.
            out.append(to_hex_size(0, image.width // 8))
    # Combine the individuals into a string of hex values.
    return "".join(out)

if __name__ == "__main__" :
    # Set up parsing.
    parser = argparse.ArgumentParser(description = "Converts images into Minecraft unihex files.")

    # Set up options.
    parser.add_argument("--file", "-f", help = "Input file to the parser",
                        required = True)
    parser.add_argument("--codepoint", "-p",
                        help = "The code point to set the character to.",
                        required = False)
    parser.add_argument("--cutoff", "-c", default = 0x7f, type = int,
                        required = False,
                        help = "The cutoff for what is considered to be part of the character or not.")
    parser.add_argument("--keep-dark", default = True, type = bool,
                        required = False,
                        help = "Whether to keep dark pixels or light pixels")
    
    args = vars(parser.parse_args())

    # Convert the image.
    imgstring = parse_file(args["file"], args["cutoff"], args["keep_dark"])

    # Print the string.
    if "codepoint" in args :
        print(to_hex_size(args["codepoint"], 3) + ":" + imgstring)
    else :
        print(imgstring)
    
