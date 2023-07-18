"""
mcfpp.main

The main program for the Minecraft function preprocessor.
"""

import argparse
import sys
import time
import os
from . import pycompile
from . import version



def main(argv = None) :
    """
    main

    :return: Zero on success, otherwise an error code.

    The main function of the preprocessor.
    """

    # Set up argument parsing.
    parser = argparse.ArgumentParser(prog = "python3 -m mcfpp", description = """
Preprocess a Minecraft function file.
""")

    parser.add_argument("filename", help = "Input file.", type = str)
    parser.add_argument("-o", help = "Place the output into <file>.",
                        type = str, default = sys.stdout, metavar = "<file>")
    #parser.add_argument("-D", help = "Define a macro.",
    #                    type = str, metavar = "<macro>")
    parser.add_argument("--version", help = "Return the version, then do nothing.",
                        action = "version", version = version.version())
    parser.add_argument("-v", help = "Turn on verbose mode.",
                        action = "store_true")
    parser.add_argument("-B", help = "Add the directory to the search path.",
                        type = str, action = "extend",
                        metavar = "<directory>")
    parser.add_argument("--save-temps", help = "Save temporary files.",
                        action = "store_true")

    parser.add_argument("-c", help = "Compile the file to Python. Do not make a function output.",
                        action = "store_true")

    # Parse the arguments.
    if argv is not None :
        args = vars(parser.parse_args(argv))
    else :
        args = vars(parser.parse_args())

    if "v" in args and args["v"] :
        print(f"Parsed arguments: {args}", file = sys.stderr)

    # Just print the version and exit.
    if "version" in args :
        return

    # Set up the output file. If none, then standard output is assumed.
    if "o" in args and isinstance(args["o"], str):
        output_file = open(args["o"], "w+")
    else :
        output_file = sys.stdout

    include_search = sys.path
    if "B" in args and args["B"] is not None :
        include_search.extend(args["B"])

    if "v" in args and args["v"] :
        print(f"Include search path is now the following: {include_search}")

    if "save_temps" not in args or not args["save_temps"] :
        temp_file = open(os.path.abspath(f"./temp_{hash(time.gmtime())}.py"), "w+")
    elif "c" not in args or not args["c"]:
        temp_file = open(os.path.abspath(args["filename"]).replace(".mcpy", ".py"), "w+")
    elif "c" in args and args["c"] :
        temp_file = output_file
    else :
        temp_file = sys.stdout

    if "v" in args and args["v"] :
        print(f"Temporary file: {temp_file.name}", file = sys.stderr)

    in_file = open(os.path.abspath(args["filename"]), "r")

    # Translate the file.
    pycompile.translate(in_file, temp_file, output_file,
                          verbose = args["v"])

    # Make the final output.
    if "c" not in args or not args["c"] :
        if args["v"] :
            print("Compiling file.", file = sys.stderr)
        temp_file.flush()
        temp_file.seek(0)
        temp_file.flush()
        source = compile(temp_file.read(), str(temp_file.name), "exec")
        exec(source)

        if "save_temps" not in args or not args["save_temps"] :
            if "v" in args and args["v"] :
                print(f"Removing {temp_file.name}")
            name = temp_file.name
            os.remove(os.path.abspath(name))
    if "v" in args and args["v"] :
        print("Finishing up.", file = sys.stderr)
    temp_file.close()
    in_file.close()
    if temp_file is not output_file :
        output_file.close()


if __name__ == "__main__" :
    main()
