# Generated by Django 3.1.3 on 2020-12-03 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_create_trigger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_region', models.CharField(max_length=300)),
                ('koordinate_region', models.CharField(max_length=300)),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.news')),
            ],
        ),
    ]
