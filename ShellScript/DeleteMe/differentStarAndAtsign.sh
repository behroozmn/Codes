#!/bin/bash

echo "Using \"\$*\":"
for a in "$*"; do
    echo $a;
done

echo -e "\nUsing \$*:"
for a in $*; do
    echo $a;
done

echo -e "\nUsing \"\$@\":"
for a in "$@"; do
    echo $a;
done

echo -e "\nUsing \$@:"
for a in $@; do
    echo $a;
done

# ussing format
#./script.sh  one two "three four"
# نکته: همواره اگر از دابل کوت استفاده شود سبب می‌شود که اسپیس دیتِکت شود
