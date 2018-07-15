#!/usr/bin/env python

import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="ip_range", help="Target IP range to scan for devices.")
    options = parser.parse_args()
    if not options.ip_range:
        parser.error("[-] Please specify an IP range. Use --help for more info.")
    return options.ip_range


def scan(ip):
    # create a packet with desired ip range
    arp_request = scapy.ARP(pdst=ip)

    # create an Internet frame to broadcast packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # concatenate the 2 packets
    arp_request_broadcast = broadcast/arp_request

    # send and receive packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # create a list of dictionaries of all ips and macs found
    clients_list = []
    for element in answered_list:
        clients_list.append({"ip": element[1].psrc, "mac": element[1].hwsrc})

    return clients_list


def print_result(results):
    print("IP\t\t\tMAC Address\n--------------------------------------------")
    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])


ip = get_arguments()
scan_result = scan(ip)
print_result(scan_result)
