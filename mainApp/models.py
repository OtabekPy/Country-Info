from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=50)  # nomi
    population = models.IntegerField(blank=True)  # aholi soni
    area = models.FloatField(blank=True)  # maydoni ming km2
    countrys = models.PositiveSmallIntegerField(blank=True)  # davlatlar soni
    details = models.TextField(blank=True)  # qisqacha qo'shimcha ma'lumot

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)  # nomi
    capital = models.CharField(max_length=50, blank=True)  # poytaxti
    nation = models.CharField(max_length=50, blank=True)  # millati
    language = models.CharField(max_length=50, blank=True)  # tili
    population = models.IntegerField(blank=True, null=True)  # aholi soni
    area = models.FloatField(blank=True, null=True)  # maydoni xxx ming km2
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, blank=True)  # materik foreign key
    currency = models.CharField(max_length=50, blank=True)  # valyuta
    phone = models.CharField(max_length=5, default="+", blank=True, null=True)  # telefon kodi
    time_zone = models.CharField(max_length=3, blank=True, choices=(
        ('-12', '-12'),
        ('-11', '-11'),
        ('-10', '-10'),
        ('-8', '-8'),
        ('-7', '-7'),
        ('-6', '-6'),
        ('-5', '-5'),
        ('-4', '-4'),
        ('-3', '-3'),
        ('-2', '-2'),
        ('-1', '-1'),
        ('+0', '+0'),
        ('+1', '+1'),
        ('+2', '+2'),
        ('+3', '+3'),
        ('+4', '+4'),
        ('+5', '+5'),
        ('+6', '+6'),
        ('+7', '+7'),
        ('+8', '+8'),
        ('+10', '+10'),
        ('+11', '+11'),
        ('+12', '+12'),
    ), null=True)  # vaqt mintaqasi
    latitude = models.FloatField(blank=True, null=True)  # kenglik kordinataga nisbatan
    longitude = models.FloatField(blank=True, null=True)  # uzunlik kordinataga nisbatan
    government_type = models.CharField(max_length=50, choices=(
        ('Republic', 'Republic'),  # respublika
        ('Islamic Republic', 'Islamic Republic'),
        ('Monarchy', 'Monarchy'),  # monarxiya
        ('State', 'State'),  # shtat
        ('Federation', 'Federation'),  # federatsiya
        ('Emirate', 'Emirate'),  # amirlik
        ('Kingdom', 'Kingdom'),  # saltanat, qirollik
        ('Empire', 'Empire'),  # imperiya, hukmronlik
        ('Theocracy', 'Theocracy')  # teokratiya - dinga asoslangan boshqaruv tizimi
    ), blank=True)
    climate = models.TextField(max_length=1000, blank=True, null=True)  # iqlimi batafsil
    urbanization = models.FloatField(blank=True, null=True)  # shahar aholisi % da
    average_age = models.PositiveSmallIntegerField(blank=True, null=True)  # o'rtacha umr ko'rish
    flag = models.ImageField(upload_to='flags', blank=True, null=True)  # davlat bayrog'i
    emblem = models.ImageField(upload_to='emblems', blank=True, null=True)  # davlat gerbi
    hymn = models.TextField(blank=True, null=True)  # davlat madhiyasi

    def __str__(self):
        return self.name


class Contiguous(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='contiguous_countries')
    countrys = models.ManyToManyField(Country, 'contiguous_to')

    def __str__(self):
        return self.country.name
