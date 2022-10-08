# Generated by Django 4.0.5 on 2022-09-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_alter_ledgeranalysismodel_lpert_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_Voucher_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True, null=True)),
                ('Particular', models.CharField(max_length=40, null=True)),
                ('Vch_Type', models.CharField(max_length=40, null=True)),
                ('Vch_No', models.IntegerField(default=0, null=True)),
                ('DEBIT', models.IntegerField(default=0, null=True)),
                ('Credit', models.IntegerField(default=0, null=True)),
                ('Open_Balance', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
