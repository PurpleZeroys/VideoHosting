# Generated by Django 4.2.2 on 2023-06-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("VideoHosting", "0005_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="preview_url",
            field=models.TextField(
                default="https://urfube.hb.ru-msk.vkcs.cloud/71672490903876c42ea496da39ac6220.png",
                max_length=200,
            ),
        ),
    ]
