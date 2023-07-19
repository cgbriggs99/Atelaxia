Minecraft Function Preprocessor
===============================

This preprocessor is an extension to Python. It adds a block, ``mcf``, to Python that replaces expressions in a Minecraft function string, before translating it into Python. If run without the ``-c`` option, it will then run this Python file to produce a Minecraft function. Here is an example of how to use this tool.

.. code-block:: python

   # file name is test_module.mcpy
   import math

   if __name__ == "__main__":
       for i in range(10) :
           mcf :
               say @a "Sine of $(i) is $(math.sin(i))"

When the command ``python3 -m mcfpp -o test_module.mcfunction test_module.mcpy`` is run, it will produce an intermediate representation in pure Python, then it will run the result to make a Minecraft function. The intermediate file looks like this.

.. code-block:: python

   # Auto-generated file.
   if "sys" not in globals() :
       import sys
   if "__mc_output__" not in globals() and "__mc_output__" not in locals() :
       __mc_output__ = open("/home/connor/git/Atelaxia/repo-scripts/test_module.mcfunction", "w+")
   if type(__mc_output__) is str :
       __mc_output__ = open(__mc_output__, "w+")

   if __name__ == "__main__" :
       print("# Auto-generated function file.", file = __mc_output__)

   import math
   if __name__ == "__main__" :
       for i in range(10) :
           print(f"say @a \"Sine of {i} is {math.sin(i)}\"", file = __mc_output__)

   if __name__ == "__main__" :
       try :
           close(__mc_output__)
       except Exception :
           pass

When it is run, it will then produce the following output.

.. code-block:: MCFunction

   # Auto-generated file
   say @a "Sine of 0 is 0.0"
   say @a "Sine of 1 is 0.8414709848078965"
   say @a "Sine of 2 is 0.9092974268256817"
   say @a "Sine of 3 is 0.1411200080598672"
   say @a "Sine of 4 is -0.7568024953079282"
   say @a "Sine of 5 is -0.9589242746631385"
   say @a "Sine of 6 is -0.27941549819892586"
   say @a "Sine of 7 is 0.6569865987187891"
   say @a "Sine of 8 is 0.9893582466233818"
   say @a "Sine of 9 is 0.4121184852417566"

Command Line Options
--------------------

.. code-block:: none

   python3 -m mcfpp [-h] [-o <file>] [--version] [-v] [-B <directory>] [--save-temps] [-c] filename``

   positional arguments:
   filename        Input file.

   optional arguments:
   -h, --help      show this help message and exit
   -o <file>       Place the output into <file>.
   --version       Return the version, then do nothing.
   -v              Turn on verbose mode.
   -B <directory>  Add the directory to the search path.
   --save-temps    Save temporary files.
   -c              Compile the file to Python. Do not make a function output.

Syntax
------

Within the ``mcf`` block, the following special syntax applies.

- Typing ``\$`` will output a dollar sign.
- Typing ``$$`` will output a section sign for format codes (``§``).
- Surrounding a Python expression with ``$(...)`` will output the result of the expression directly into the function.
- Surrounding a Python expression with ``${...}`` will output the result of the expression, but will surround it with quotes. It will escape the string produced as appropriate, but will not escape backslashes.
- Indentation still applies, but only so far as your functions are more indented than the block head. Indentation among the functions themselves does not matter.
