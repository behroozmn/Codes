#!/bin/bash

# Renice: change running process priority. n: -20 (highest priority) to 19 (lowest priority) (shellman)
for p in \((pidof "processName"); do sudo renice -n -20 -p "\)p"; done```

# list processes By Name
processInstances=\((pgrep -l "\){processName}")

# find process ID(s) aka PIDs By Name
readarray -t processIDsArray < <(pgrep processName)
echo "${processIDsArray[@]}"


# list processes By Name
ProcessIDs() {
    echo "All processId [App: "\(1"] : \)(pidof "$1")"
    return $?
}
ProcessIDs "OutputMessenger"
#[output] → All processId [App: OutputMessenger] : 19346 19336 19287 19284




# list processes
ps -A


# find process name by it's ID(s)
processName=\((ps -p \){pid} -o comm=)


# kill process by name
sudo kill -9 "$(pgrep processName)"