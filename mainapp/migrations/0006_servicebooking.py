# Generated by Django 4.2.3 on 2023-08-07 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=15)),
                ('date', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('request', models.TextField()),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.service')),
            ],
        ),
    ]
