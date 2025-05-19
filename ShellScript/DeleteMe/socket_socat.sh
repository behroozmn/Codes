#!/bin/bash

#################################################LOCAL###########################
export Port="55055"
export ScriptName="02-Script.sh"

# Listen
/usr/bin/nohup /usr/bin/socat TCP4-LISTEN:"$Port",reuseaddr,fork,ignoreeof,keepalive EXEC:$(/usr/bin/dirname "$0")/"$ScriptName" &
/usr/bin/nohup /usr/bin/socat TCP4-LISTEN:"$Port",reuseaddr,fork,ignoreeof,keepalive EXEC:/bin/MyScript.sh &

#MyScript
read MESSAGE

peerServer="$SOCAT_PEERADDR"
peerSendServerIP=$PeerServer
peerSendServerIP=$SOCAT_PEERPORT

localRecieveServerIP=$SOCAT_SOCKADDR
localRecieveServerPort=$SOCAT_SOCKPORT
localParentPid=$SOCAT_PPID
localScriptPid:$$

 
#################################################LOCAL###########################

#################################################PEER###########################
#send
echo "check" | socat -t 3 - TCP:127.0.0.1:55055,connect-timeout=3
echo "$2" | socat -t $timeOut - TCP:$1:$Port,connect-timeout=$timeOut
#############################################PEER###########################
