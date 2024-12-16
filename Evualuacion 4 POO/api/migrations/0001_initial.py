# Generated by Django 5.1.3 on 2024-12-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]