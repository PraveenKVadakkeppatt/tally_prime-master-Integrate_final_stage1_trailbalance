# Generated by Django 4.0.5 on 2022-09-23 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_cash_bank_books_totalclosing_balance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='First_Voucher_Summary_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Particular', models.CharField(max_length=40, null=True)),
                ('Debit', models.IntegerField(default=0, null=True)),
                ('Credit', models.IntegerField(default=0, null=True)),
                ('Voucher_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tally_group')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Stock_Group_Summary_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Particular', models.CharField(max_length=40, null=True)),
                ('Quantity', models.CharField(max_length=40, null=True)),
                ('Rate', models.IntegerField(default=0, null=True)),
                ('Value', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Item_Monthly_Summary_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Open_Balance_Qty', models.IntegerField(default=0, null=True)),
                ('Open_Balance_Value', models.IntegerField(default=0, null=True)),
                ('Particular', models.CharField(max_length=50, null=True)),
                ('Inwards_Qty', models.IntegerField(default=0, null=True)),
                ('Inwards_Vlu', models.IntegerField(default=0, null=True)),
                ('Outwards_Qty', models.IntegerField(default=0, null=True)),
                ('Outwards_Vlu', models.IntegerField(default=0, null=True)),
                ('Closing_Bal_Qty', models.IntegerField(default=0, null=True)),
                ('Closing_Bal_Vlu', models.IntegerField(default=0, null=True)),
                ('Pro_Stock_Voucher_Forgn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.product_stock_group_summary_model')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Item_Voucher_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Particular', models.CharField(max_length=50, null=True)),
                ('Voucher_Type', models.CharField(max_length=40, null=True)),
                ('Vch_No', models.IntegerField(default=0, null=True)),
                ('Inwards_Qty', models.IntegerField(default=0, null=True)),
                ('Inwards_Vlu', models.IntegerField(default=0, null=True)),
                ('Outwards_Qty', models.IntegerField(default=0, null=True)),
                ('Outwards_Vlu', models.IntegerField(default=0, null=True)),
                ('Pro_Stock_Forgn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stock_item_monthly_summary_model')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Group_Summary_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Particular', models.CharField(max_length=40, null=True)),
                ('Quantity', models.IntegerField(default=0, null=True)),
                ('Rate', models.IntegerField(default=0, null=True)),
                ('Value', models.IntegerField(default=0, null=True)),
                ('Stock_Voucher_Forgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tally_group')),
            ],
        ),
        migrations.CreateModel(
            name='Second_Voucher_Summary_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Particular', models.CharField(max_length=40, null=True)),
                ('Debit', models.IntegerField(default=0, null=True)),
                ('Credit', models.IntegerField(default=0, null=True)),
                ('FVoucher_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.first_voucher_summary_model')),
            ],
        ),
        migrations.AddField(
            model_name='product_stock_group_summary_model',
            name='PStock_Voucher_Forgn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stock_group_summary_model'),
        ),
    ]