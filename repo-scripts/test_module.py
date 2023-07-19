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

