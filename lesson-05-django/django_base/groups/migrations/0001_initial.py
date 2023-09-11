# Generated by Django 4.2.5 on 2023-09-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Назва групи')),
                ('students_count', models.IntegerField(default='', verbose_name='Кількість студентів')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
    ]