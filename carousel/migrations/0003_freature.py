# Generated by Django 3.2.3 on 2021-07-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0002_rename_post_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='public/')),
                ('description', models.TextField()),
            ],
        ),
    ]
