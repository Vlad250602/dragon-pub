from django.urls import path
from . import views

urlpatterns = [
    #sushi
    path('', views.Sushi_main, name='sushi_main'),
    path('rolls-shef', views.sushi_rolls_shef, name='shef'),
    path('sushi-news', views.Sushi_news, name='sushi_news'),
    path('maki_rolls', views.sushi_maki, name='maki'),
    path('rolls_kalifornia_kunjit', views.sushi_kalif_kunj, name='kalif_kunj'),
    path('rolls_kalifornia_tobiko', views.sushi_kalif_tobiko, name='kalif_tobiko'),
    path('rolls_cheese_filadelfia', views.sushi_cheese, name='cheese'),
    path('rolls_dragon', views.sushi_dragon_roll, name='dragon_roll'),
    path('sets', views.sushi_sets, name='sets'),
    path('sushi_nigiri', views.sushi_nigiri, name='nigiri'),
    path('gunkan_nigiri', views.sushi_gunkan, name='gunkan'),
    path('sashimi', views.sushi_sashimi, name='sashimi'),
    #Pub
    path('pub-news', views.Pub_news, name='pub_news'),
    path('pub-main',views.Pub_main, name='pub_main'),
    path('lunch', views.pub_lunch, name='lunch'),
    path('salad', views.pub_salad, name='salad'),
    path('soup', views.pub_soup, name='soup'),
    path('fish', views.pub_fish, name='fish'),
    path('grill-menu', views.pub_grill, name='grill'),
    path('pizza', views.pub_pizza, name='pizza'),
    path('dessert', views.pub_dessert, name='dessert'),
    path('garnish', views.pub_garnir, name='garnir'),
    path('tea-coffee', views.pub_tea_coffee, name='tea_coffee'),
    path('home-dish', views.pub_home, name='home'),
    path('water', views.pub_water, name='water'),
    path('alcohol-coctails', views.pub_coctails, name='coctails'),
    path('non-alco-coctails', views.pub_non_alco_coctails, name='non_alco_coctails'),

    path('alcohol', views.pub_alco, name='alco'),
]
