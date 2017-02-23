#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
import urllib2
import bs4


class Client(object):

    def __init__(self):
        super(Client,self).__init__()

    def get_web_page(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def parse_web_page(self, html):
        """
        Parses an html page searching for the agenda
        """
        book = []
        soup = bs4.BeautifulSoup(html, "lxml")
        book = soup.find_all("div", "dotd-title")
        bookContents = book[0].contents
        finalList = str(bookContents[1]).split()
        stringBook = ""
        for i in finalList:
            if i != "<h2>" and i != "</h2>":
                stringBook += str(i) + " "

        return stringBook


    def get_book(self):

        html = self.get_web_page("https://www.packtpub.com/packt/offers/free-learning/")
        print self.parse_web_page(html)

if __name__ == "__main__":
    client = Client()
    client.get_book()
