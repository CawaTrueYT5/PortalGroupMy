# Generated by Django 5.2 on 2025-04-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
