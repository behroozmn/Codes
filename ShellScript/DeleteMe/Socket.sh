
# Send
echo "behrooz"| socat - TCP4:127.0.0.1:1234
echo "behrooz"| socat -  TCP:127.0.0.1:1234
echo "behrooz"| socat -  TCP:127.0.0.1:1234




# Listen.Recieve
socat -  TCP-LISTEN:1234,reuseaddr,fork
socat - TCP4-LISTEN:1234,reuseaddr,fork
socat    TCP-LISTEN:1234,reuseaddr,fork   EXEC:"/tmp/salam/myscript.sh"
socat   tcp-l:1234,reuseaddr,fork system:'cat >> /tmp/log.txt',nofork
socat - TCP-LISTEN:1234,reuseaddr,fork |tee -a /tmp/log.txt #سوکت TIME_WAIT بوجود میآورد و بعد از یک دقیقه آن را می‌بندد