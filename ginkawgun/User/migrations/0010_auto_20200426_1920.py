# Generated by Django 3.0.5 on 2020-04-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20200426_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='userpicture',
            field=models.ImageField(blank=True, null=True, upload_to='user_image'),
        ),
    ]
