# Generated by Django 4.1.1 on 2022-09-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_application', '0002_alter_car_asking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('sold', 'sold')], max_length=20, null=True),
        ),
    ]