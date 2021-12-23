from Avito import *

url = "https://www.avito.ru/cheboksary/avtomobili/porsche_cayenne_2014_2190119414"
outputdata = AvitoFull(url).get_full_info()
for item in outputdata.items():
    print(item)
