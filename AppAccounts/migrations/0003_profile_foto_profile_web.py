# Generated by Django 4.0.3 on 2022-03-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAccounts', '0002_remove_profile_posts_profile_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
        migrations.AddField(
            model_name='profile',
            name='web',
            field=models.URLField(blank=True, null=True),
        ),
    ]
