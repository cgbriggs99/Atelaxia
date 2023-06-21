Unihex Converter (unihex.py)
============================

.. py:module:: unihex
  
Minecraft unihex fonts are new in 1.20. They can be used to add glyphs to the character set with resource packs, but the file format can be a little weird.

Command Line
------------

To see a help message, type

.. code::

   python3 unihex.py -h

This program uses Python's PIL library to read images. Most common formats, such as PNG and JPEG, are accepted. To convert an image, invoke as such.

.. code::

   # Long way
   python3 unihex.py --file filename.png

   # Short way
   python3 unihex.py -f filename.png

This will convert the image into a hexadecimal string. It contains no information on the codepoint, though. The files must have dimensions of at most 32 by 16. Examples of properly sized glyphs can be seen in ``repo-scripts/test_glyphs``. To specify which codepoint the glyph will represent, pass it to the ``--codepoint`` or ``-p`` option. This option accepts decimal and hexidecimal numbers, with hexadecimal numbers formatted as ``0xabcdef`` or ``0xABCDEF``, or some combination. If this is done, the program will output a unihex line that can be directly pasted into the unihex file.

The ``--cutoff`` or ``-c`` argument specifies that if the average value of a pixel is below this cutoff, it will be set as a 1 in the glyph. If it is greater, then it will be set as a 0 in the glyph. Setting the ``--keep-dark`` option to ``False`` inverts this behavior.

The average value is found by adding together the red, green, and blue channels then dividing by 3. If the image has an alpha channel, it will then be multiplied by the alpha channel and divided by 255 to normalize.

Module Documentation
--------------------

.. py:function:: to_hex_size(number, length)

   :param number: The number to convert.
   :type number: str or int
   :param length: The number of bytes to be output. This will be half the length of the final string.
   :type length: int
   :return: The hexadecimal representation of the string with leading zeros added for padding.

   Converts a number into hexadecimal with padding zeros placed in front. This string does not include the leading ``0x``.

.. py:function:: parse_file(fname, cutoff = 0x7f, keep_dark = True)

   :param str fname: The name of the image file.
   :param cutoff: The cutoff value which determines whether a pixel is considered to be on or off.
   :param keep_dark: Whether dark pixels are part of the image, or light pixels are part of the image. Defaults to ``True``, which means that dark pixels are part of the image.
   :return: The hexadecimal string representation of the given image.



