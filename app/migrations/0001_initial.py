# Generated by Django 4.2.4 on 2023-09-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('serie', models.IntegerField()),
                ('nota_final', models.IntegerField()),
            ],
        ),
    ]
