# Generated by Django 5.1.3 on 2024-11-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hackathon", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="relatorio",
            name="imagens_antes",
            field=models.ImageField(blank=True, null=True, upload_to="imagens/antes/"),
        ),
        migrations.AddField(
            model_name="relatorio",
            name="imagens_depois",
            field=models.ImageField(blank=True, null=True, upload_to="imagens/antes/"),
        ),
    ]