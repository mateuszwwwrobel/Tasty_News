# Generated by Django 3.0.5 on 2021-02-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='portal',
            field=models.CharField(
                choices=[('Benchmark.pl', 'Benchmark.pl'), ('boardgamesgeek.com', 'boardgamesgeek.com'),
                         ('Tojuzbylo.pl', 'Tojuzbylo.pl'), ('Zwiadowca Historii', 'Zwiadowca Historii'),
                         ('Computer World', 'Computer World'), ('InfoWorldPython.com', 'InfoWorldPython.com'),
                         ('RealPython.com', 'RealPython.com'), ('bushcraftable.com', 'bushcraftable.com')],
                max_length=100),
        ),
    ]
