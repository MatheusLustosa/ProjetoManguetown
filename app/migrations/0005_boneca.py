# Generated by Django 5.1.1 on 2024-10-25 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_empresaparceira_captacao_local_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boneca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.PositiveIntegerField()),
                ('nivel_dificuldade', models.CharField(max_length=50)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonecas', to='app.colaborador')),
            ],
        ),
    ]
