# Generated by Django 4.2.2 on 2023-07-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postType',
            field=models.CharField(choices=[('AR', 'Статья'), ('NW', 'Новости')], default='AR', max_length=2),
        ),
    ]
