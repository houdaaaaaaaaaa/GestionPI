# Generated by Django 5.0.1 on 2024-02-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='niveau',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('c', 'c')], default='c', max_length=5),
        ),
    ]
