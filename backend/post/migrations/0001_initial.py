# Generated by Django 3.2.7 on 2021-09-17 07:09

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=350)),
                ('image', models.ImageField(upload_to=post.models.upload_to, verbose_name='Image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
