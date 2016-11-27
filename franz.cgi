#!/bin/bash

echo "Content: text/html

"

if [ -e "$1" ]
then
	./bin/dir-to-html.sh "$1"
fi
