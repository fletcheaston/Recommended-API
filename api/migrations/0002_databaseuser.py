# Generated by Django 3.2.5 on 2021-08-01 17:41

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001"),
    ]

    operations = [
        migrations.CreateModel(
            name="DatabaseUser",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated", models.DateTimeField(auto_now=True, db_index=True)),
                ("name", models.TextField()),
                ("email", models.TextField(unique=True)),
                ("hashed_password", models.TextField()),
                ("image_url", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
