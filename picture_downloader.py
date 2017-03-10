import re
import urllib
import urllib2

class downloader():
    def download_web(self,url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()

    def download_file(self,url):
        print 'picture url:',url
        fileName = re.search(r'[a-zA-Z0-9]+\.jpg',url)
        print 'fileName:',fileName.group()
        urllib.urlretrieve(url,fileName.group())
