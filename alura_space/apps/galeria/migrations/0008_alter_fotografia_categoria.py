# Generated by Django 4.2.7 on 2023-12-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_fotografia_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galaxia'), ('PLANETAS', 'Planeta'), ('TELESCOPIOS', 'Telescopios'), ('SATELITES', 'Satelites')], default='', max_length=100),
        ),
    ]
