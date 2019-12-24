# Generated by Django 3.0.1 on 2019-12-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=255)),
                ('receiver_name', models.CharField(max_length=255)),
                ('tracking_number', models.CharField(max_length=255)),
                ('address_from', models.CharField(max_length=255)),
                ('address_to', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('AC', 'Accepted'), ('TR', 'In transit'), ('DV', 'Delivered'), ('RJ', 'Rejected')], default='AC', max_length=2)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('weight', models.FloatField(default=0)),
                ('accepted_at', models.DateTimeField(auto_now=True)),
                ('delivered_at', models.DateTimeField(null=True)),
            ],
        ),
    ]