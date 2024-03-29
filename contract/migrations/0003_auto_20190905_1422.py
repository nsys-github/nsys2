# Generated by Django 2.2.3 on 2019-09-05 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_auto_20190905_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_quotation_item',
            name='contract_exclude_tax',
            field=models.DecimalField(blank=True, db_column='contract_exclude_tax', decimal_places=0, max_digits=13, null=True, verbose_name='契約額(税抜)'),
        ),
        migrations.AlterField(
            model_name='t_quotation_item',
            name='unit_prices_minus',
            field=models.DecimalField(blank=True, db_column='unit_prices_minus', decimal_places=0, max_digits=13, null=True, verbose_name='精算単価_不足時'),
        ),
        migrations.AlterField(
            model_name='t_quotation_item',
            name='unit_prices_plus',
            field=models.DecimalField(blank=True, db_column='unit_prices_plus', decimal_places=0, max_digits=13, null=True, verbose_name='精算単価_超過時'),
        ),
        migrations.AlterField(
            model_name='t_quotation_item',
            name='unitprice_exclude_tax',
            field=models.DecimalField(blank=True, db_column='unitprice_exclude_tax', decimal_places=0, max_digits=13, null=True, verbose_name='契約単価(税抜)'),
        ),
    ]
