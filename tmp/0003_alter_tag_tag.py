# Generated by Django 5.0.3 on 2024-03-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0002_author_created_at_quote_created_at_tag_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
