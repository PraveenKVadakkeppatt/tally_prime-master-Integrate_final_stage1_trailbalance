# Generated by Django 4.0.4 on 2022-10-14 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0058_svouchert_pvouchert_divouchert_bdvouchert'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdvouchert',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='divouchert',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='pvouchert',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='svouchert',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
