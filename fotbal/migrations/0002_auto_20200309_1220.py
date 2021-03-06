# Generated by Django 3.0.4 on 2020-03-09 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fotbal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='cislo_dresu',
            field=models.IntegerField(max_length=2, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='jmeno',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='narozeni',
            field=models.DateField(verbose_name='Birthdate'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='post',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='prijmeni',
            field=models.CharField(max_length=30, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='obec',
            name='nazev_obce',
            field=models.CharField(max_length=40, verbose_name='Village name'),
        ),
        migrations.AlterField(
            model_name='realizacni_tym',
            name='jmeno',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='realizacni_tym',
            name='narozeni',
            field=models.DateField(verbose_name='Birthdate'),
        ),
        migrations.AlterField(
            model_name='realizacni_tym',
            name='pozice',
            field=models.CharField(max_length=25, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='realizacni_tym',
            name='prijmeni',
            field=models.CharField(max_length=30, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='tym',
            name='informace',
            field=models.TextField(verbose_name='Informations about team'),
        ),
        migrations.AlterField(
            model_name='tym',
            name='nazev',
            field=models.CharField(max_length=40, verbose_name='Team name'),
        ),
        migrations.AlterField(
            model_name='tym',
            name='znak',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Team symbol'),
        ),
        migrations.AlterField(
            model_name='zapasy',
            name='cas',
            field=models.TimeField(verbose_name='Match time'),
        ),
        migrations.AlterField(
            model_name='zapasy',
            name='datum',
            field=models.DateField(verbose_name='Match date'),
        ),
        migrations.AlterField(
            model_name='zapasy',
            name='domaci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Home', to='fotbal.Tym'),
        ),
        migrations.AlterField(
            model_name='zapasy',
            name='hoste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Host', to='fotbal.Tym'),
        ),
        migrations.AlterField(
            model_name='zapasy',
            name='skore_domaci',
            field=models.IntegerField(max_length=2, verbose_name='Home score'),
        ),
        migrations.AlterField(
            model_name='zapasy',
            name='skore_hoste',
            field=models.IntegerField(max_length=2, verbose_name='Host score'),
        ),
    ]
