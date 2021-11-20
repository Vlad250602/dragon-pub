from django.db import models

class sushi_news(models.Model):
    name = models.CharField('Название новости', max_length=30)
    spec = models.TextField('Новость', max_length=300, blank=True)
    date = models.CharField('Дата', max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости суши'


class pub_news(models.Model):
    name = models.CharField('Название новости', max_length=30)
    spec = models.TextField('Новость', max_length=300, blank=True)
    date = models.CharField('Дата', max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости паб'

#sushi
class Menu_shef(models.Model):
    name = models.CharField('Название', max_length=20)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=100)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='/media/sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ролы от шефа'
        verbose_name_plural = 'Ролы от шефа'

class Menu_maki(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=100, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Маки'
        verbose_name_plural = 'Маки'

class Menu_kalif_kunj(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=100, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Калифорния кунжут'
        verbose_name_plural = 'Калифорния кунжут'

class Menu_kalif_tobiko(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=100, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Калифорния тобико'
        verbose_name_plural = 'Калифорния тобико'

class Menu_cheese(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=100, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сыр филадельфия'
        verbose_name_plural = 'Сыр филадельфия'

class Menu_dragon(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=100, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рол дракон'
        verbose_name_plural = 'Рол дракон'

class Menu_sets(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сет'
        verbose_name_plural = 'Сеты'

class Menu_nigiri(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нигири'
        verbose_name_plural = 'Нигири'

class Menu_gunkan(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Гункан'
        verbose_name_plural = 'Гункан'

class Menu_sashimi(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="sushi", default='sushi/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сашими'
        verbose_name_plural = 'Сашими'

#pub

class Menu_pub_lunch(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ланчи'
        verbose_name_plural = 'Ланч'

class Menu_pub_salad(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Салаты'
        verbose_name_plural = 'Салат'

class Menu_pub_soup(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Супы'
        verbose_name_plural = 'Суп'

class Menu_pub_fish(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рыбные блюда'
        verbose_name_plural = 'Рыбное блюдо'

class Menu_pub_grill(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=20)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Гриль блюда'
        verbose_name_plural = 'Гриль блюдо'

class Menu_pub_pizza(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пицца'

class Menu_pub_dessert(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Десерты'
        verbose_name_plural = 'Десерт'

class Menu_pub_garnish(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Гарниры'
        verbose_name_plural = 'Гарнир'

class Menu_pub_tea(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чай/кофе'
        verbose_name_plural = 'Чай/кофе'

class Menu_pub_home(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Домашние блюда'
        verbose_name_plural = 'Домашнее блюдо'

class Menu_pub_water(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вода'
        verbose_name_plural = 'Вода'

class Menu_pub_coctail(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коктели'
        verbose_name_plural = 'Коктель'

class Menu_pub_coctail_non(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Безалкогольные коктели'
        verbose_name_plural = 'Безалкогольный коктель'

#----------------Alcohol-------------------------
class Menu_alco_vodka(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vodka'
        verbose_name_plural = 'Vodka'

class Menu_alco_brendi(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brendi'
        verbose_name_plural = 'Brendi'

class Menu_alco_konjack(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Konjack'
        verbose_name_plural = 'Konjack'

class Menu_alco_vine_bokal(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vine bokal'
        verbose_name_plural = 'Vine bokal'

class Menu_alco_vine_igr(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vine igr'
        verbose_name_plural = 'Vine igr'

class Menu_alco_vine_white(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vine white'
        verbose_name_plural = 'Vine white'

class Menu_alco_vine_red(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vine red'
        verbose_name_plural = 'Vine red'

class Menu_alco_beer(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Beer'
        verbose_name_plural = 'Beer'

class Menu_alco_whiskey(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Whiskey'
        verbose_name_plural = 'Whiskey'

class Menu_alco_liker(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Liker'
        verbose_name_plural = 'Liker'

class Menu_alco_djin(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Djin'
        verbose_name_plural = 'Djin'

class Menu_alco_rom(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rom'
        verbose_name_plural = 'Rom'

class Menu_alco_tekila(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tekila'
        verbose_name_plural = 'Tekila'

class Menu_alco_vermut(models.Model):
    name = models.CharField('Название', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    spec = models.CharField('Состав', max_length=200, blank=True)
    price = models.CharField('Цена', max_length=10)
    image = models.ImageField(upload_to="pub", default='pub/empty.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vermut'
        verbose_name_plural = 'Vermut'
