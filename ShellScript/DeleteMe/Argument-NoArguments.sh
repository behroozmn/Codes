#!/bin/bash
#
if [ -z $1 ];then
	echo Please provide an argument
	read ARG
else
	ARG=$1
fi

echo Your argument was $ARG
