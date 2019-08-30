# Generated by Django 2.2.3 on 2019-08-30 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master_mainte', '0002_t_staff_authuser_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_quotation',
            fields=[
                ('contract_type', models.CharField(blank=True, choices=[('1', '新規'), ('2', '更新')], db_column='contract_type', default='1', max_length=1, null=True, verbose_name='契約区分')),
                ('acceptance_or_retention', models.CharField(blank=True, choices=[('1', '労働者派遣契約'), ('2', '業務委託契約'), ('3', '業務請負契約'), ('4', '準委任契約'), ('5', 'システム・エンジニアリング・サービス契約(SES)'), ('9', 'その他')], db_column='acceptance_or_retention', default='1', max_length=1, null=True, verbose_name='新規更新区分')),
                ('recommision_type', models.CharField(blank=True, choices=[('0', '無し'), ('1', '有り')], db_column='recommision_type', default='0', max_length=1, null=True, verbose_name='再委託_区分')),
                ('recommision_text', models.TextField(blank=True, db_column='recommision_text', null=True, verbose_name='再委託_内容')),
                ('my_manager_is_stay', models.BooleanField(blank=True, db_column='my_manager_is_stay', default=False, null=True, verbose_name='弊社担当者_常駐区分')),
                ('title', models.CharField(blank=True, db_column='title', max_length=600, null=True, verbose_name='契約件名')),
                ('outline', models.TextField(blank=True, db_column='outline', null=True, verbose_name='業務内容')),
                ('base_contract', models.CharField(blank=True, db_column='base_contract', max_length=500, null=True, verbose_name='準拠する契約条件')),
                ('law_terms', models.CharField(blank=True, db_column='law_terms', max_length=500, null=True, verbose_name='該当法令')),
                ('contract_date_from', models.DateField(db_column='contract_date_from', verbose_name='契約期間_開始日')),
                ('contract_date_to', models.DateField(db_column='contract_date_to', verbose_name='契約期間_終了日')),
                ('man', models.DecimalField(blank=True, db_column='man', decimal_places=3, max_digits=7, null=True, verbose_name='契約人数')),
                ('man_month', models.DecimalField(blank=True, db_column='man_month', decimal_places=3, max_digits=7, null=True, verbose_name='工数合計(人月)')),
                ('tax_type', models.CharField(blank=True, choices=[('1', '税込'), ('2', '税別')], db_column='tax_type', default='2', max_length=1, null=True, verbose_name='税区分')),
                ('tax_rate', models.DecimalField(blank=True, db_column='tax_rate', decimal_places=3, max_digits=4, null=True, verbose_name='税率')),
                ('contract_exclude_tax', models.DecimalField(blank=True, db_column='contract_exclude_tax', decimal_places=3, max_digits=13, null=True, verbose_name='契約額合計(税抜)')),
                ('contract_tax_amount', models.DecimalField(blank=True, db_column='contract_tax_amount', decimal_places=3, max_digits=13, null=True, verbose_name='契約額合計(税額)')),
                ('contract_amount', models.DecimalField(blank=True, db_column='contract_amount', decimal_places=3, max_digits=13, null=True, verbose_name='契約額合計(合計)')),
                ('base_hour_min', models.DecimalField(blank=True, db_column='base_hour_min', decimal_places=0, max_digits=3, null=True, verbose_name='基準時間下限(時間)')),
                ('base_hour_max', models.DecimalField(blank=True, db_column='base_hour_max', decimal_places=0, max_digits=3, null=True, verbose_name='基準時間上限(時間)')),
                ('base_hour_text', models.CharField(blank=True, db_column='base_hour_text', max_length=500, null=True, verbose_name='基準時間_テキスト')),
                ('adjust_type', models.CharField(blank=True, choices=[('1', '不足時/超過時単価精算'), ('2', '均一単価精算'), ('3', '精算なし'), ('4', '不足時のみ精算'), ('5', '超過時のみ精算')], db_column='adjust_type', default='1', max_length=1, null=True, verbose_name='精算区分')),
                ('adjust_text', models.TextField(blank=True, db_column='adjust_text', null=True, verbose_name='精算内容')),
                ('expenses_payment_type', models.CharField(blank=True, choices=[('1', '交通費精算有り(現場までの交通費は契約額に含む)'), ('2', '交通費精算有り'), ('3', '交通費精算なし')], db_column='expenses_payment_type', default='1', max_length=1, null=True, verbose_name='交通費精算区分')),
                ('expenses_payment_text', models.TextField(blank=True, db_column='expenses_payment_text', null=True, verbose_name='交通費精算_テキスト')),
                ('unit_minutes', models.DecimalField(blank=True, db_column='unit_minutes', decimal_places=0, max_digits=3, null=True, verbose_name='計算単位(分)')),
                ('rounding_type', models.CharField(blank=True, choices=[('1', '四捨五入'), ('2', '切り捨て'), ('3', '切り上げ')], db_column='rounding_type', default='2', max_length=1, null=True, verbose_name='端数処理方法')),
                ('rounding_digit', models.DecimalField(blank=True, db_column='rounding_digit', decimal_places=0, max_digits=2, null=True, verbose_name='端数処理桁')),
                ('closing_day', models.CharField(blank=True, db_column='closing_day', max_length=500, null=True, verbose_name='締め日')),
                ('payment_term', models.CharField(blank=True, db_column='payment_term', max_length=500, null=True, verbose_name='支払サイト')),
                ('check_condition', models.CharField(blank=True, db_column='check_condition', max_length=500, null=True, verbose_name='検査条件')),
                ('deliverables', models.CharField(blank=True, db_column='deliverables', max_length=500, null=True, verbose_name='納入物')),
                ('delivery_place', models.CharField(blank=True, db_column='delivery_place', max_length=500, null=True, verbose_name='受渡場所')),
                ('workday', models.CharField(blank=True, db_column='workday', max_length=500, null=True, verbose_name='就業日')),
                ('holiday', models.CharField(blank=True, db_column='holiday', max_length=500, null=True, verbose_name='休日')),
                ('overtime_work', models.TextField(blank=True, db_column='overtime_work', null=True, verbose_name='時間外及び休日勤務')),
                ('work_hours_from', models.TimeField(blank=True, db_column='work_hours_from', null=True, verbose_name='就業時間_開始時間')),
                ('work_hours_to', models.TimeField(blank=True, db_column='work_hours_to', null=True, verbose_name='就業時間_終了時間')),
                ('work_hours', models.DecimalField(blank=True, db_column='work_hours', decimal_places=3, max_digits=5, null=True, verbose_name='就業時間_合計(時)')),
                ('work_hours_text', models.CharField(blank=True, db_column='work_hours_text', max_length=500, null=True, verbose_name='就業時間_テキスト')),
                ('interval_hours_from', models.TimeField(blank=True, db_column='interval_hours_from', null=True, verbose_name='休憩時間帯_開始時間')),
                ('interval_hours_to', models.TimeField(blank=True, db_column='interval_hours_to', null=True, verbose_name='休憩時間帯_終了時間')),
                ('interval_hours', models.DecimalField(blank=True, db_column='interval_hours', decimal_places=3, max_digits=5, null=True, verbose_name='休憩時間_合計(時)')),
                ('interval_hours_text', models.CharField(blank=True, db_column='interval_hours_text', max_length=500, null=True, verbose_name='休憩時間_テキスト')),
                ('accord_text', models.TextField(blank=True, db_column='accord_text', null=True, verbose_name='時間外労働協定_内容')),
                ('accord_date_from', models.DateTimeField(blank=True, db_column='accord_date_from', null=True, verbose_name='時間外労働協定_開始日')),
                ('accord_date_to', models.DateTimeField(blank=True, db_column='accord_date_to', null=True, verbose_name='時間外労働協定_終了日')),
                ('is_over_60', models.BooleanField(blank=True, db_column='is_over_60', default=False, null=True, verbose_name='60歳以上フラグ')),
                ('limits_only_no_term', models.BooleanField(blank=True, db_column='limits_only_no_term', default=False, null=True, verbose_name='無期限定フラグ')),
                ('with_hospital', models.BooleanField(blank=True, db_column='with_hospital', default=False, null=True, verbose_name='診療所有無フラグ')),
                ('with_locker', models.BooleanField(blank=True, db_column='with_locker', default=False, null=True, verbose_name='ロッカー有無フラグ')),
                ('with_resting_room', models.BooleanField(blank=True, db_column='with_resting_room', default=False, null=True, verbose_name='休憩室有無フラグ')),
                ('with_dressing_room', models.BooleanField(blank=True, db_column='with_dressing_room', default=False, null=True, verbose_name='更衣室有無フラグ')),
                ('with_kitchen', models.BooleanField(blank=True, db_column='with_kitchen', default=False, null=True, verbose_name='給湯室有無フラグ')),
                ('with_dining_room', models.BooleanField(blank=True, db_column='with_dining_room', default=False, null=True, verbose_name='食堂有無フラグ')),
                ('temp_to_perm_flg', models.BooleanField(blank=True, db_column='temp_to_perm_flg', default=False, null=True, verbose_name='紹介予定派遣有無フラグ')),
                ('temp_to_perm_text', models.TextField(blank=True, db_column='temp_to_perm_text', null=True, verbose_name='紹介予定派遣_内容')),
                ('special_accord_text', models.TextField(blank=True, db_column='special_accord_text', null=True, verbose_name='特別協定_内容')),
                ('special_accord_reason', models.TextField(blank=True, db_column='special_accord_reason', null=True, verbose_name='特別協定_適用事情')),
                ('holiday_work_text', models.TextField(blank=True, db_column='holiday_work_text', null=True, verbose_name='休日労働_限度')),
                ('prevent_disputes_text', models.TextField(blank=True, db_column='prevent_disputes_text', null=True, verbose_name='紛争防止措置_内容')),
                ('notes_1', models.TextField(blank=True, db_column='notes_1', null=True, verbose_name='備考1')),
                ('notes_2', models.TextField(blank=True, db_column='notes_2', null=True, verbose_name='備考2')),
                ('notes_3', models.TextField(blank=True, db_column='notes_3', null=True, verbose_name='備考3')),
                ('notes_4', models.TextField(blank=True, db_column='notes_4', null=True, verbose_name='備考4')),
                ('notes_5', models.TextField(blank=True, db_column='notes_5', null=True, verbose_name='備考5')),
                ('contract_file_path', models.FileField(blank=True, db_column='contract_file_path', null=True, upload_to='uploads/', verbose_name='契約書添付')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_quotation_id', models.AutoField(db_column='t_quotation_id', editable=False, primary_key=True, serialize=False, verbose_name='見積ID')),
                ('customer_quotation_no', models.CharField(blank=True, db_column='customer_quotation_no', max_length=50, null=True, verbose_name='客先見積書番号')),
                ('my_quotation_no', models.CharField(blank=True, db_column='my_quotation_no', max_length=50, null=True, verbose_name='弊社見積書番号')),
                ('issue_date', models.DateField(blank=True, db_column='issue_date', null=True, verbose_name='発行日')),
                ('valid_date', models.DateField(blank=True, db_column='valid_date', null=True, verbose_name='見積有効期限')),
                ('complaint_dept_id', models.ForeignKey(blank=True, db_column='complaint_dept_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_complaint_dept_id', to='master_mainte.t_dept', verbose_name='派遣先苦情申出先_組織ID')),
                ('complaint_manager_id', models.ForeignKey(blank=True, db_column='complaint_manager_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_complaint_manager_id', to='master_mainte.t_manager', verbose_name='派遣先苦情申出先_担当者ID')),
                ('instructor_dept_id', models.ForeignKey(blank=True, db_column='instructor_dept_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_instructor_dept_id', to='master_mainte.t_dept', verbose_name='指揮命令者_組織ID')),
                ('instructor_id', models.ForeignKey(blank=True, db_column='instructor_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_instructor_id', to='master_mainte.t_manager', verbose_name='指揮命令者_担当者ID')),
                ('manager_dept_id', models.ForeignKey(blank=True, db_column='manager_dept_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_manager_dept_id', to='master_mainte.t_dept', verbose_name='契約先(派遣先)担当者_組織ID')),
                ('manager_id', models.ForeignKey(blank=True, db_column='manager_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_manager_id', to='master_mainte.t_manager', verbose_name='契約先(派遣先)担当者_担当者ID')),
                ('my_company_id', models.ForeignKey(db_column='my_company_id', default='1', on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_my_company_id', to='master_mainte.t_company', verbose_name='弊社ID')),
                ('my_complaint_dept_id', models.ForeignKey(blank=True, db_column='my_complaint_dept_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_my_complaint_dept_id', to='master_mainte.t_dept', verbose_name='派遣元苦情申出先_組織ID')),
                ('my_complaint_manager_id', models.ForeignKey(blank=True, db_column='my_complaint_manager_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_my_complaint_manager_id', to='master_mainte.t_manager', verbose_name='派遣元苦情申出先_担当者ID')),
                ('my_manager_dept_id', models.ForeignKey(blank=True, db_column='my_manager_dept_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_my_manager_dept_id', to='master_mainte.t_dept', verbose_name='弊社担当者_組織ID')),
                ('my_manager_id', models.ForeignKey(blank=True, db_column='my_manager_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_my_manager_id', to='master_mainte.t_manager', verbose_name='弊社担当者_担当者ID')),
                ('privacy_dept_id', models.ForeignKey(blank=True, db_column='privacy_dept_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_privacy_dept_id', to='master_mainte.t_dept', verbose_name='個人情報管理責任者_組織ID')),
                ('privacy_manager_id', models.ForeignKey(blank=True, db_column='privacy_manager_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_privacy_manager_id', to='master_mainte.t_manager', verbose_name='個人情報管理責任者_担当者ID')),
                ('recommision_company_id', models.ForeignKey(blank=True, db_column='recommision_company_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_recommision_company_id', to='master_mainte.t_company', verbose_name='再委託_会社ID')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_t_company_id', to='master_mainte.t_company', verbose_name='客先会社ID')),
                ('t_workplace_id', models.ForeignKey(blank=True, db_column='t_workplace_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contract_t_quotation_related_t_workplace_id', to='master_mainte.t_workplace', verbose_name='就業場所ID')),
            ],
            options={
                'verbose_name': '見積テーブル',
                'verbose_name_plural': '見積テーブル',
                'ordering': ['-contract_date_from', 't_company_id'],
            },
        ),
        migrations.CreateModel(
            name='t_quotation_item',
            fields=[
                ('technical_level', models.CharField(blank=True, db_column='technical_level', max_length=20, null=True, verbose_name='職種')),
                ('man_month', models.DecimalField(blank=True, db_column='man_month', decimal_places=3, max_digits=7, null=True, verbose_name='工数(人月)')),
                ('tax_type', models.CharField(blank=True, choices=[('1', '税込'), ('2', '税別')], db_column='tax_type', max_length=1, null=True, verbose_name='税区分')),
                ('tax_rate', models.DecimalField(blank=True, db_column='tax_rate', decimal_places=3, max_digits=4, null=True, verbose_name='税率')),
                ('unitprice_exclude_tax', models.DecimalField(blank=True, db_column='unitprice_exclude_tax', decimal_places=3, max_digits=13, null=True, verbose_name='契約単価(税抜)')),
                ('contract_exclude_tax', models.DecimalField(blank=True, db_column='contract_exclude_tax', decimal_places=3, max_digits=13, null=True, verbose_name='契約額(税抜)')),
                ('contract_tax_amount', models.DecimalField(blank=True, db_column='contract_tax_amount', decimal_places=3, max_digits=13, null=True, verbose_name='契約額(税額)')),
                ('contract_amount', models.DecimalField(blank=True, db_column='contract_amount', decimal_places=3, max_digits=13, null=True, verbose_name='契約額(合計)')),
                ('unit_prices_minus', models.DecimalField(blank=True, db_column='unit_prices_minus', decimal_places=3, max_digits=13, null=True, verbose_name='精算単価_不足時')),
                ('unit_prices_plus', models.DecimalField(blank=True, db_column='unit_prices_plus', decimal_places=3, max_digits=13, null=True, verbose_name='精算単価_超過時')),
                ('notes', models.TextField(blank=True, db_column='notes', null=True, verbose_name='備考')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_quotation_item_id', models.AutoField(db_column='t_quotation_item_id', editable=False, primary_key=True, serialize=False, verbose_name='見積内訳ID')),
                ('t_quotation_id', models.ForeignKey(db_column='t_quotation_id', on_delete=django.db.models.deletion.PROTECT, to='contract.t_quotation', verbose_name='見積ID')),
                ('t_staff_id', models.ForeignKey(db_column='t_staff_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_staff', verbose_name='社員ID')),
            ],
            options={
                'verbose_name': '見積内訳テーブル',
                'verbose_name_plural': '見積内訳テーブル',
                'ordering': ['t_staff_id'],
            },
        ),
    ]
