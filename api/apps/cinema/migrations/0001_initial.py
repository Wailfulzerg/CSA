# Generated by Django 4.0.2 on 2022-02-26 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('afisha_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='halls', to='cinema.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='cinema.cinema')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='cinema.hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='movies.movie')),
            ],
        ),
    ]
