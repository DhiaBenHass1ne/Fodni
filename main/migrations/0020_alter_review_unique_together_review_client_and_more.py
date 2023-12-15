# Generated by Django 5.0 on 2023-12-15 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_rename_rating_review_value'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('client', 'provider')},
        ),
        migrations.AddField(
            model_name='review',
            name='client',
            field=models.ForeignKey(default=404, on_delete=django.db.models.deletion.CASCADE, to='main.client'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]
