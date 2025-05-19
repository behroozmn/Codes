#!/bin/bash
while true; do ping 8.8.8.8 -c 2 > /tmp/ping.log  && zenity --info --text="$(date +%T).\n\nInternet is OK." --title="Coffee time" --ok-label="exit" && exit; sleep 2; done;

