#!/bin/bash

# Compaire
man test
man bash


test -e $VAR                #Check Exist
test -d "$VAR"              #A test to check if a FILE exists and is a directory.
test -x "$VAR"              #A test to check if FILE exists and execute (or search) permission is granted
test -e "$VAR"              #A test to check if FILE exists
test -h "$VAR"              #A test to check if FILE exists and is a symbolic link (same as -L)
test -r "$VAR"              #A test to check if FILE exists and read permission is granted.
test -f "$VAR"              #test exist readable
test -w "$VAR"              #A test to check if FILE exists and write permission is granted.
test "$VAR" -ef "$VAR"      #A test to check if FILE1 and FILE2 have the same device and inode numbers.
test "$VAR" -nt "$VAR"      #A test to check if FILE1 is newer (modification date) than FILE2.
test "$VAR" -ot "$VAR"      #A test to check if FILE1 is older than FILE2.
test "$VAR1" -eq "$VAR2"    #[intEqual]A test to compare two different INTEGERS. Returns TRUE if they are of equal value.
test "$VAR1" -ge "$VAR2"    #[intGreatEqual]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is of equal or greater value than INTEGER2.
test "$VAR1" -gt "$VAR2"    #[intGreatThan]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is greater than INTEGER2 in value
test "$VAR1" -le "$VAR2"    #[intLessEqual]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is less than or equal to INTEGER2 in value.
test "$VAR1" -lt "$VAR2"    #[intLessThan]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is less than INTEGER2 in value.
test "$VAR1" -ne "$VAR2"    #[intNotEqual]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is NOT equal to INTEGER2 in value.
test -z "$VAR"              #[string Empty] A test to check the lengh of VAR is zero (i.e. it is empty) and returns TRUE if so.
test "$VAR1" = "$VAR2"      #[string Equal] A test to compare two different STRINGS and returns TRUE if they are of equal value
test -n "$VAR"              #[string NotEmpty] A test that checks the length of a STRING is greater than zero and returns TRUE if so
test "$VAR1" != "$VAR2"     #[string NotEqual] A test to compare two different STRINGS. Returns TRUE if they are NOT of equal value






if [ -d "/../dir/.." ]   # → If Dir  Exist
if [ -f "/../file.txt" ] # → If file Exist
if [ -z "$variable" ]    # → وقتی متغیر تهی باشد 