# Generated by Django 4.0.3 on 2022-03-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAccounts', '0008_remove_profile_email_alter_profile_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]