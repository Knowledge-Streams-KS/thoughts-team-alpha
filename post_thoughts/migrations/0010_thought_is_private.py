# Generated by Django 4.2.4 on 2023-10-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_thoughts', '0009_alter_thought_shared_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]
