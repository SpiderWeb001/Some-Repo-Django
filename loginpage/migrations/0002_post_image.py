# Generated by Django 3.2.6 on 2021-08-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
