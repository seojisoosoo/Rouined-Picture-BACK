# Generated by Django 4.1 on 2022-08-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_delete_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor', models.CharField(max_length=50)),
            ],
        ),
    ]
