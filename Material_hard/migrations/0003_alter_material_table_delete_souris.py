# Generated by Django 5.0.1 on 2024-02-29 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Material_hard', '0002_delete_cableusb_material_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='material',
            table='MaterialHard',
        ),
        migrations.DeleteModel(
            name='Souris',
        ),
    ]