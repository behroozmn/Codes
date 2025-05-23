# IP Commands

* show
    * ip a
    * ip addr show
    * ip -s link #network statistics
    * ip -4 a #Only show TCP/IP IPv4
    * ip -6 a #Only show TCP/IP IPv6
    * ip a list eth0 #Only show eth0 interface
    * ip a show dev eth0 #Only show eth0 interface
    * ip a show eth0 #Only show eth0 interface
    * ip addr #Show information for all addresses
    * ip addr help #Display address commands and arguments
    * ip addr show dev eth0 #Display information only for device
* link
    * ip link set <NIC> up|down
    * ip link #show information for all interfaces
    * ip link show dev eth0 #Display information only for device eth0
    * ip link set eth0 promisc on #Enable promiscuous mode for eth0
    * ip link ls up #Only show running interfaces
    * ip -s link #Display interface statistics
    * ip -s link ls eth0 #get information about a particular network interface
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
      →