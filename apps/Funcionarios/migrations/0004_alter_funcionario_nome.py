# Generated by Django 3.2 on 2022-01-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionarios', '0003_funcionario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
    ]
