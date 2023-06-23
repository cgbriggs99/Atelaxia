#!/bin/sh

# packager.sh
# author: Connor Briggs
#
# Packages maps, resource packs, and data packs into zip files.
#

package() {
    
    # Package maps.
    if [ -d maps ]; then
	cd ./maps
    else
	cd ../maps
    fi
    pwd
    
    zip -ru ../build/Atelaxia-Map.zip * -x@../.gitignore
    
    # Package resource pack
    cd ../resource-pack
    zip -ru ../build/Atelaxia-Resource-Pack.zip * -x@../.gitignore
    
    # Package data pack.
    cd ../data-pack
    zip -ru ../build/Atelaxia-Data-Pack.zip * -x@../.gitignore
}

# Clean the build directory.
clean() {
    if [ -d build ]; then
	rm -rf build/*
    elif [ -d ../build ]; then
	rm -rf ../build/*
    else
	echo "Could not find build directory. Do it yourself, coward."
	return -1
    fi
}

echo $1

if [ "$1" = "clean" ]; then
    clean
else
    package
fi
