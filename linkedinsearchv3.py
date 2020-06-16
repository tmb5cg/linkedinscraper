# Adapted from bingscraper package, src: https://pypi.org/project/bingscraper/

import os
import requests as re
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import time
import random

class scrape:
    def __init__(self, term):
        self.search_term = term
        self.dir_name = self.search_term.replace(" ", "_").lower()
        #if not os.path.isdir(self.dir_name):
        #    os.makedirs(self.dir_name)
    def getSearch(self):
        return self.search_term
    def getDir(self):
        return self.dir_name

    def GET_UA():
        uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                    ]
        return random.choice(uastrings)

    def text(self):
        param = {"q": self.getSearch()}
        try:
            rt = re.get("https://www.bing.com/search", params = param)
            soupt = BeautifulSoup(rt.text, "html.parser")
        except:
            print("Internet Disconnected. Connect to download text.")

        results = soupt.find("ol", {"id":"b_results"})
        lists = results.findAll("li", {"class":"b_algo"})
        file = open("./results/people.txt", 'a')
        file.close()

        firstresult = lists[0]

        item_text = firstresult.find("a").text
        item_href = firstresult.find("a").attrs["href"]

        if item_text and item_href:
            if "linkedin.com/in/" in str(item_href):
                print("LINKEDIN FOUND")

                print(item_text + "\n" + item_href + "\n")
                file = open("./results/people.txt", 'a')
                file.write(item_text + "\n" + item_href + "\n\n")
                file.close()
            else:
                print("Linkedin not found")
                file = open("./results/people.txt", 'a')
                file.write(str(self.getSearch()) + " NOT FOUND IN FIRST RESULT" + "\n" + item_href + "\n\n")
                file.close()

        # for item in lists:
        #     item_text = item.find("a").text
        #     item_href = item.find("a").attrs["href"]
        #     if item_text and item_href:
        #
        #         if "linkedin.com/in/" in str(item_href):
        #             print("yeifjs")
        #
        #         #else:
        #
        #
        #         print(item_text + "\n" + item_href + "\n")
        #         file = open("./"+ self.getDir() + "/" + self.getSearch() +".txt", 'a')
        #         file.write(item_text + "\n" + item_href + "\n\n")
        #         file.close()


# Master.txt includes names and position
qbfile = open("./results/master.txt", "r")

for aline in qbfile:

    # Delay to not get flagged
    delay = random.randint(3,20)
    time.sleep(delay)
    query = str(aline)
    scrape(query).text() #For Text Scraping.
    print(query)
