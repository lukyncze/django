from django.db import models

class Hrac(models.Model):
    jmeno = models.CharField(max_length=20, verbose_name='Name')
    prijmeni = models.CharField(max_length=30, verbose_name='Surname')
    narozeni = models.DateField(verbose_name='Birthdate')
    post = models.CharField(max_length=20, verbose_name='Position', null=True, blank=True)
    cislo_dresu = models.IntegerField(max_length=2, verbose_name='Number')
    tym_nazev = models.ForeignKey('Tym', on_delete=models.DO_NOTHING)

class Realizacni_tym(models.Model):
    jmeno = models.CharField(max_length=20, verbose_name='Name')
    prijmeni = models.CharField(max_length=30, verbose_name='Surname')
    narozeni = models.DateField(verbose_name='Birthdate')
    pozice = models.CharField(max_length=25, verbose_name='Position')
    tym_nazev = models.ForeignKey('Tym', on_delete=models.DO_NOTHING)

class Tym(models.Model):
    nazev = models.CharField(max_length=40, verbose_name='Team name')
    informace = models.TextField(verbose_name='Informations about team')
    znak = models.ImageField(verbose_name='Team symbol', null=True, blank=True)
    obec = models.ForeignKey('Obec', on_delete=models.DO_NOTHING)

class Obec(models.Model):
    nazev_obce = models.CharField(max_length=40, verbose_name='Village name')

class Zapasy(models.Model):
    domaci = models.ForeignKey('Tym', on_delete=models.DO_NOTHING, related_name='Home')
    hoste = models.ForeignKey('Tym', on_delete=models.DO_NOTHING, related_name='Host')
    skore_domaci = models.IntegerField(max_length=2, verbose_name='Home score')
    skore_hoste = models.IntegerField(max_length=2, verbose_name='Host score')
    datum = models.DateField(verbose_name='Match date')
    cas = models.TimeField(verbose_name='Match time')
