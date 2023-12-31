# Generated by Django 4.2.7 on 2023-11-15 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('score', models.FloatField(default=0.0, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_criteria', models.CharField(max_length=6)),
                ('state', models.CharField(choices=[('conforme', 'Compliant'), ('en cours de déploiement', 'Under Deployment'), ('non conforme', 'Improper'), ('non applicable', 'Non Applicable')], max_length=23)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score.website')),
            ],
        ),
    ]
