#!/bin/bash

# Am I Root
if (( $(id -u) == 0 )); then
    echo "I'm root"
fi

# Get data from user
read -rep "Question here? " -i "Default answer" answer
echo "${answer}"