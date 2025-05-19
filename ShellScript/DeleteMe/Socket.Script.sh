#!/bin/bash

####script summary
# Title: title
# Description: description
# Author: author <email>
# Date: yyyy-mm-dd
# Version: 1.0.0

# Exit codes
# ==========
# 0 no error
# 1 script interrupted
# 2 error description

# >>>>>>>>>>>>>>>>>>>>>>>> ExecuteOnRecieveDataFromSocket >>>>>>>>>>>>>>>>
read MESSAGE

if [[   "$MESSAGE" == "behrooz"  ]];then
    echo "I see behrooz";
else
    echo "Data:  $MESSAGE";
fi
# <<<<<<<<<<<<<<<<<<<<<<<< ExecuteOnRecieveDataFromSocket <<<<<<<<<<<<<<<<<<<<<<<<

# Listening
socat  TCP4-LISTEN:1234,reuseaddr,fork EXEC:/tmp/13980215/myscript.sh

