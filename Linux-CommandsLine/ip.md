

# IP Commands

* show
  * ip a
  * ip addr show
  * ip -s link #network statistics
* edit
  * ip link set <NIC> up|down 
* add
  * ip addr add x.x.x.x/Y dev <NIC> → Add IP
* remove
  * ip addr del x.x.x.x/Y dev <NIC> → del IP
  * ip link del <nic> down → up/down NIC


# [Gateway|Routr] Commands

* show
  * ip route
  * ip route show #default gateway information
* add
  * ip route add default via 192.168.200.1/24 #assign a default gateway
* remove
  * ip route del 192.168.0.150/24 #Removing a static route
