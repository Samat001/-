# Generated by Django 4.1.6 on 2023-02-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='john',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]