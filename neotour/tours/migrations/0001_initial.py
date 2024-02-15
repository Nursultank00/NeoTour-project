# Generated by Django 5.0.2 on 2024-02-15 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='tour_profile_photos')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tours.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('review_image', models.ImageField(upload_to='review_images')),
                ('commentary', models.TextField()),
                ('tour_related', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tours.tour')),
            ],
        ),
    ]
