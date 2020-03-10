# Generated by Django 3.0.3 on 2020-03-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_is_freelancer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='location',
            field=models.TextField(choices=[('Hyd', 'Hyderabad'), ('MAS', 'Chennai')], default='Hyd'),
        ),
        migrations.AddField(
            model_name='freelancerprofile',
            name='location',
            field=models.TextField(choices=[('Hyd', 'Hyderabad'), ('MAS', 'Chennai')], default=None),
        ),
    ]
