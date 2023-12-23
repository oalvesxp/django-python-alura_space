# Generated by Django 4.2.7 on 2023-12-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galaxia'), ('PLANETAS', 'Planeta')], default='', max_length=100),
        ),
    ]