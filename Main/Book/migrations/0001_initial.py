# Generated by Django 3.0.2 on 2020-02-13 19:34

from django.db import migrations, models
import django.db.models.deletion
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_data', models.CharField(max_length=11)),
                ('ISBN', isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('pages', models.IntegerField(blank=True)),
                ('language', models.CharField(max_length=4)),
                ('authors', models.ManyToManyField(related_name='author', to='Book.Author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BookCovers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_thumbnail', models.URLField(blank=True, max_length=250, null=True)),
                ('big_thumbnail', models.URLField(blank=True, max_length=250, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='covers', to='Book.Book')),
            ],
        ),
    ]