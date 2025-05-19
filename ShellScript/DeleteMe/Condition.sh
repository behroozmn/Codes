#if condition is false then run command
[ condition ] || command

# if condition is true then run command
[ condition ] && command

# Condition.File.Notempty
if [ -s "/path/to/file" ]; then
    echo "File \"/path/to/file\" is not empty"
fi

# Condition.File.Readalbe
if [ -r "/path/to/file" ]; then
    echo "File \"/path/to/file\" is readable"
fi

# Condition.File.writealbe
if [ -w "/path/to/file" ]; then
    echo "File \"/path/to/file\" is writeable"
fi

# Condition.while.wait
Count=100
while [ شرط اول ] && [ ${Count} -gt 0 ] ; do
/bin/sleep 1
Count=$(( ${Count}-1 ))
done


# Condition.if.Quote
# Surround your variable with " in if [ "${NAME}" = "Kevin" ],
# because if $NAME isn't declared, bash will throw a syntax error(also see nounset). 


# Condition.if.File1OlderThanFile2
if [ "/path/to/file1" -ot "/path/to/file2" ]; then
    echo "Path \"/path/to/file1\" is older than path \"/path/to/file2\""
fi


# Condition.if.File1NewerThanFile2
# check if file1 is newer than file2
if [ "/path/to/file1" -nt "/path/to/file2" ]; then
    echo "Path \"/path/to/file1\" is newer than path \"/path/to/file2\""
fi



# Condition.if.==
# You don't need two equal signs when checking if [ "${NAME}" = "Kevin" ]


# Condition.if
# Use (( ... )) rather than [[ ... ]] when evaluating integers




# Behrooz
# if command; then
#    :
# fi
#### Example
# if /usr/local/sbin/zpool-delete "${poolName}" &>>"$LOG"; then
#        sed -i "/\<${poolName}\>/d" "${filePools}"
#        logPrint "sed -i '/${poolName}/d' ${filePools}"
#        logPrint "\n$(zpool status | nl)"
#        echo "pool [${poolName}] is correctly deleted"
# else
#        echo -e "pool [${poolName}] is \e[31m NOT\e[39m correctly deleted"
# fi



#Behrooz
#logPrint "zpool add -f ${poolName} ${raidType} ${out[*]}"               #نکته: ستاره سبب قرار دادن در یک خط است 
#if zpool add -f "${poolName}" "${raidType}" "${out[@]}" &>>"$LOG"; then #نکته: حتما باید @ باشد وگرنه اگر ستاره باشد باید حتما بدون کوتیشن باشد
#         echo -e "${GREEN}DONE${NOCOLOR}"
# else
#        echo -e "${RED}Not DONE${NOCOLOR}"
#fi
