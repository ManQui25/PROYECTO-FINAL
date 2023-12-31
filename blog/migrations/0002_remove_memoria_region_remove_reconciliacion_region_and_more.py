# Generated by Django 4.1.2 on 2023-06-22 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memoria',
            name='region',
        ),
        migrations.RemoveField(
            model_name='reconciliacion',
            name='region',
        ),
        migrations.AddField(
            model_name='memoria',
            name='departamento',
            field=models.CharField(choices=[('amazonas', 'Amazonas'), ('antioquia', 'Antioquia'), ('arauca', 'Arauca'), ('atlantico', 'Atlántico'), ('bogota', 'Bogotá'), ('bolivar', 'Bolívar'), ('boyaca', 'Boyacá'), ('caldas', 'Caldas'), ('caqueta', 'Caquetá'), ('cauca', 'Cauca'), ('cesar', 'Cesar'), ('choco', 'Chocó'), ('cordoba', 'Córdoba'), ('cundinamarca', 'Cundinamarca'), ('guaviare', 'Guaviare'), ('huila', 'Huila'), ('guajira', 'Guajira'), ('magdalena', 'Magdalena'), ('meta', 'Meta'), ('nariño', 'Nariño'), ('norte de santander', 'Norte de Santander'), ('putumayo', 'Putumayo'), ('quindio', 'Quindio'), ('risaralda', 'Risaralda'), ('san andres y providencia', 'San Andrés y Providencia'), ('santander', 'Santander'), ('sucre', 'Sucre'), ('tolima', 'Tolima'), ('valle del cauca', 'Valle del Cauca'), ('vaupes', 'Vaupés'), ('vichada', 'Vichada')], default='amazonas', max_length=255),
        ),
        migrations.AddField(
            model_name='reconciliacion',
            name='departamento',
            field=models.CharField(choices=[('amazonas', 'Amazonas'), ('antioquia', 'Antioquia'), ('arauca', 'Arauca'), ('atlantico', 'Atlántico'), ('bogota', 'Bogotá'), ('bolivar', 'Bolívar'), ('boyaca', 'Boyacá'), ('caldas', 'Caldas'), ('caqueta', 'Caquetá'), ('cauca', 'Cauca'), ('cesar', 'Cesar'), ('choco', 'Chocó'), ('cordoba', 'Córdoba'), ('cundinamarca', 'Cundinamarca'), ('guaviare', 'Guaviare'), ('huila', 'Huila'), ('guajira', 'Guajira'), ('magdalena', 'Magdalena'), ('meta', 'Meta'), ('nariño', 'Nariño'), ('norte de santander', 'Norte de Santander'), ('putumayo', 'Putumayo'), ('quindio', 'Quindio'), ('risaralda', 'Risaralda'), ('san andres y providencia', 'San Andrés y Providencia'), ('santander', 'Santander'), ('sucre', 'Sucre'), ('tolima', 'Tolima'), ('valle del cauca', 'Valle del Cauca'), ('vaupes', 'Vaupés'), ('vichada', 'Vichada')], default='amazonas', max_length=255),
        ),
    ]
