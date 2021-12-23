import unittest
from Avito import AvitoFull, CategoriesUrl
import requests
from requests.exceptions import HTTPError

url = "https://www.avito.ru/sevastopol/avtomobili/vaz_2107_1986_2286329373"


class TestAvito(unittest.TestCase):

    def test_init_class(self):
        self.assertRaises(TypeError, AvitoFull(path=url))
        self.assertRaises(Exception, AvitoFull(path=url))

    def test_class_method(self):
        self.assertEqual(AvitoFull(path=url).get_image(), [
            'https://23.img.avito.st/image/1/1.wtPGn7a4bjrmPQKGmOmfZHA4aDZyPGQw5j0COHA-bvBx.c7dqYhAOiqdU6MvxDclcbLsPVGQEdoora3lcRjLtba4',
            'https://09.img.avito.st/image/1/1._OUarLa4UAw6DjzMdNuhUqwLVgCuD1oGOg48DqwNUMat.AapizusB56XIdd7trAtACFe6UVkMgUjJDHjkTe_F698',
            'https://13.img.avito.st/image/1/1.-AF2U7a4VOhW8TggGCSltsD0UuTC8F7iVvE46sDyVCLB.7_OhbKtt_YOgvqjOfyp9q30IzbjsiMU2FrnkfKO-n_U',
            'https://16.img.avito.st/image/1/1.9bOovra4WVqIHDWIxsmoBB4ZX1YcHVNQiBw1WB4fWZAf.ry_uDipcTL2ssz9qZCNrhTB82TcMDyXHD7Ns8gfCIBc'])

    @unittest.skip
    def test_link_seller(self):
        self.assertEqual(AvitoFull(path=url).get_link2seller(),
                         'https://www.avito.ru/user/cdff4d706c28c80a47f84edb2cf50165f0155440f7b96c9d85798d5e3e26eaf2/profile?id=2286329373&src=item&page_from=from_item_card&iid=2286329373')

    @unittest.skip
    def test_full_info(self):
        self.assertEqual(AvitoFull(path=url).get_full_info(),
                         {
                             'item-navigation': 'Севастополь   ·  …   ·  Автомобили   ·  С пробегом   ·  ВАЗ (LADA)   ·  2107   ·  I (1982—2012)',
                             'title': 'ВАЗ 2107, 1986', 'metadata': '15 декабря в 01:41', 'price': '10000₽',
                             'seller name': 'Август Месяц', 'seller label': 'Частное лицо',
                             'item-params': 'Год выпуска: 1986  Поколение: I (1982—2012)  Пробег: 99999км  Владельцев по ПТС: 3  Состояние: Битый  Модификация: 1.3 MT (64 л.с.)  Объём двигателя: 1.3л  Тип двигателя: Бензин  Коробка передач: Механика  Привод: Задний  Комплектация: Базовая  Тип кузова: Седан  Цвет: Бежевый  Руль: Левый  VIN или номер кузова: 389****21',
                             'item-address__string': 'Севастополь, ул. Гоголя, 20А',
                             'item-description': 'Только обмен , на ходу Нет акб, битая в крыло и фару не критично Сеасвополь',
                             'advanced-params': 'Салон Кожаный руль',
                             'link': 'https://www.avito.ru/user/cdff4d706c28c80a47f84edb2cf50165f0155440f7b96c9d85798d5e3e26eaf2/profile?id=2286329373&src=item&page_from=from_item_card&iid=2286329373',
                             'list photo': [
                                 'https://23.img.avito.st/image/1/1.wtPGn7a4bjrmPQKGmOmfZHA4aDZyPGQw5j0COHA-bvBx.c7dqYhAOiqdU6MvxDclcbLsPVGQEdoora3lcRjLtba4',
                                 'https://09.img.avito.st/image/1/1._OUarLa4UAw6DjzMdNuhUqwLVgCuD1oGOg48DqwNUMat.AapizusB56XIdd7trAtACFe6UVkMgUjJDHjkTe_F698',
                                 'https://13.img.avito.st/image/1/1.-AF2U7a4VOhW8TggGCSltsD0UuTC8F7iVvE46sDyVCLB.7_OhbKtt_YOgvqjOfyp9q30IzbjsiMU2FrnkfKO-n_U',
                                 'https://16.img.avito.st/image/1/1.9bOovra4WVqIHDWIxsmoBB4ZX1YcHVNQiBw1WB4fWZAf.ry_uDipcTL2ssz9qZCNrhTB82TcMDyXHD7Ns8gfCIBc']}
                         )


class TestCategoriesUrl(unittest.TestCase):
    city = "nizhniy_novgorod"
    category = "avtomobili"
    url = "https://www.avito.ru/" + city + "/" + category

    def test_init_class(self):
        self.assertRaises(TypeError, CategoriesUrl(path=self.url))
        self.assertRaises(Exception, CategoriesUrl(path=self.url))

    def test_count_pages(self):
        self.assertEqual(CategoriesUrl(path=self.url).count_pages(), 100)

    @unittest.skip
    def test_get_url_of_ads(self):
        self.assertEqual(CategoriesUrl(path=self.url).get_url_of_ads(), {
            1: ['https://www.avito.ru/ivanovskaya_oblast_shuya/avtomobili/renault_logan_2012_2291716437',
                'https://www.avito.ru/gorodets/avtomobili/gaz_31105_volga_2005_2299115693',
                'https://www.avito.ru/kovrov/avtomobili/lexus_nx_2015_2278931504',
                'https://www.avito.ru/uren/avtomobili/chevrolet_lacetti_2009_2247083614',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/chery_tiggo_7_pro_2021_2255715803',
                'https://www.avito.ru/uren/avtomobili/lada_granta_2016_2279026279',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/geely_emgrand_ec7_2014_2289117250',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/volkswagen_polo_2017_2275226258',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/renault_kaptur_2021_2138249288',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/renault_duster_2021_2221810394',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/renault_kaptur_2021_2106729819',
                'https://www.avito.ru/uren/avtomobili/lada_priora_2016_2279727246',
                'https://www.avito.ru/dzerzhinsk/avtomobili/suzuki_grand_vitara_2010_2286059320',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/renault_arkana_2021_2138620314',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/peugeot_4008_2012_2314437339',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/lada_xray_cross_2021_2322881437',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/suzuki_sx4_2018_2279395968',
                'https://www.avito.ru/uren/avtomobili/hyundai_accent_2005_2215432809',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/chevrolet_aveo_2011_2296707192',
                'https://www.avito.ru/kstovo/avtomobili/toyota_land_cruiser_prado_2012_2284063556',
                'https://www.avito.ru/uren/avtomobili/hyundai_accent_2008_2247275247',
                'https://www.avito.ru/cheboksary/avtomobili/hyundai_solaris_2019_2259747270',
                'https://www.avito.ru/uren/avtomobili/geely_mk_2014_2279020142',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/kia_rio_2016_2295987609',
                'https://www.avito.ru/uren/avtomobili/lada_priora_2012_2215243896',
                'https://www.avito.ru/uren/avtomobili/chevrolet_aveo_2011_2214945399',
                'https://www.avito.ru/kineshma/avtomobili/renault_logan_2008_2280400738',
                'https://www.avito.ru/uren/avtomobili/volkswagen_passat_1994_2247001746',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/lada_xray_2021_2291157929',
                'https://www.avito.ru/moskva/avtomobili/kia_ceed_2015_2313960245',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/kia_soul_2021_2273876710',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/gaz_gazel_3302_2011_2278695643',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/nissan_qashqai_2021_2219334743',
                'https://www.avito.ru/uren/avtomobili/uaz_3962_2000_2183500202',
                'https://www.avito.ru/kazan/avtomobili/audi_q3_2015_2273172426',
                'https://www.avito.ru/uren/avtomobili/hyundai_matrix_2008_2279815811',
                'https://www.avito.ru/cheboksary/avtomobili/volkswagen_polo_2016_2246373068',
                'https://www.avito.ru/vorsma/avtomobili/volkswagen_amarok_2019_2217114031',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/hyundai_elantra_2004_2290728989',
                'https://www.avito.ru/doschatoe/avtomobili/vaz_2107_2002_2270328804',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/gaz_gazel_next_2017_2285799553',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/hyundai_creta_2021_2276604576',
                'https://www.avito.ru/sarov/avtomobili/daewoo_nexia_2010_2299379496',
                'https://www.avito.ru/uren/avtomobili/volkswagen_jetta_2014_2121530985',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/mercedes-benz_e-klass_2021_2255607271',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/hyundai_palisade_2021_2294013656',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/kia_rio_2021_2193114190',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/mazda_cx-5_2017_2279298517',
                'https://www.avito.ru/moskva/avtomobili/mercedes-benz_cla-klass_2013_2314530494',
                'https://www.avito.ru/uren/avtomobili/toyota_avensis_2002_2278945846',
                'https://www.avito.ru/murom/avtomobili/ford_focus_2013_2272229702',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/hyundai_solaris_2021_2276046763',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/renault_duster_2021_2153577598',
                'https://www.avito.ru/dzerzhinsk/avtomobili/toyota_camry_2012_2295747369',
                'https://www.avito.ru/arzamas/avtomobili/vaz_2115_samara_2010_2321280670',
                'https://www.avito.ru/nizhniy_novgorod/avtomobili/renault_arkana_2021_2217115883']})