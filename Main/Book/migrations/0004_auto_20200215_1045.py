# Generated by Django 3.0.2 on 2020-02-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_auto_20200215_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcovers',
            name='big_thumbnail',
            field=models.URLField(blank=True, default='https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781442499577/random-9781442499577_hr.jpg', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bookcovers',
            name='small_thumbnail',
            field=models.URLField(blank=True, default='https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781442499577/random-9781442499577_hr.jpg', max_length=250, null=True),
        ),
    ]
