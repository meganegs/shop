# Generated by Django 4.1.5 on 2023-01-31 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=200)),
                ("prenoms", models.CharField(db_index=True, max_length=200)),
                ("date_de_naissance", models.CharField(db_index=True, max_length=200)),
                ("date_inscription", models.CharField(db_index=True, max_length=200)),
                ("postal_addresse", models.CharField(db_index=True, max_length=200)),
                ("email", models.CharField(db_index=True, max_length=200)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Livreur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=200)),
                ("prenoms", models.CharField(db_index=True, max_length=200)),
                ("date_de_naissance", models.CharField(db_index=True, max_length=200)),
                ("date_inscription", models.CharField(db_index=True, max_length=200)),
                ("postal_addresse", models.CharField(db_index=True, max_length=200)),
                ("adresse_facturation", models.CharField(max_length=200)),
                ("email", models.CharField(db_index=True, max_length=200)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
