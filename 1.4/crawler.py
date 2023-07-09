import urllib.request
from bs4 import BeautifulSoup
import ssl
import re
import sys
import os


class Crawler:
    def __init__(self):
        self.url = "https://sport050.nl/sportaanbieders/alle-aanbieders/"
        self.ctx = self.hack_ssl()

    @staticmethod
    def hack_ssl():
        """
        Ignore certificate errors.
        Returns:
            ssl.SSLContext: SSL context with certificate verification disabled.
        """
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    @staticmethod
    def remove_html_tags(text):
        """
        Remove HTML tags from a string.
        Args:
            text (str): Input string containing HTML tags.

        Returns:
            str: Cleaned string with HTML tags removed.
        """
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def open_url(self, url):
        """
        Reads the URL file as a big string and cleans the HTML file to make it more readable.

        Args:
            url (str): URL of the webpage to open.

        Returns:
            bs4.BeautifulSoup: Soup object representing the parsed HTML content.
        """
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def read_hrefs(self, soup):
        """
        Get a list of anchor tags from the soup object and return their href keys.

        Args:
            soup (bs4.BeautifulSoup): Soup object representing the parsed HTML content.

        Returns:
            list: List of href values from anchor tags.
        """
        reflist = []
        tags = soup('a')
        for tag in tags:
            reflist.append(tag)
        return reflist

    def read_li(self, soup):
        """
        Get a list of li tags from the soup object and return them.

        Args:
            soup (bs4.BeautifulSoup): Soup object representing the parsed HTML content.

        Returns:
            list: List of li tags.
        """
        lilist = []
        tags = soup('li')
        for tag in tags:
            lilist.append(tag)
        return lilist

    def get_phone(self, info):
        """
        Get the phone number from the provided info list.

        Args:
            info (list): List of li tags containing information.

        Returns:
            str: Extracted phone number.
        """
        reg = r"(?:(?:00|\+)?[0-9]{4})?(?:[ .-][0-9]{3}){1,5}"
        phone = [s for s in info if 'Telefoon' in str(s)]
        try:
            phone = str(phone[0])
        except IndexError:
            phone = [s for s in info if re.findall(reg, str(s))]
            try:
                phone = str(phone[0])
            except IndexError:
                phone = ""
        return self.remove_html_tags(phone).replace('Facebook', '').replace('Telefoon:', '')

    def get_email(self, soup):
        """
        Get the email address from the provided soup object.

        Args:
            soup (bs4.BeautifulSoup): Soup object representing the parsed HTML content.

        Returns:
            str: Extracted email address.
        """
        try:
            email = [s for s in filter(lambda x: '@' in str(x), soup)]
            email = str(email[0])[4:-5]
            bs = BeautifulSoup(email, features="html.parser")
            email_tag = bs.find('a')
            if email_tag:
                email = email_tag.attrs['href'].replace('mailto:', '')
            else:
                email = ""
        except:
            email = ""
        return self.remove_html_tags(email).replace("/", "")
    
    def fetch_sidebar(self, soup):
        """
        Extracts the sidebar from the provided soup object.

        Args:
            soup (bs4.BeautifulSoup): Soup object representing the parsed HTML content.

        Returns:
            bs4.element.Tag: Sidebar element.
        """
        sidebar = soup.findAll(attrs={'class': 'sidebar'})
        return sidebar[0]
    
    def extract(self, url):
        """
        Extracts the relevant portion of the URL.

        Args:
            url (str): URL string.

        Returns:
            str: Extracted portion of the URL.
        """
        text = str(url)
        text = text[26:].split('"')[0] + "/"
        return text
    
    def crawl_site(self):
        """
        Crawls the website and extracts information from sub-urls.

        This method performs the crawling process by iterating over the sub-urls and extracting relevant information such as
        phone numbers and email addresses. The extracted data is then written to an output file.

        """
        output_path = 'output.txt'
        output_location = os.path.abspath(output_path)
        print(f'Output Location: {output_location}')
        print('fetch urls')
        soup = self.open_url(self.url)
        reflist = self.read_hrefs(soup)

        print('getting sub-urls')
        sub_urls = [s for s in reflist if '<a href="/sportaanbieders' in str(s)]
        sub_urls = sub_urls[3:]

        print('extracting the data')
        print(f'{len(sub_urls)} sub-urls')

        try:
            with open(output_path, 'w') as f:
                iterator = iter(sub_urls)

                while True:
                    try:
                        sub = next(iterator)
                        sub = self.extract(sub)
                        site = self.url[:-16] + sub
                        soup = self.open_url(site)
                        info = self.fetch_sidebar(soup)
                        info = self.read_li(info)
                        phone = self.get_phone(info)
                        phone = self.remove_html_tags(phone).strip()
                        email = self.get_email(info)
                        email = self.remove_html_tags(email).replace("/", "")
                        output = f'{site} ; {phone} ; {email}'
                        print(output)
                        f.write(output + '\n')
                    except StopIteration:
                        break
                    except Exception as e:
                        print(e)
                        raise
        except KeyboardInterrupt:
            print('Program stopped by user')
            sys.exit()
