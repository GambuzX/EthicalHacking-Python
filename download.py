#!/usr/bin/env python

import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download("https://cdn.shopify.com/s/files/1/1190/6156/products/Some_Guy_On_A_Potato_1024x1024.jpg?v=1492707440")