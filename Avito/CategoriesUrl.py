from __future__ import annotations
import validators
import requests
import time
import random
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent


class CategoriesUrl:
    "класс для получения url со страниц по категорям"
    def __init__(self, path: str) -> None:
        self.path = path
        if not validators.url(self.path):
            raise ValueError("incorrect url input")
        else:
            try:
                html = requests.get(self.path, headers={'User-Agent': UserAgent().chrome})
                html.raise_for_status()
                self.__root = BeautifulSoup(html.text, features="html.parser")
            except HTTPError as http_error:
                print(f"HTTP error occurred: {http_error}")
            except Exception as error:
                print(f"Other error occurred: {error}")

    def count_pages(self) -> int:
        pagination = self.__root.find("div", {"data-marker": "pagination-button"})
        return int(re.split('\D+', str(pagination))[-2])

    def get_url_of_ads(self, pages: int = 1) -> dict | None:
        try:
            sheets = dict()
            for page in range(1, pages + 1):
                url = self.path + "?p=" + str(page)
                response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
                print(f'[PAGE] {url}')
                code = BeautifulSoup(response.content, features="html.parser")

                sheets[page] = ["https://www.avito.ru" + item["href"] for item in
                                code.find_all("a", {'data-marker': "item-title"})]

                if page == pages:
                    break

                value = random.random()
                scaled_value = 1 + (value * (9 - 5))
                print(f'[TIME] {scaled_value}')
                time.sleep(scaled_value)

            return sheets
        except:
            return None