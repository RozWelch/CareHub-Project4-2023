# Generated by Django 3.2.16 on 2023-01-30 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caresearch', '0003_auto_20230129_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careseeker',
            old_name='landline_phone_number',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='careseeker',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='careseeker',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='careseeker',
            name='address_line_3',
        ),
        migrations.RemoveField(
            model_name='careseeker',
            name='mobile_phone',
        ),
        migrations.RemoveField(
            model_name='careseeker',
            name='postcode',
        ),
    ]
