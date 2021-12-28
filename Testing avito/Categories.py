import time
import random
from Avito import CategoriesUrl

URL = [
    "https://www.avito.ru/nizhniy_novgorod/transport?cd=1",
    "https://www.avito.ru/nizhniy_novgorod/nedvizhimost?cd=1",
    "https://www.avito.ru/nizhniy_novgorod/kvartiry?cd=1",
    "https://www.avito.ru/nizhniy_novgorod/rabota?cd=1",
    "https://www.avito.ru/nizhniy_novgorod/predlozheniya_uslug?cd=1",
    "https://www.avito.ru/nizhniy_novgorod/lichnye_veschi?cd=1",
    "https://www.avito.ru/nizhniy_novgorod/dlya_doma_i_dachi?cd=1&localPriority=0",
    "https://www.avito.ru/nizhniy_novgorod/zapchasti_i_aksessuary?cd=1&localPriority=0",
    "https://www.avito.ru/nizhniy_novgorod/bytovaya_elektronika?cd=1&localPriority=0",
    "https://www.avito.ru/nizhniy_novgorod/hobbi_i_otdyh?cd=1&localPriority=0",
    "https://www.avito.ru/nizhniy_novgorod/zhivotnye?cd=1&localPriority=0",
    "https://www.avito.ru/nizhniy_novgorod/dlya_biznesa?cd=1&localPriority=0"
]

# вывод в терминал все url с первой страницы каждой категории,
# без подкатигорий (их просто дофига, а это просто пример для наглядности, не более)
for url in URL:
    get_info_by_category = CategoriesUrl(path=url)
    print(get_info_by_category.get_url_of_ads())
    time.sleep(random.randint(15, 25))
