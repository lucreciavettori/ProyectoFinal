# Generated by Django 4.0.2 on 2022-03-04 12:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppViajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(upload_to='imagenes_post/', verbose_name='Imagen Referencial')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Mensaje',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='alta',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido_usuario',
            field=models.CharField(default=0, max_length=30, verbose_name='Apellido de usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(default=0, max_length=30, verbose_name='Nombre de usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo electronico'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppViajes.usuario'),
        ),
    ]
