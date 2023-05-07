# Generated by Django 4.0.5 on 2023-04-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quran_text_alll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quran_text_simplee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
    ]
