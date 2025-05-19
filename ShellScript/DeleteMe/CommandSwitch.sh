#!/bin/bash
while getopts "a:f:n:v:z:" options; do
    case "${options}" in
    a)
        valueA="$OPTARG"
        ;;
    f)
        valueF="$OPTARG"
        ;;
    n)
        valueN="$OPTARG"
        ;;
    v)
        valueV="$OPTARG"
        ;;
    z)
        valueZ="$OPTARG"
        ;;
    *)
        :
        ;;
    esac
done

echo "valueA:${valueA}"
echo "valueF:${valueF}"
echo "valueN:${valueN}"
echo "valueV:${valueV}"
echo "valueZ:${valueZ} "


# output:
# ./CommandSwitch.sh  -z 1 -n2  -v 3 -a 4  -f 5
# valueA:4
# valueF:5
# valueN:2
# valueV:3
# valueZ:1