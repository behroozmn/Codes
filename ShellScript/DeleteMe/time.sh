#!/bin/bash


#system uptime. -p: --pretty, -s: since
systemUptime=$(uptime -p)
echo "${systemUptime}"

# system uptime in seconds.
systemUptime=$(awk '{print $1}' /proc/uptime)
echo "${systemUptime}"

# Convert time
timeNowSecondsEpoch=$(date +%s)     #seconds since epoch (1970-01-01 00:00:00)
timeNowLocal=$(date +%R)            #current local time (R: 24hrs, r: 12hrs)
timeNowUTC=$(date -u +%R)           #current UTC time