#!/usr/bin/env python

import requests, re


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "bing.com"

response = request(target_url)
href_links = re.findall('(?:href=")(.*?)"', response.content)

print(href_links)