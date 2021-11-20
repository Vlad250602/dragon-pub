from django.contrib import admin
from .models import Menu_shef, \
    Menu_maki, Menu_kalif_kunj, \
    Menu_kalif_tobiko, Menu_cheese, \
    Menu_dragon, Menu_sets, \
    Menu_nigiri, Menu_gunkan, Menu_sashimi
from .models import Menu_pub_tea, \
    Menu_pub_home, Menu_pub_soup,\
    Menu_pub_pizza, Menu_pub_grill, \
    Menu_pub_garnish, Menu_pub_lunch, \
    Menu_pub_water, Menu_pub_coctail, \
    Menu_pub_coctail_non, Menu_pub_dessert, \
    Menu_pub_salad, Menu_pub_fish, \
    Menu_alco_vodka, Menu_alco_brendi, \
    Menu_alco_konjack, Menu_alco_vine_bokal,\
    Menu_alco_vine_igr, Menu_alco_vine_red, \
    Menu_alco_vine_white, Menu_alco_beer, \
    Menu_alco_whiskey, Menu_alco_liker, \
    Menu_alco_djin, Menu_alco_rom, \
    Menu_alco_tekila, Menu_alco_vermut
from .models import sushi_news, pub_news

admin.site.register(sushi_news)
admin.site.register(pub_news)
#sushi models
admin.site.register(Menu_shef)
admin.site.register(Menu_maki)
admin.site.register(Menu_kalif_kunj)
admin.site.register(Menu_kalif_tobiko)
admin.site.register(Menu_cheese)
admin.site.register(Menu_dragon)
admin.site.register(Menu_sets)
admin.site.register(Menu_nigiri)
admin.site.register(Menu_gunkan)
admin.site.register(Menu_sashimi)

#pub models
admin.site.register(Menu_pub_fish)
admin.site.register(Menu_pub_coctail)
admin.site.register(Menu_pub_salad)
admin.site.register(Menu_pub_coctail_non)
admin.site.register(Menu_pub_dessert)
admin.site.register(Menu_pub_water)
admin.site.register(Menu_pub_pizza)
admin.site.register(Menu_pub_lunch)
admin.site.register(Menu_pub_garnish)
admin.site.register(Menu_pub_grill)
admin.site.register(Menu_pub_soup)
admin.site.register(Menu_pub_home)
admin.site.register(Menu_pub_tea)

admin.site.register(Menu_alco_vodka)
admin.site.register(Menu_alco_brendi)
admin.site.register(Menu_alco_konjack)
admin.site.register(Menu_alco_vine_bokal)
admin.site.register(Menu_alco_vine_igr)
admin.site.register(Menu_alco_vine_white)
admin.site.register(Menu_alco_vine_red)
admin.site.register(Menu_alco_beer)
admin.site.register(Menu_alco_whiskey)
admin.site.register(Menu_alco_liker)
admin.site.register(Menu_alco_djin)
admin.site.register(Menu_alco_rom)
admin.site.register(Menu_alco_tekila)
admin.site.register(Menu_alco_vermut)
