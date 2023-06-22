# Generated by Django 4.2 on 2023-06-20 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Oui', max_length=100)),
                ('has2links', models.BooleanField(default=False)),
                ('link1name', models.CharField(default='Oui', max_length=100)),
                ('link2name', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.CharField(default='Oui', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hosters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('changelog', models.CharField(blank=True, max_length=100, null=True)),
                ('download', models.CharField(max_length=100)),
                ('download2', models.CharField(blank=True, max_length=100)),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datas.category')),
                ('game', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datas.game')),
                ('hostdownload', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datas.hosters')),
                ('hostdownload2', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hostdownload2', to='datas.hosters')),
            ],
        ),
        migrations.CreateModel(
            name='CatAndGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.game')),
            ],
        ),
    ]
