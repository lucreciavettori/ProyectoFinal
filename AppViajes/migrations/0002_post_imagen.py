# Generated by Django 4.0.2 on 2022-03-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppViajes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_post/', verbose_name='Imagen Referencial'),
        ),
    ]
