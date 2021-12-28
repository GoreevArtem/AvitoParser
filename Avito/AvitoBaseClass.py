from __future__ import annotations
import re
from typing import List, Any
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import validators
from fake_useragent import UserAgent


class AvitoBaseClass:
    "базовый класс парсера авито"

    def __init__(self, path: str) -> None:
        if not validators.url(path):
            raise ValueError("incorrect url input")
        else:
            try:
                html = requests.get(path, headers={'User-Agent': UserAgent().chrome})
                html.raise_for_status()
                self.__root = BeautifulSoup(html.text, features="html.parser")
            except HTTPError as http_error:
                # print(f"HTTP error occurred: {http_error}")
                raise http_error
            except Exception as error:
                # print(f"Other error occurred: {error}")
                raise error

    # параметр - css класс, вывод - текст
    def get_css_class(self, attr: str) -> str | None:
        try:
            return re.sub("^\s+|\n|\r|\s+$", '', self.__root.find(class_=attr).text).replace(u'\xa0', u'').replace("\t", " ")
        except:
            return None

    # получаем url на фото
    def get_image(self) -> List[Any] | None:
        try:
            return [item["src"] for item in self.__root.find_all('img') if item.has_attr('alt')][0:-6]
        except:
            return None

    # получаем главную картинку, которая представлена в объявлении
    def get_gallery_img_frame(self) -> str | None:
        try:
            return self.__root.find("div", class_="gallery-img-frame js-gallery-img-frame")["data-url"]
        except:
            return None

    # получаем ссылку на продавца
    def get_link2seller(self) -> str | None:
        try:
            path = self.__root.find('div', attrs={'class': 'seller-info-name js-seller-info-name'}).findChild("a")[
                "href"]
            if bool(path.find("https://www.avito.ru")):
                return "https://www.avito.ru" + path
            else:
                return path
        except:
            return None

    def get_marker(self, data):
        try:
            return self.__root.find("div", {"data-marker": data}).text
        except:
            return None
