#!/usr/bin/env python

import scapy.all as scapy

def get_mac(ip):
    # create a packet with desired ip range
    arp_request = scapy.ARP(pdst=ip)

    # create an Internet frame to broadcast packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # concatenate the 2 packets
    arp_request_broadcast = broadcast/arp_request

    # send and receive packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # return mac address of target ip
    return answered_list[0][1].hwsrc


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print("[+] You are under attack!")
        except IndexError:
            pass


sniff("eth0")