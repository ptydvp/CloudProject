# Generated by Django 3.0.5 on 2020-04-20 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Customer'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Vendor'),
        ),
    ]
