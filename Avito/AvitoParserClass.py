from .AvitoBaseClass import *


class AvitoParserClass(AvitoBaseClass):
    """класс расширение базового класса AvitoParser, красиво все выводит"""

    def __init__(self, path: str) -> None:
        super().__init__(path)

    """получаем все информацию из объявления"""

    def get_full_info(self) -> dict:
        res = {
            "item-navigation": self.get_css_class("item-navigation"),
            "title": self.get_css_class("title-info-title-text"),
            "metadata": self.get_css_class("title-info-metadata-item-redesign"),
            "price": self.get_css_class("price-value-main"),
            "seller name": self.get_css_class("seller-info-name js-seller-info-name"),
            "seller label": self.get_marker("seller-info/label"),
            "item-params": self.get_css_class("item-params"),
            "item-address__string": self.get_css_class("item-address__string"),
            "item-description": self.get_css_class("item-description"),
            "advanced-params": self.get_css_class("advanced-params-param"),
            "link": self.get_link2seller(),
            "gallery-img-frame": self.get_gallery_img_frame(),
        }
        if self.get_image():
            res["list photo"] = self.get_image()
        return res
