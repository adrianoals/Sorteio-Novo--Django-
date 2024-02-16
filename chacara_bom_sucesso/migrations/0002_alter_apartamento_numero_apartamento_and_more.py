# Generated by Django 5.0.1 on 2024-02-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chacara_bom_sucesso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamento',
            name='numero_apartamento',
            field=models.CharField(choices=[('Apto 01', 'Apto 01'), ('Apto 02', 'Apto 02'), ('Apto 11', 'Apto 11'), ('Apto 12', 'Apto 12'), ('Apto 13', 'Apto 13'), ('Apto 14', 'Apto 14'), ('Apto 15', 'Apto 15'), ('Apto 16', 'Apto 16'), ('Apto 21', 'Apto 21'), ('Apto 22', 'Apto 22'), ('Apto 23', 'Apto 23'), ('Apto 24', 'Apto 24'), ('Apto 25', 'Apto 25'), ('Apto 26', 'Apto 26'), ('Apto 31', 'Apto 31'), ('Apto 32', 'Apto 32'), ('Apto 33', 'Apto 33'), ('Apto 34', 'Apto 34'), ('Apto 35', 'Apto 35'), ('Apto 36', 'Apto 36'), ('Apto 41', 'Apto 41'), ('Apto 42', 'Apto 42'), ('Apto 43', 'Apto 43'), ('Apto 44', 'Apto 44'), ('Apto 45', 'Apto 45'), ('Apto 46', 'Apto 46')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='bloco',
            name='bloco',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='-', max_length=100, unique=True),
        ),
    ]