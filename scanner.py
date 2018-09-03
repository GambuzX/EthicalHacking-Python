#!/usr/bin/env python

import requests, re, urlparse


class Scanner:
    def __init__(self, url, links_to_ignore):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = links_to_ignore

    def extract_links_from(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url=None):
        if url is None:
            url = self.target_url

        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
                self.target_links.append(link)
                print(link)
                self.crawl(link)
