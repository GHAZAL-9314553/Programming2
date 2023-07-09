
from crawler import Crawler
import sys 

def main():
    crawler = Crawler()
    try:
        crawler.crawl_site()
    except KeyboardInterrupt:
        print('Program stopped by user')
        sys.exit()

if __name__ == "__main__":
    main()