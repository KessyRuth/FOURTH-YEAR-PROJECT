# Generated by Django 4.2.10 on 2024-02-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KidneyPredictor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('serum_creatinine', models.FloatField()),
                ('blood_pressure', models.FloatField()),
            ],
        ),
    ]
