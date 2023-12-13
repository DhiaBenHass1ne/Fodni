# Generated by Django 5.0 on 2023-12-13 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_review_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='bio',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_category', to='main.category'),
        ),
    ]
