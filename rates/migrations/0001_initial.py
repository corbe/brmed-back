# Generated by Django 4.0.4 on 2022-05-22 12:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('base_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_currency', to='rates.currency')),
            ],
        ),
        migrations.CreateModel(
            name='RateValue',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency', to='rates.currency')),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='rates.rate')),
            ],
        ),
    ]
