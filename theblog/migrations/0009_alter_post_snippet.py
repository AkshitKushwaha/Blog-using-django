# Generated by Django 4.2.2 on 2023-06-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='', max_length=255),
        ),
    ]