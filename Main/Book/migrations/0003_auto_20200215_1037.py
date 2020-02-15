# Generated by Django 3.0.2 on 2020-02-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20200213_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcovers',
            name='big_thumbnail',
            field=models.URLField(blank=True, default='default_for_articles.jpg', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bookcovers',
            name='small_thumbnail',
            field=models.URLField(blank=True, default='default_for_articles.jpg', max_length=250, null=True),
        ),
    ]
