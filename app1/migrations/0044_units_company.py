# Generated by Django 4.0.4 on 2022-09-30 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0043_employee_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='units',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
