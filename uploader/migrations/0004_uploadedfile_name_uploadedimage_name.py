# Generated by Django 4.1.1 on 2022-09-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uploader", "0003_uploadedfile"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadedfile",
            name="name",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="ファイル名"
            ),
        ),
        migrations.AddField(
            model_name="uploadedimage",
            name="name",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="ファイル名"
            ),
        ),
    ]