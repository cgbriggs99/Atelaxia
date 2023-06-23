Packager Script (packager.sh)
=============================

This script packages the project for release and use with Minecraft. It can take one optional argument, ``clean``, which will clean the build directory. Here is the usage of this script.::

  # Zips up maps and packs. First option only works if it has been chmod-ed.
  packager.sh
  sh packager.sh

  # Cleans the build directory. First option only works if it has been chmod-ed.
  packager.sh clean
  sh packager.sh clean
