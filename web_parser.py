import re

from bs4 import BeautifulSoup


class webParser():

    def get_soup_urls(self,soup):
        pic_urls = set()
        urls = soup.find_all('img',class_='BDE_Image',src=re.compile(r'[a-zA-Z0-9]+\.jpg'))
        for i in urls:
            print i.get('src')
            pic_urls.add(i.get('src'))
        return pic_urls

    def parser(self,content):
        if content is None:
            return

        soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')
        pic_urls = self.get_soup_urls(soup)

        return pic_urls
