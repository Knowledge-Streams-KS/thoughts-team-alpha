# Generated by Django 4.2.5 on 2023-10-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_thoughts', '0004_alter_thought_shared_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
