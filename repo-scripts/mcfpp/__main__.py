"""
mcfpp.main

The main program for the Minecraft function preprocessor.
"""

import argparse
import sys
from . import *
import time
import os


def main(argv = sys.argv) :
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
    args = vars(parser.parse_args(argv[1:]))

    if "v" in args and args["v"] :
        print(f"Parsed arguments: {args}", file = sys.stderr)

    # Just print the version and exit.
    if "version" in args :
        return

    # Set up the output file. If none, then standard output is assumed.
    if "o" in args and type(args["o"]) == str:
        OUTPUT_FILE = open(args["o"], "w+")
    else :
        OUTPUT_FILE = sys.stdout

    INCLUDE_SEARCH = sys.path
    if "B" in args and args["B"] is not None :
        INCLUDE_SEARCH.extend(args["B"])

    if "v" in args and args["v"] :
        print(f"Include search path is now the following: {INCLUDE_SEARCH}")

    if "save_temps" not in args or not args["save_temps"] :
        TEMP_FILE = open(os.path.abspath(f"./temp_{hash(time.gmtime())}.py"), "w+")
    elif "c" not in args or not args["c"]:
        TEMP_FILE = open(os.path.abspath(args["filename"]).replace(".mcpy", ".py"), "w+")
    elif "c" in args and args["c"] :
        TEMP_FILE = OUTPUT_FILE
    else :
        TEMP_FILE = sys.stdout

    if "v" in args and args["v"] :
        print(f"Temporary file: {TEMP_FILE.name}", file = sys.stderr)

    IN_FILE = open(os.path.abspath(args["filename"]), "r")

    # Translate the file.
    pycompile.translate(IN_FILE, TEMP_FILE, OUTPUT_FILE,
                          verbose = args["v"])

    # Make the final output.
    if "c" not in args or not args["c"] :
        if args["v"] :
            print("Compiling file.", file = sys.stderr)
        TEMP_FILE.flush()
        TEMP_FILE.seek(0)
        TEMP_FILE.flush()
        source = compile(TEMP_FILE.read(), str(TEMP_FILE.name), "exec")
        exec(source)
        
        if "save_temps" not in args or not args["save_temps"] :
            if "v" in args and args["v"] :
                print(f"Removing {TEMP_FILE.name}")
            name = TEMP_FILE.name
            os.remove(os.path.abspath(name))
    if "v" in args and args["v"] :
        print("Finishing up.", file = sys.stderr)
    TEMP_FILE.close()
    IN_FILE.close()
    if TEMP_FILE is not OUTPUT_FILE :
        OUTPUT_FILE.close()
    

if __name__ == "__main__" :
    main()
