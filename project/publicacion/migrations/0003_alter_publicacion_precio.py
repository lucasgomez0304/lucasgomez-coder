# Generated by Django 5.0.4 on 2024-05-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0002_alter_ciudad_options_alter_pais_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
