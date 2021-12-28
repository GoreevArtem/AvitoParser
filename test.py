from Avito import *

# url = "https://www.avito.ru/moskva/nedvizhimost_za_rubezhom/kvartira_turtsiya_2292081161"
# url = "https://www.avito.ru/ekaterinburg/zapchasti_i_aksessuary/bamper_peredniy_mersedes_amg_6.3_dlya_s350500_w221_1564428767"
# url = "https://www.avito.ru/ivanovo/gruzoviki_i_spetstehnika/katok_dorozhnyy_gruntovyy_ammann_asc150d_2249486154"
# url = "https://www.avito.ru/nizhniy_novgorod/gruzoviki_i_spetstehnika/gaz_next_2017_2193606937"
# url = "https://www.avito.ru/ivanovo/gruzoviki_i_spetstehnika/shacman_shaanxi_sx3258dr385_2019_2281051227"
# url = "https://www.avito.ru/nizhniy_novgorod/tovary_dlya_kompyutera/modemy_i_routery_2285576961"
# url = "https://www.avito.ru/nizhniy_novgorod/planshety_i_elektronnye_knigi/planshet_s_sim-kartoy_bq_bq-7082g_2287001501"
# url = "https://www.avito.ru/nizhniy_novgorod/audio_i_video/tv_box_ugoos_x4_4k_android_11_podgotovka_2223460371"
# url = "https://www.avito.ru/nizhniy_novgorod/audio_i_video/domashniy_kinoteatr_lg_2303171616"
# url = "https://www.avito.ru/nizhniy_novgorod/audio_i_video/videoproigryvatel_samsung_1913284325"

# url = "https://www.avito.ru/nizhniy_novgorod/audio_i_video/cd_mihail_shufutinskiy._dobryy_vecher_gospoda_2294437993"

url = 'https://www.avito.ru/nizhniy_novgorod/noutbuki/apple_macbook_pro_13_2019_2287457227'
outputdata = AvitoFull(url).get_full_info()
print(outputdata)

'''url = "https://www.avito.ru/nizhniy_novgorod/noutbuki"

get = CategoriesUrl(path=url)
for _page, _url in get.get_url_of_ads().items():
    for item in _url:
        outputdata = AvitoFull(item).get_full_info()
        print(outputdata)'''