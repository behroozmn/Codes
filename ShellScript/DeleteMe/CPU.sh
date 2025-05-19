#processor architecture (i.e. x86_64)
CPUArch=$(lscpu | grep 'Architecture' |awk '{print $2}' | head -n 1)
echo "${CPUArch}"


#Processors Count
cores=$(lscpu | grep 'CPU(s)' |awk '{print $2}' | head -n 1)


#processor model name (i.e. Intel(R) Core(TM) i5-5200U CPU @ 2.20GHz)
cpuModel=$(lscpu | grep 'Model name' |cut -d ' ' -f 3- | sed -e 's/^[[:space:]]*//')


#OS processor type (i.e. x86_64)
cpuType=$(uname -p)