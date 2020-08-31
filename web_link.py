import requests
import re, sys
from urllib.parse import urljoin
import argparse
from colorama import Fore

WHITE = Fore.WHITE

def get_arguments():
    parser = argparse.ArgumentParser(description="Website href links")
    parser.add_argument('-u' , '--url' , nargs='?' , dest='url' , help= "Website, example: https://www.google.com" , required=True)
    args = parser.parse_args()
    return args



class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.links = []

    def get_links(self, url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.text)

    links = []
    def process(self, url = None) :
        try :
            if url == None :
                url = self.target_url
            href_links = self.get_links(url)
            for link in href_links :

                link = urljoin(url, link)

                if '#' in link :
                    link = link.split('#')[0]

                if self.target_url in link and link not in self.links :
                    self.links.append(link)
                    print(f'{WHITE}{link}')
                    self.process(link)

        except :

            pass


result = get_arguments()

scan = Scanner(result.url)
scan.process()
