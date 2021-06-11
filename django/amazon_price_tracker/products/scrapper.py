import requests
from bs4 import BeautifulSoup


class Scrapper:
    """
    Scrapping Amazon Page by
    using Python built in requests
    and BeautifulSoup from bs4
    """

    def __init__(self, product_name):

        self.product_name = product_name

    def get_page(self):
        """
        Function returns the page
        content based on given product
        name by Python requests
        """

        product = self.product_name.replace(" ", "+")

        URL = f"https://www.amazon.pl/s?k={product}"
        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"

        session = requests.Session()
        session.headers["User-Agent"] = USER_AGENT
        session.headers["Accept-Language"] = LANGUAGE
        session.headers["Content-Language"] = LANGUAGE

        return session.get(URL).text

    def get_products(self):
        """
        Gets page content from 'get_page'
        function and returns page elements
        with products within
        """

        while True:
            soup = BeautifulSoup(
                self.get_page(),
                "html.parser",
            )
            not_found = soup.find(
                "span",
                attrs={"class": "a-size-medium a-color-base"},
            )

            if not_found is not None:
                return None

            product_divs = soup.find_all(
                "div",
                attrs={
                    "class": "sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"
                },
            )

            if len(product_divs) > 0:
                break

        return product_divs

    def get_list_of_products(self):
        """
        Gets products page elements
        and returns list of all products
        """

        products = self.get_products()
        if products is not None:
            list_of_products = []
            for product in products:
                try:
                    link = product.find(
                        "a", attrs={"class": "a-link-normal a-text-normal"}
                    )["href"]

                    link = "https://www.amazon.pl" + link

                    name = product.find(
                        "span",
                        attrs={"class": "a-size-base-plus a-color-base a-text-normal"},
                    ).text

                    image = product.find("img", attrs={"class": "s-image"})["src"]

                    price_whole = product.find(
                        "span", attrs={"class": "a-price-whole"}
                    ).text[:-1]

                    price_fraction = product.find(
                        "span", attrs={"class": "a-price-fraction"}
                    ).text

                    price = float(f"{price_whole}.{price_fraction}")
                    list_of_products.append([name, image, price, link])
                except:
                    pass

            return list_of_products

        return None
