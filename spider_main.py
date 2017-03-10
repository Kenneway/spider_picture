from picture_downloader import downloader
from web_parser import webParser

class spiderMain():
    def __init__(self):
        self.downloader = downloader()
        self.parser = webParser()


    def craw(self,url):
        web_content = self.downloader.download_web(url)
        urls = self.parser.parser(web_content)

        for pic_url in urls:
            print 'pic_url:',pic_url
            self.downloader.download_file(pic_url)

        print 'craw success!'



if __name__ == '__main__':
    src_url = 'http://tieba.baidu.com/p/2166231880'

    obj_spider = spiderMain()
    obj_spider.craw(src_url)