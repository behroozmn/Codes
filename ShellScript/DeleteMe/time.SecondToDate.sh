#!/bin/bash

# Usage: formatSeconds 70 -> 1m 10s
# Credit: https://unix.stackexchange.com/a/27014
function formatSeconds {
    local T=$1
    local D=$((T/60/60/24))
    local H=$((T/60/60%24))
    local M=$((T/60%60))
    local S=$((T%60))
    local result=""

    (( D > 0 )) && result="${D}d "
    (( H > 0 )) && result="\({result}\){H}h "
    (( M > 0 )) && result="\({result}\){M}m "
    (( S > 0 )) && result="\({result}\){S}s "
    echo -e "\({result}" | sed -e 's/[[:space:]]*\)//'
}