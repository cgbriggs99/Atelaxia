"""
mcfpp.pycompile

Compile a Minecraft+Python file into pure Python.
"""

import os
import sys

__HEADER = """
if __name__ == "__main__" :
    print("# Auto-generated function file.", file = __mc_output__)
"""

__FOOTER = """
if __name__ == "__main__" :
    try :
        close(__mc_output__)
    except Exception :
        pass
"""


def translate(in_fp, out_fp, mcf_fp, verbose = False) :
    """
Perform the actual translation.

:param in_fp: The input file object.
:param out_fp: The output file object.
:param verbose: Whether to be verbose.
"""
    if verbose :
        print("Starting to translate.", file = sys.stderr)

    # Check what the output file is and place it where it needs to go.
    if mcf_fp is sys.stdout :
        print("""# Auto-generated file.
if "sys" not in globals() :
    import sys
if "__mc_output__" not in globals() and "__mc_output__" not in locals() :
    __mc_output__ = sys.stdout
if type(__mc_output__) is str :
    __mc_output__ = open(__mc_output__, "w+")""", file = out_fp)
    else :
        print(f"""# Auto-generated file.
if "sys" not in globals() :
    import sys
if "__mc_output__" not in globals() and "__mc_output__" not in locals() :
    __mc_output__ = open("{os.path.abspath(mcf_fp.name)}", "w+")
if type(__mc_output__) is str :
    __mc_output__ = open(__mc_output__, "w+")""", file = out_fp)

    print(__HEADER, file = out_fp)

    if verbose :
        print("Header information added.", file = sys.stderr)

    is_mcfunc = False
    indent = 0

    for line in in_fp :
        # Need to remove ending new line.
        if line[-1] == "\n" :
            line = line[:-1]
        # If this line only has whitespace skip.
        if all(map(lambda x : x.isspace(), line)) or line == "":
            continue
        if not is_mcfunc :
            # Split into words.
            hold_line = line.expandtabs().split(" ")

            # Set to spaces for easy conversion.
            line = line.expandtabs()

            # Remove empty words.
            hold_line = list(filter(lambda x : x != '', hold_line))

            # Check to see if the first word is the block.
            if (hold_line[0] == "mcf" and hold_line[1][0] == ":") \
               or hold_line[0][:4] == "mcf:" :
                if verbose :
                    print("Found mcf block", file = sys.stderr)
                # This is the beginning of the mcf block.
                is_mcfunc = True

                # Calculate the indentation level.
                indent = 0
                while line[indent] == " " :
                    indent += 1
                if verbose :
                    print(f"mcf block at indent level {indent}", file = sys.stderr)

            else :
                # This is not the beginning of a function block.
                line = line.expandtabs()
                print(line, file = out_fp)
        else :
            # Ensure the indent level is still consistent.
            line = line.expandtabs()

            curr_indent = 0
            while line[curr_indent] == " " :
                curr_indent += 1
            if verbose :
                print(f"Current line at indent level {indent}", file = sys.stderr)

            if curr_indent <= indent :
                # Outside of block.
                if verbose :
                    print("End of mcf block.", file = sys.stderr)
                print(line, file = out_fp)
                is_mcfunc = False
                indent = 0
            else :
                # Strip the line.
                line = line.strip()
                # Check to see if the line ends in a \
                while line[-1] == "\\" :
                    # Grab the next line and stick it on the end.
                    try :
                        line = line[:-1] + " " + next(in_fp).expandtabs(8).strip()
                    except Exception as error :
                        raise SyntaxError("EOL while scanning line.") from error

                # Set up the new line.
                out_line = "".join([" " for i in range(indent)])
                out_line += "print(f\""

                # Parse through the line for dollar signs. $( and ${
                # resolve expressions, $$ becomes §. \$ is a dollar sign.
                brace_state = 0
                paren_state = 0
                for i in range(len(line)) :
                    if line[i] == "\"" :
                        out_line += "\\\""
                        continue
                    if brace_state == 0 and paren_state == 0:
                        # Look for opening braces.
                        try :
                            if line[i:i + 2] == "\\$" :
                                out_line += "$"
                            elif line[i:i + 2] == "$$" :
                                out_line += "§"
                            elif line[i:i + 2] == "$(" :
                                paren_state = 1
                                out_line += "{"
                            elif line[i:i + 2] == "${" :
                                brace_state = 1
                                out_line += "\\\"{str(str("
                            else :
                                out_line += line[i]
                        except Exception :
                            raise SyntaxError("Invalid dollar sign at end of line.")
                    elif brace_state != 0 :
                        # Keep braces straight.
                        if line[i] == "{" :
                            if brace_state != 1 :
                                out_line += line[i]
                            brace_state += 1
                        elif line[i] == "}" :
                            brace_state -= 1
                            if brace_state == 1 :
                                out_line += ").encode(\"raw_unicode_escape\"))}\\\""
                                brace_state = 0
                            else :
                                out_line += line[i]
                        else :
                            out_line += line[i]
                    elif paren_state != 0 :
                        # Keep parentheses straight.
                        if verbose :
                            print(f"Current paren depth {paren_state}", file = sys.stderr)
                        if line[i] == "(" :
                            if paren_state != 1 :
                                out_line += line[i]
                            paren_state += 1
                        elif line[i] == ")" :
                            paren_state -= 1
                            if paren_state == 1 :
                                out_line += "}"
                                paren_state = 0
                            else :
                                out_line += line[i]
                        else :
                            out_line += line[i]

                if brace_state != 0 or paren_state != 0 :
                    raise SyntaxError("Braces or parentheses not closed!")
                out_line += "\", file = __mc_output__)"
                print(out_line, file = out_fp)
    # Print the footer
    print(__FOOTER, file = out_fp)
    if verbose :
        print("Footer information added. File finished.", file = sys.stderr)
