# Generated by Django 4.2.2 on 2023-06-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='default snippet', max_length=255),
        ),
    ]
