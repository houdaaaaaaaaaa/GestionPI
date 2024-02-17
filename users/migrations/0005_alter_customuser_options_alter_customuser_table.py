# Generated by Django 5.0.1 on 2024-02-17 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_num_bureau'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('view_user', 'Can view user')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='custom_user',
        ),
    ]
