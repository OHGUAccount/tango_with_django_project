# Generated by Django 2.2.28 on 2024-02-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_remove_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
