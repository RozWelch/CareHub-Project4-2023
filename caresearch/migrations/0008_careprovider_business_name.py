# Generated by Django 3.2.16 on 2023-02-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caresearch', '0007_auto_20230202_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='careprovider',
            name='business_name',
            field=models.CharField(default='default_business_name', max_length=100),
        ),
    ]
