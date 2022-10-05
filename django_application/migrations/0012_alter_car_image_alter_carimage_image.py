# Generated by Django 4.1.1 on 2022-10-05 04:51

from django.db import migrations, models
import django_application.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_application', '0011_alter_car_image_alter_carimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.FileField(null=True, upload_to='get_image_path'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.FileField(upload_to=django_application.models.get_image_path),
        ),
    ]