# Generated by Django 3.2.8 on 2021-11-13 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crpyto', '0010_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('membership_type', models.CharField(choices=[('Medium', 'Medium'), ('Advance', 'Advance'), ('Extended', 'Extended'), ('Free', 'Free')], default='Free', max_length=30)),
                ('duration', models.PositiveIntegerField(default=7)),
                ('duration_period', models.CharField(choices=[('Days', 'Days'), ('Week', 'Week'), ('Months', 'Months')], default='Day', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('price2', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_code', models.CharField(blank=True, default='', max_length=100)),
                ('membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_membership', to='crpyto.membership')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires_in', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('user_membership', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='crpyto.usermembership')),
            ],
        ),
        migrations.CreateModel(
            name='PayHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_for', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crpyto.membership')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
