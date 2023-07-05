# Generated by Django 4.2.3 on 2023-07-05 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('img', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=4)),
                ('synopsis', models.TextField(max_length=500)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='main_app.director')),
            ],
        ),
    ]
