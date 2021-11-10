# Generated by Django 3.2.9 on 2021-11-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='addedBy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='lastModifiedBy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='addedBy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='lastModifiedBy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='addedBy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='lastModifiedBy',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
