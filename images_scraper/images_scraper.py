from selenium import webdriver
from urllib.request import urlretrieve, build_opener, install_opener
from urllib.parse import urlparse, unquote
import time


class ImageParser:
    def __init__(self, url):
        self.url = url
        self.folder = '/path/to/folder/for/downloaded/images/'
        self.driver = webdriver.Chrome('/path/to/chromedriver')
        self.driver.get(self.url)

    def scroller(self):
        # Function for scrolling Google page to load more images

        # Time for pause while page is loading
        scroll_pause_time = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def downloader(self, fin_link):

        # Path for downloaded image
        dest = self.folder + fin_link.rsplit('/', 1)[1]

        # Headers for request
        opener = build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        install_opener(opener)

        try:
            # Function for download
            urlretrieve(fin_link, dest)
        except Exception as e:
            # Print errors if occur
            print(str(e))

    def chromeImageParser(self):

        # Find all <a> tags which contain <img> tag
        a_tag = self.driver.find_elements_by_xpath('//a[img]')

        for a in a_tag:

            # Get href attribute of <a>
            href = a.get_attribute("href")

            if href is None:
                continue

            # Parse href value
            prs = urlparse(href)
            print(prs)
            prs_q = unquote(prs.query)
            
            prs_str_start = "imgurl="
            prs_str_end = "jpg"
            prs_str_alt = "png"

            # Building final link for download full size image
            if prs_str_start and prs_str_end in prs_q:
                fin_link = prs_q.split(prs_str_start)[1].split(prs_str_end)[0] + "jpg"
                print(fin_link)
                IP.downloader(fin_link)

            elif prs_str_start in prs_q and prs_str_end not in prs_q:
                if prs_str_alt in prs_q:
                    fin_link = prs_q.split(prs_str_start)[1].split(prs_str_alt)[0] + "png"
                    print(fin_link)
                    IP.downloader(fin_link)
                else:
                    fin_link = prs_q.split(prs_str_start)[1].split("&")[0] + ".jpg"
                    print(fin_link)
                    IP.downloader(fin_link)


if __name__=='__main__':
    IP = ImageParser("paste-here-link-from-google")
    IP.scroller()
    IP.chromeImageParser()
