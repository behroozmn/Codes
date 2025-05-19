alias ifconfig='/sbin/ifconfig'
alias apt='sudo apt'
alias nmap='sudo nmap'
alias nmapT='sudo nmap -T5'
alias shutdown='sudo shutdown'
alias updatedb='sudo updatedb'
alias vims='sudo vim'
alias kill='sudo kill'
alias killall='sudo killall'
alias bcommentResovle='sudo  sed -i "s/nameserver\ 10.0.20.2/#&/g" /etc/resolv.conf'
alias GitLogBeatifull="git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)' --all"


alias bback="gsettings set org.gnome.desktop.background picture-uri 'file:///home/user/.local/share/backgrounds/background_nature1.jpg'"
alias bbackFake="gsettings set org.gnome.desktop.background picture-uri ''"
alias b_killOutputMessengers='kill -9 $(pidof OutputMessenger)'
alias b_Busy="cat /dev/urandom | hexdump -C | grep --color=auto -E 'aa|bb|cc|dd|ee|ff'"
alias b_GenPasswd="strings /dev/urandom | grep -o '[[:alnum:]]' | head -n 30 | tr -d '\n'; echo"
alias b_ipAll='ip addr list |column -t|grep -E "\." |awk "{print \$2}"'
alias b_ipPublic='curl -s http://ip.jsontest.com|jq .ip|tr -d "\""' #dependency: jq, curl
alias b_ipPublic2='curl -s ifconfig.me'
alias b_logDmesg='sudo dmesg -Tx  --follow'
alias b_mount="mount | column -t"
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias mv='mv -i'
alias cp='cp -i' #prompt before overwrite
alias dir='dir --color=auto'
#alias grep='grep --color=auto'
alias ll="ls --color -al"
alias ls="ls --color=auto"
alias ps?="ps aux | grep"
alias torBehrooz="cd APP/Tor/tor-browser_en-US/Browser/;./start-tor-browser --detach"



b_backup () { _time=$(date +%Y%m%d-%H%M%S) ;  cp "$1"{,.bak_$_time}; }
cls() { cd "$1"; ls;}
mcd() { mkdir -p "$1"; cd "$1";}
b_7z() { 7z -mx9 a data.7z "$1";}


#alias chgrp='chgrp --preserve-root'       # Parenting changing perms on /
#alias chmod='chmod --preserve-root'    # Parenting changing perms on /
#alias chown='chown --preserve-root'    # Parenting changing perms on /
alias rm='rm -I --preserve-root'
alias systemctl='sudo systemctl'


alias b_ScanPort_1-1000_open='nc -vv -z localhost 1-1000 2>&1 | grep open'
alias b_DeleteDirOnTMP='mkdir /tmp/DeletedFiles'
alias b_Chk_Duplicate='fdupes -R .'
alias echoColorize='echo -e "${NOCOLOR}Nocolor ${RED}Red ${GREEN}Green ${ORANGE}Orange ${BLUE}Blue ${PURPLE}Purple ${YELLOW}Yellow ${CYAN}Cyan ${LIGHTGRAY}LightGray ${DARKGRAY}DarkGray ${LIGHTRED}LightRed ${LIGHTGREEN}LightGreen ${LIGHTBLUE}LightBlue ${LIGHTPURPLE}LightPurple ${LIGHTCYAN}LightCyan ${WHITE}White ${NOCOLOR}Nocolor"'


NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'


