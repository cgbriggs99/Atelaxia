Python
======

When writing Python code, the latest version of Python3 is preferred. A hash-bang line at the beginning of your code is optional. This is a line that looks like ``#!/usr/bin/python3`` which tells the command line utility where to find the Python interpreter for making executable scripts. Before submission, your code should be run through a linter like PyLint. We prefer code that scores at least 9/10, but you should try to make it better. There may be arguments to let lower scores through, but in order to maintain good coding standards, we will not move too far from this.

Names
-----

When naming things in your Python code, the following standards are apreciated.

- Classes should be in ``CapitalizedWords``.
- Functions and methods should be in ``lower_case_with_underscores``.
- Constants should be in ``UPPER_CASE_WITH_UNDERSCORES``.
- Variables and arguments should be in ``lower_case_with_underscores``.
- File names and module names should be in ``lower_case_with_underscores``. This is to avoid confusion and to make it easier to import.

Also, avoiding undescriptive names like ``i, j, k`` or ``x, y, z`` would be nice, but if these undescriptive variables have common uses, like a loop index, it may be allowed. For instance, the following is perfectly acceptable, since ``i`` is a very common loop index variable name.

.. code-block:: python

   for i in range(10) :
       ...

Code Formatting
---------------

When formatting your code, use four spaces per level of indentation. Line continuations may use a different amount to make it easier to read. For instance, in this example, the second line is aligned to the beginning of the right hand argument so as to make it look more natural.

.. code-block:: python

   value = sum(image.getpixel((j, i))[:3]) / 3 * \
           image.getpixel((j, i))[3] / 255

It could just as easily be this instead.

.. code-block:: python

   value = sum(image.getpixel((j, i))[:3]) / 3 *\
       image.getpixel((j, i))[3] / 255

Spaces Between Operators
^^^^^^^^^^^^^^^^^^^^^^^^

Spaces are preferred between arguments of a binary operator and the operator. Spaces are also preferred after commas, as well as after colons in dictionary entries. They are not prefered in slices, and not required before control flow colons. If you have a way you are comfortable with, go with your preferred spacing. Otherwise, try to use ours to become more familiar with consistent style.
