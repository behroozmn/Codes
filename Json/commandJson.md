/home/user/.commands.json
```json
{
    "menu": [
        {
            "title": "TERMINAL",
            "type": "submenu",
            "submenu": [
                {
                    "title": "Kill OutputMessenger",
                    "command": "gnome-terminal -- bash -c 'kill -9 $(pidof OutputMessenger)'",
                    "icon": "utilities-terminal"
                },
                {
                    "title": "Kill thunderbird",
                    "command": "gnome-terminal -- bash -c 'kill -9 $(pidof thunderbird)'",
                    "icon": "utilities-terminal"
                },
                {
                    "title": "Open Terminator",
                    "command": "terminator",
                    "icon": "terminator"
                },
                {
                    "title": "Bussy Command",
                    "command": "gnome-terminal -- bash -c '/usr/bin/cat /dev/urandom | hexdump -C | grep --color=auto -E \"aa|bb|cc|dd|ee|ff\"; exec bash'",
                    "icon": "user-busy"
                }
            ]
        },
        {
            "type": "separator"
        },
        {
            "title": "FILES",
            "type": "submenu",
            "submenu": [
                {
                    "title": "Files",
                    "command": "nautilus /home/Files",
                    "icon": "folder"
                },
                {
                    "title": "DeleteME",
                    "command": "nautilus /home/user/DeleteME",
                    "icon": "folder"
                },
                {
                    "title": "tmp",
                    "command": "nautilus /tmp",
                    "icon": "folder"
                }
            ]
        },
        {
            "type": "separator"
        },
        {
            "title": "nmap custom IP(GUI)",
            "command": "gnome-terminal -- bash -c 'ip=$(zenity --entry --title=\"Input\" --text=\"Enter ip:\"); if [ -n \"$ip\" ]  ; then /usr/bin/sudo /usr/bin/nmap -T5 $ip;fi;/usr/bin/sleep 2; exec bash'",
            "icon": "network-offline"
        },
        {
            "title": "nmap custom IP",
            "command": "gnome-terminal -- bash -c 'echo \"Enter IP:\"; read ip;/usr/bin/sudo /usr/bin/nmap -T5 $ip;/usr/bin/sleep 2;'",
            "icon": "network-offline"
        },
        {
            "title": "NMAP",
            "type": "submenu",
            "submenu": [
                {
                    "title": "xx.xx.xx.xx(General)",
                    "command": "terminator -x bash -c '/usr/bin/sudo /usr/bin/nmap -T5 xx.xx.xx.2;/usr/bin/sleep 2;'",
                    "icon": "network-offline"
                },
                {
                    "title": "xx.xx.xx.xx(Email)",
                    "command": "terminator -x bash -c '/usr/bin/sudo /usr/bin/nmap -T5 xx.xx.xx.5;/usr/bin/sleep 2;'",
                    "icon": "network-offline"
                },
                {
                    "title": "xx.xx.xx.xx[Gitlab]",
                    "command": "terminator -x bash -c '/usr/bin/sudo /usr/bin/nmap -T5 xx.xx.xx.7;/usr/bin/sleep 2;'",
                    "icon": "network-offline"
                },
                {
                    "title": "xx.xx.xx.8[jira]",
                    "command": "terminator -x bash -c '/usr/bin/sudo /usr/bin/nmap -T5 xx.xx.xx.8;/usr/bin/sleep 2;'",
                    "icon": "network-offline"
                },
                {
                    "title": "xx.xx.xx.xx[Share]",
                    "command": "terminator -x bash -c '/usr/bin/sudo /usr/bin/nmap -T5 xx.xx.xx.22;/usr/bin/sleep 2;'",
                    "icon": "network-offline"
                },
                {
                    "title": "xx.xx.xx.xx[Share]",
                    "command": "terminator -x bash -c '/usr/bin/sudo /usr/bin/nmap -T5 xx.xx.xx.124;/usr/bin/sleep 2;'",
                    "icon": "network-offline"
                },
                {
                    "title": "xx.xx.xx.xx[Chat]",
                    "command": "terminator -x bash -c '/usr/bin/sudo /usr/bin/nmap -T5 192.168.10.155;/usr/bin/sleep 2;'",
                    "icon": "network-offline"
                }
            ]
        },
        {
            "title": "SSH",
            "type": "submenu",
            "submenu": [
                {
                    "title": "xx.xx.xx.xx(General)",
                    "command": "terminator -x bash -c 'ssh user@xx.xx.xx.2; exec bash'",
                    "icon": "utilities-terminal"
                },
                {
                    "title": "xx.xx.xx.xx(Email)",
                    "command": "terminator -x bash -c 'ssh user@xx.xx.xx.5; exec bash'",
                    "icon": "utilities-terminal"
                },
                {
                    "title": "xx.xx.xx.xx[Gitlab]",
                    "command": "terminator -x bash -c 'ssh user@xx.xx.xx.7; exec bash'",
                    "icon": "utilities-terminal"
                },
                {
                    "title": "xx.xx.xx.xx[jira]",
                    "command": "terminator -x bash -c 'ssh user@xx.xx.xx.8; exec bash'",
                    "icon": "utilities-terminal"
                }
            ]
        }
    ]
}
```