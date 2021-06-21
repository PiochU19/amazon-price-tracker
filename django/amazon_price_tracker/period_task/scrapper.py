import requests
from bs4 import BeautifulSoup


class Scrapper:
    """
    Scrapping Product on Amazon by provided link
    using Python built in requests
    and BeutifulSoup from bs4
    """

    def __init__(self, link):

        self.link = link

    def get_page(self):
        """
        Function returns the page
        content based on given product
        name by Python requests
        """

        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"

        session = requests.Session()
        session.headers["User-Agent"] = USER_AGENT
        session.headers["Accept-Language"] = LANGUAGE
        session.headers["Content-Language"] = LANGUAGE

        return session.get(self.link).text

    def get_price(self):
        """
        Return actual price of product
        """

        soup = BeautifulSoup(self.get_page(), "html.parser")

        price = soup.find("span", attrs={"id": "price_inside_buybox"}).getText()

        return float(price[:-3].strip().replace(",", "."))
