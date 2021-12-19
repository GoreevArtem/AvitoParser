import unittest
from Avito import *
import requests
from requests.exceptions import HTTPError
url = "https://www.avito.ru/sevastopol/avtomobili/vaz_2107_1986_2286329373"


class TestAvito(unittest.TestCase):

    def test_init_class(self):
        self.assertRaises(TypeError, AvitoFull(path=url))

    def test_class_method(self):
        self.assertEqual(AvitoFull(path=url).get_image(), [
            'https://23.img.avito.st/image/1/1.wtPGn7a4bjrmPQKGmOmfZHA4aDZyPGQw5j0COHA-bvBx.c7dqYhAOiqdU6MvxDclcbLsPVGQEdoora3lcRjLtba4',
            'https://09.img.avito.st/image/1/1._OUarLa4UAw6DjzMdNuhUqwLVgCuD1oGOg48DqwNUMat.AapizusB56XIdd7trAtACFe6UVkMgUjJDHjkTe_F698',
            'https://13.img.avito.st/image/1/1.-AF2U7a4VOhW8TggGCSltsD0UuTC8F7iVvE46sDyVCLB.7_OhbKtt_YOgvqjOfyp9q30IzbjsiMU2FrnkfKO-n_U',
            'https://16.img.avito.st/image/1/1.9bOovra4WVqIHDWIxsmoBB4ZX1YcHVNQiBw1WB4fWZAf.ry_uDipcTL2ssz9qZCNrhTB82TcMDyXHD7Ns8gfCIBc'])

    def test_link_seller(self):
        self.assertEqual(AvitoFull(path=url).get_link2seller(),
                         'https://www.avito.ru/user/cdff4d706c28c80a47f84edb2cf50165f0155440f7b96c9d85798d5e3e26eaf2/profile?id=2286329373&src=item&page_from=from_item_card&iid=2286329373')

    def test_full_info(self):
        self.assertEqual(AvitoFull(path=url).get_full_info(),
            {'item-navigation': 'Севастополь   ·  …   ·  Автомобили   ·  С пробегом   ·  ВАЗ (LADA)   ·  2107   ·  I (1982—2012)', 'title': 'ВАЗ 2107, 1986', 'metadata': '15 декабря в 01:41', 'price': '10000₽', 'seller name': 'Август Месяц', 'seller label': 'Частное лицо', 'item-params': 'Год выпуска: 1986  Поколение: I (1982—2012)  Пробег: 99999км  Владельцев по ПТС: 3  Состояние: Битый  Модификация: 1.3 MT (64 л.с.)  Объём двигателя: 1.3л  Тип двигателя: Бензин  Коробка передач: Механика  Привод: Задний  Комплектация: Базовая  Тип кузова: Седан  Цвет: Бежевый  Руль: Левый  VIN или номер кузова: 389****21', 'item-address__string': 'Севастополь, ул. Гоголя, 20А', 'item-description': 'Только обмен , на ходу Нет акб, битая в крыло и фару не критично Сеасвополь', 'advanced-params': 'Салон Кожаный руль', 'link': 'https://www.avito.ru/user/cdff4d706c28c80a47f84edb2cf50165f0155440f7b96c9d85798d5e3e26eaf2/profile?id=2286329373&src=item&page_from=from_item_card&iid=2286329373', 'list foto': ['https://23.img.avito.st/image/1/1.wtPGn7a4bjrmPQKGmOmfZHA4aDZyPGQw5j0COHA-bvBx.c7dqYhAOiqdU6MvxDclcbLsPVGQEdoora3lcRjLtba4', 'https://09.img.avito.st/image/1/1._OUarLa4UAw6DjzMdNuhUqwLVgCuD1oGOg48DqwNUMat.AapizusB56XIdd7trAtACFe6UVkMgUjJDHjkTe_F698', 'https://13.img.avito.st/image/1/1.-AF2U7a4VOhW8TggGCSltsD0UuTC8F7iVvE46sDyVCLB.7_OhbKtt_YOgvqjOfyp9q30IzbjsiMU2FrnkfKO-n_U', 'https://16.img.avito.st/image/1/1.9bOovra4WVqIHDWIxsmoBB4ZX1YcHVNQiBw1WB4fWZAf.ry_uDipcTL2ssz9qZCNrhTB82TcMDyXHD7Ns8gfCIBc']}
            )
