# Generated by Django 4.0.4 on 2022-07-01 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='documento_contratista',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='nombre_contratista',
        ),
        migrations.RemoveField(
            model_name='entidad',
            name='rector',
        ),
        migrations.CreateModel(
            name='Rector',
            fields=[
                ('modelobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entidades.modelobase')),
                ('persona_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.persona')),
            ],
            bases=('entidades.modelobase',),
        ),
        migrations.CreateModel(
            name='Contratista',
            fields=[
                ('modelobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entidades.modelobase')),
                ('persona_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.persona')),
            ],
            bases=('entidades.modelobase',),
        ),
        migrations.AddField(
            model_name='contrato',
            name='contratista_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.contratista'),
        ),
        migrations.AddField(
            model_name='entidad',
            name='rector_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidades.rector'),
        ),
    ]
