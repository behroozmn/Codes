#!/bin/bash

source "/usr/local/sbin/Libraries/Initialize.sh"
import "lib_log"
import "lib_drbd"
import "lib_ExecuteHandler"

export LOG="/var/log/rama/drbd.log"
logInitialize

Arg1="${1}"
Arg2="drbd${2}"

banner "Set DRBD Attribute" "${@}"
