# Generated by Django 3.2.13 on 2022-06-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifedo_services', '0006_alter_taskmodel_employers'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='Истек срок исполнения?'),
        ),
    ]
