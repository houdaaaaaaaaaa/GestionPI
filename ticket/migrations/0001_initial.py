# Generated by Django 5.0.1 on 2024-02-29 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_titre', models.CharField(max_length=50)),
                ('ticket_description', models.TextField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('panding', 'panding'), ('resolved', 'resolved')], default=True, max_length=20)),
                ('date_de_creation', models.DateTimeField(auto_now_add=True)),
                ('derniere_modification', models.DateTimeField(auto_now=True)),
                ('niveau', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('c', 'c')], default='B', max_length=5)),
                ('technicien', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='engineer', to=settings.AUTH_USER_MODEL)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
