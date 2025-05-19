#!/bin/bash

_time=$(date +%Y/%m/%d-%H:%M:%S)
if /usr/bin/zenity --question --title="یادآوری" --text="${_time}\nثبت فعالیت کنونی :" --ok-label="ثبت" --cancel-label="عدم ثبت"; then
	echo "${_time}-Registry successfully done" >>"/tmp/Behrooz.log"
fi