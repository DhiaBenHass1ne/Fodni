# Generated by Django 5.0 on 2023-12-15 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_review_unique_together_remove_review_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='client',
            field=models.ForeignKey(default=404, on_delete=django.db.models.deletion.CASCADE, to='main.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='provider',
            field=models.ForeignKey(default=404, on_delete=django.db.models.deletion.CASCADE, to='main.provider'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='value',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('client', 'provider')},
        ),
    ]