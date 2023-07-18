"""
mcfpp.version

Contains a single value, __VERSION, which tells the version. This should be
accessed using the function mcfpp.version.version().
"""

__VERSION = "alpha"

def version() :
    """
Return the version.
"""
    return __VERSION
