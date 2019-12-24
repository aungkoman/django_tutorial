# Generated by Django 3.0 on 2019-12-23 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intakebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mc', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('intake', models.IntegerField()),
                ('phone_no', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intakebook.Academy')),
                ('mc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intakebook.McType')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intakebook.Rank')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intakebook.Role')),
            ],
        ),
    ]
