# Generated by Django 3.2.9 on 2021-11-10 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryName', models.CharField(max_length=30)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=50)),
                ('authorName', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('isActive', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pages', models.IntegerField()),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedOn', models.DateTimeField(auto_now_add=True)),
                ('category', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booksApp.category')),
                ('subCategory', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booksApp.subcategory')),
            ],
        ),
    ]
