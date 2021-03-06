# Generated by Django 4.0.1 on 2022-02-11 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('reference_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('photo', models.ImageField(upload_to='')),
                ('phone_number', models.CharField(max_length=11)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('personal', 'Personal'), ('merchant', 'Merchant')], max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('balance', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profile')),
                ('wallet', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Topup',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('reference_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('wallet_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.wallet')),
            ],
        ),
    ]
