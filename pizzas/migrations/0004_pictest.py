# Generated by Django 3.2.1 on 2021-05-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(upload_to='booktest')),
            ],
        ),
    ]