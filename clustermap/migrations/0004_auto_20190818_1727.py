# Generated by Django 2.2.4 on 2019-08-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clustermap', '0003_coords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coord_lats', models.FloatField()),
                ('coord_lons', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Coords',
        ),
    ]