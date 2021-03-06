# Generated by Django 4.0.4 on 2022-06-26 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_tipoautor_options_alter_tipoautor_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='fk_minicurso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.minicurso'),
        ),
        migrations.AddField(
            model_name='video',
            name='fk_minicurso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.minicurso'),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='fk_projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.projeto'),
        ),
        migrations.AlterField(
            model_name='video',
            name='fk_projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.projeto'),
        ),
    ]
