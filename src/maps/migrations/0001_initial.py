# Generated by Django 3.1.3 on 2020-12-02 05:50

import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=500)),
                ('web_site', models.CharField(max_length=30)),
                ('news_date', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('document_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]