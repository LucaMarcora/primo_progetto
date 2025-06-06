# Generated by Django 5.1.3 on 2025-01-29 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Giornalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('contenuto', models.TextField()),
                ('giornalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articoli', to='news.giornalista')),
            ],
        ),
    ]
