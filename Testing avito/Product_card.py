import time
import random
from Avito import AvitoParserClass

URL = ["https://www.avito.ru/moskva/nedvizhimost_za_rubezhom/kvartira_turtsiya_2292081161",
       "https://www.avito.ru/ekaterinburg/zapchasti_i_aksessuary/bamper_peredniy_mersedes_amg_6.3_dlya_s350500_w221_1564428767",
       "https://www.avito.ru/ivanovo/gruzoviki_i_spetstehnika/katok_dorozhnyy_gruntovyy_ammann_asc150d_2249486154",
       "https://www.avito.ru/nizhniy_novgorod/gruzoviki_i_spetstehnika/gaz_next_2017_2193606937",
       "https://www.avito.ru/ivanovo/gruzoviki_i_spetstehnika/shacman_shaanxi_sx3258dr385_2019_2281051227",
       "https://www.avito.ru/nizhniy_novgorod/tovary_dlya_kompyutera/modemy_i_routery_2285576961",
       "https://www.avito.ru/nizhniy_novgorod/planshety_i_elektronnye_knigi/planshet_s_sim-kartoy_bq_bq-7082g_2287001501",
       "https://www.avito.ru/nizhniy_novgorod/audio_i_video/tv_box_ugoos_x4_4k_android_11_podgotovka_2223460371",
       "https://www.avito.ru/nizhniy_novgorod/audio_i_video/domashniy_kinoteatr_lg_2303171616",
       "https://www.avito.ru/nizhniy_novgorod/audio_i_video/videoproigryvatel_samsung_1913284325",
       'https://www.avito.ru/nizhniy_novgorod/noutbuki/apple_macbook_pro_13_2019_2287457227',
       "https://www.avito.ru/nizhniy_novgorod/audio_i_video/cd_mihail_shufutinskiy._dobryy_vecher_gospoda_2294437993",
       "https://www.avito.ru/nizhniy_novgorod/noutbuki/igrovoy_17.3_acer_nitro_c_rtx_3060_na_6_yadrah_2251145752",
       "https://www.avito.ru/nizhniy_novgorod/noutbuki/noutbuk_lenovo-g580-model_n_20150_1954197157",
       "https://www.avito.ru/nizhniy_novgorod/planshety_i_elektronnye_knigi/ipad_2019_128gb_2314845379",
       "https://www.avito.ru/nizhniy_novgorod/tovary_dlya_kompyutera/rtx_3080ti_gainward_2281496631",
       "https://www.avito.ru/nizhniy_novgorod/koshki/plyushevye_pozitivchiki_1885719691"
       ]

# вывод карточки товара
for url in URL:
    outputdata = AvitoParserClass(path=url).get_full_info()
    print("\n\n", outputdata)
    time.sleep(random.randint(3, 7))
