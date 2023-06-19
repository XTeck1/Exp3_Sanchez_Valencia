# Generated by Django 4.2.1 on 2023-06-14 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(blank=True, max_length=50, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Codigo producto')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('precio', models.CharField(blank=True, max_length=10, verbose_name='Precio')),
                ('stock', models.CharField(blank=True, max_length=10, verbose_name='Stock')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.categoria', verbose_name='Categoria')),
            ],
        ),
    ]