# Generated by Django 3.2.5 on 2022-01-09 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=200, unique=True)),
                ('mobile_no', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.user')),
                ('profile_no', models.IntegerField(default=0)),
            ],
        ),
    ]
