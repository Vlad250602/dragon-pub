from django.shortcuts import render
from .models import Menu_shef, \
    Menu_maki, Menu_kalif_kunj, \
    Menu_kalif_tobiko, Menu_cheese, \
    Menu_dragon, Menu_sets, Menu_nigiri, \
    Menu_sashimi, Menu_gunkan
from .models import Menu_pub_tea, \
    Menu_pub_home, Menu_pub_soup,\
    Menu_pub_pizza, Menu_pub_grill, \
    Menu_pub_garnish, Menu_pub_lunch, \
    Menu_pub_water, Menu_pub_coctail,\
    Menu_pub_coctail_non, Menu_pub_dessert, \
    Menu_pub_salad, Menu_pub_fish, \
    Menu_pub_zak_beer, Menu_pub_zak_cold, \
    Menu_alco_vodka, Menu_alco_brendi, \
    Menu_alco_konjack, Menu_alco_vine_bokal, \
    Menu_alco_vine_igr, Menu_alco_vine_red, \
    Menu_alco_vine_white, Menu_alco_beer, \
    Menu_alco_whiskey, Menu_alco_liker, \
    Menu_alco_djin, Menu_alco_rom, \
    Menu_alco_tekila, Menu_alco_vermut

from .models import sushi_news, pub_news

#----------------------------------SUSHI-----------------------------------------
def Sushi_main(request):
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_main.html', {'news': n1})

def Sushi_news(request):
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_news.html', {'news': n1})

def sushi_rolls_shef(request):
    dish = Menu_shef.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Rolls_shef.html', {'Menu': dish, 'news': n1})

def sushi_maki(request):
    dish = Menu_maki.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Maki.html', {'Menu': dish, 'news': n1})

def sushi_kalif_kunj(request):
    dish = Menu_kalif_kunj.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Kalif_kunjut.html', {'Menu': dish, 'news': n1})

def sushi_kalif_tobiko(request):
    dish = Menu_kalif_tobiko.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Kalif_tobiko.html', {'Menu': dish, 'news': n1})

def sushi_cheese(request):
    dish = Menu_cheese.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Cheese_filadelfia.html', {'Menu': dish, 'news': n1})

def sushi_dragon_roll(request):
    dish = Menu_dragon.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Roll_dragon.html', {'Menu': dish, 'news': n1})

def sushi_sets(request):
    dish = Menu_sets.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Sets.html', {'Menu': dish, 'news': n1})

def sushi_nigiri(request):
    dish = Menu_nigiri.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Sushi_nigiri.html', {'Menu': dish, 'news': n1})

def sushi_gunkan(request):
    dish = Menu_gunkan.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_Gunkan_nigiri.html', {'Menu': dish, 'news': n1})

def sushi_sashimi(request):
    dish = Menu_sashimi.objects.all()
    n1 = sushi_news.objects.all()
    return render(request, 'main/sushi_sashimi.html', {'Menu': dish, 'news': n1})


#-----------------------------------PUB------------------------------------------

def Pub_main(request):
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_main.html', {'news': n1})

def Pub_news(request):
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_news.html', {'news': n1})

def pub_lunch(request):
    dish = Menu_pub_lunch.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_lunch.html', {'Menu': dish, 'news': n1})

def pub_salad(request):
    dish = Menu_pub_salad.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Salad.html', {'Menu': dish, 'news': n1})

def pub_soup(request):
    dish = Menu_pub_soup.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Soup.html', {'Menu': dish, 'news': n1})

def pub_grill(request):
    dish = Menu_pub_grill.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Grill.html', {'Menu': dish, 'news': n1})

def pub_pizza(request):
    dish = Menu_pub_pizza.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Pizza.html', {'Menu': dish, 'news': n1})

def pub_dessert(request):
    dish = Menu_pub_dessert.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Desert.html', {'Menu': dish, 'news': n1})

def pub_garnir(request):
    dish = Menu_pub_garnish.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Garnir.html', {'Menu': dish, 'news': n1})

def pub_tea_coffee(request):
    dish = Menu_pub_tea.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Tea_coffee.html', {'Menu': dish, 'news': n1})

def pub_home(request):
    dish = Menu_pub_home.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Home_tea.html', {'Menu': dish, 'news': n1})

def pub_water(request):
    dish = Menu_pub_water.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Water.html', {'Menu': dish, 'news': n1})

def pub_coctails(request):
    dish = Menu_pub_coctail.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Coctail_alco.html', {'Menu': dish, 'news': n1})

def pub_non_alco_coctails(request):
    dish = Menu_pub_coctail_non.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Coctail_nonalco.html', {'Menu': dish, 'news': n1})

def pub_zak_beer(request):
    dish = Menu_pub_zak_beer.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_zak_beer.html', {'Menu': dish, 'news': n1})

def pub_zak_cold(request):
    dish = Menu_pub_zak_cold.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_zak_cold.html', {'Menu': dish, 'news': n1})

#-------------------------Alcohol models--------------------------------
def pub_alco(request):
    vodka = Menu_alco_vodka.objects.all()
    brendi = Menu_alco_brendi.objects.all()
    konjack = Menu_alco_konjack.objects.all()
    vine_bokal = Menu_alco_vine_bokal.objects.all()
    vine_igr = Menu_alco_vine_igr.objects.all()
    vine_white = Menu_alco_vine_white.objects.all()
    vine_red = Menu_alco_vine_red.objects.all()
    beer = Menu_alco_beer.objects.all()
    whiskey = Menu_alco_whiskey.objects.all()
    liker = Menu_alco_liker.objects.all()
    djin = Menu_alco_djin.objects.all()
    rom = Menu_alco_rom.objects.all()
    tekila = Menu_alco_tekila.objects.all()
    vermut = Menu_alco_vermut.objects.all()
    n1 = pub_news.objects.all()
    return render(request, 'main/pub_Alco.html', {'vodka': vodka, 'brendi': brendi, 'konjack': konjack,
                                                  'vine_bokal': vine_bokal, 'vine_igr': vine_igr,
                                                  'vine_white': vine_white, 'vine_red': vine_red,
                                                  'beer': beer, 'whiskey': whiskey, 'liker': liker,
                                                  'djin': djin, 'rom': rom, 'tekila': tekila, 'vermut': vermut,
                                                  'news': n1})
