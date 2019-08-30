# Generated by Django 2.2.3 on 2019-08-30 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_company',
            fields=[
                ('t_company_id', models.AutoField(db_column='t_company_id', editable=False, primary_key=True, serialize=False, verbose_name='会社ID')),
                ('company_type', models.CharField(choices=[('NV', 'Nurinubi/Veritec'), ('OT', 'それ以外')], db_column='company_type', default='OT', max_length=2, verbose_name='会社区分')),
                ('company_name', models.CharField(db_column='company_name', max_length=150, verbose_name='会社名称')),
                ('company_name_k', models.CharField(blank=True, db_column='company_name_k', help_text='「株式会社」などを除いた部分をカタカナで。区切りは「・」を使用。(例)SBC株式会社\u3000-> エス・ビー・シー', max_length=150, null=True, verbose_name='会社名称カナ')),
                ('postcode', models.CharField(blank=True, db_column='postcode', max_length=10, null=True, verbose_name='郵便番号')),
                ('address1', models.CharField(blank=True, db_column='address1', max_length=250, null=True, verbose_name='住所１')),
                ('address2', models.CharField(blank=True, db_column='address2', max_length=250, null=True, verbose_name='住所２')),
                ('tel', models.CharField(db_column='tel', max_length=15, verbose_name='TEL')),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=15, null=True, verbose_name='FAX')),
                ('url', models.URLField(blank=True, db_column='url', null=True, verbose_name='URL')),
                ('position', models.CharField(blank=True, db_column='position', max_length=100, null=True, verbose_name='代表者役職名')),
                ('fname', models.CharField(blank=True, db_column='fname', max_length=90, null=True, verbose_name='代表者姓')),
                ('lname', models.CharField(blank=True, db_column='lname', max_length=90, null=True, verbose_name='代表者名')),
                ('fname_k', models.CharField(blank=True, db_column='fname_k', max_length=90, null=True, verbose_name='代表者姓カナ')),
                ('lname_k', models.CharField(blank=True, db_column='lname_k', max_length=90, null=True, verbose_name='代表者名カナ')),
                ('fname_e', models.CharField(blank=True, db_column='fname_e', max_length=90, null=True, verbose_name='代表者姓英字')),
                ('lname_e', models.CharField(blank=True, db_column='lname_e', max_length=90, null=True, verbose_name='代表者名英字')),
                ('mail', models.EmailField(blank=True, db_column='mail', max_length=254, null=True, verbose_name='代表者メールアドレス')),
                ('dispatch_no', models.CharField(blank=True, db_column='dispatch_no', max_length=30, null=True, verbose_name='一般労働者派遣事業許可番号')),
                ('dispatch_date', models.DateField(blank=True, db_column='dispatch_date', null=True, verbose_name='一般労働者派遣事業許可日')),
                ('placement_no', models.CharField(blank=True, db_column='placement_no', max_length=30, null=True, verbose_name='有料職業紹介事業許可番号')),
                ('placement_date', models.DateField(blank=True, db_column='placement_date', null=True, verbose_name='有料職業紹介事業許可日')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(db_column='upd_date', editable=False, verbose_name='更新日時')),
                ('upd_id', models.CharField(db_column='upd_id', editable=False, max_length=6, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
            ],
            options={
                'verbose_name': '0100_会社テーブル',
                'verbose_name_plural': '0100_会社テーブル',
                'ordering': ['company_type', 'company_name_k'],
            },
        ),
        migrations.CreateModel(
            name='t_dept',
            fields=[
                ('t_dept_id', models.AutoField(db_column='t_dept_id', editable=False, primary_key=True, serialize=False, verbose_name='組織ID')),
                ('dept_name', models.CharField(db_column='dept_name', max_length=150, verbose_name='組織名称')),
                ('postcode', models.CharField(blank=True, db_column='postcode', max_length=10, null=True, verbose_name='郵便番号')),
                ('address1', models.CharField(blank=True, db_column='address1', max_length=250, null=True, verbose_name='住所１')),
                ('address2', models.CharField(blank=True, db_column='address2', max_length=250, null=True, verbose_name='住所２')),
                ('tel', models.CharField(blank=True, db_column='tel', max_length=15, null=True, verbose_name='TEL')),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=15, null=True, verbose_name='FAX')),
                ('station', models.CharField(blank=True, db_column='station', max_length=250, null=True, verbose_name='最寄駅')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', limit_choices_to={'company_type': 'OT'}, on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID')),
            ],
            options={
                'verbose_name': '0600_組織テーブル',
                'verbose_name_plural': '0600_組織テーブル',
                'ordering': ['t_company_id', 'dept_name'],
            },
        ),
        migrations.CreateModel(
            name='t_staff',
            fields=[
                ('t_staff_id', models.AutoField(db_column='t_staff_id', editable=False, primary_key=True, serialize=False, verbose_name='社員ID')),
                ('staff_no', models.CharField(blank=True, db_column='staff_no', max_length=6, null=True, unique=True, verbose_name='社員番号')),
                ('fname', models.CharField(db_column='fname', max_length=90, verbose_name='社員姓')),
                ('lname', models.CharField(db_column='lname', max_length=90, verbose_name='社員名')),
                ('fname_k', models.CharField(blank=True, db_column='fname_k', max_length=90, null=True, verbose_name='社員姓カナ')),
                ('lname_k', models.CharField(blank=True, db_column='lname_k', max_length=90, null=True, verbose_name='社員名カナ')),
                ('fname_e', models.CharField(blank=True, db_column='fname_e', max_length=30, null=True, verbose_name='社員姓英字')),
                ('lname_e', models.CharField(blank=True, db_column='lname_e', max_length=30, null=True, verbose_name='社員名英字')),
                ('oname', models.CharField(blank=True, db_column='oname', max_length=90, null=True, verbose_name='旧姓')),
                ('oname_k', models.CharField(blank=True, db_column='oname_k', max_length=90, null=True, verbose_name='旧姓カナ')),
                ('oname_e', models.CharField(blank=True, db_column='oname_e', max_length=30, null=True, verbose_name='旧姓英字')),
                ('mail', models.EmailField(db_column='mail', max_length=254, verbose_name='メールアドレス')),
                ('slack_id', models.CharField(blank=True, db_column='slack_id', max_length=100, null=True, verbose_name='slackID')),
                ('image_filename', models.FileField(blank=True, db_column='image_filename', upload_to='uploads/', verbose_name='顔写真パス')),
                ('gender', models.CharField(choices=[('M', '男性'), ('F', '女性 ')], db_column='gender', max_length=1, verbose_name='性別')),
                ('birth_date', models.DateField(db_column='birth_date', verbose_name='生年月日')),
                ('joined_date', models.DateField(db_column='joined_date', verbose_name='入社日')),
                ('paid_holidays_base_date', models.DateField(db_column='paid_holidays_base_date', verbose_name='有休付与基準日')),
                ('retired_date', models.DateField(blank=True, db_column='retired_date', null=True, verbose_name='退職日')),
                ('retired_type', models.CharField(blank=True, db_column='retired_type', max_length=1, null=True, verbose_name='退職種別')),
                ('retired_reason', models.CharField(blank=True, choices=[('1', '自己都合'), ('2', '会社都合'), ('3', '定年退職')], db_column='retired_reason', max_length=1000, null=True, verbose_name='退職理由')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID')),
            ],
            options={
                'verbose_name': '0200_社員テーブル',
                'verbose_name_plural': '0200_社員テーブル',
                'ordering': ['staff_no'],
            },
        ),
        migrations.CreateModel(
            name='t_workplace',
            fields=[
                ('t_workplace_id', models.AutoField(db_column='t_workplace_id', editable=False, primary_key=True, serialize=False, verbose_name='就業場所ID')),
                ('workplace_name', models.CharField(db_column='workplace_name', max_length=500, verbose_name='就業場所_名称')),
                ('postcode', models.CharField(blank=True, db_column='postcode', max_length=10, null=True, verbose_name='郵便番号')),
                ('address1', models.CharField(db_column='address1', max_length=250, verbose_name='住所１')),
                ('address2', models.CharField(blank=True, db_column='address2', max_length=250, null=True, verbose_name='住所２')),
                ('tel', models.CharField(blank=True, db_column='tel', max_length=15, null=True, verbose_name='TEL')),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=15, null=True, verbose_name='FAX')),
                ('station', models.CharField(blank=True, db_column='station', max_length=250, null=True, verbose_name='最寄駅')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID')),
            ],
            options={
                'verbose_name': '0800_就業場所テーブル',
                'verbose_name_plural': '0800_就業場所テーブル',
                'ordering': ['t_company_id', 'workplace_name'],
            },
        ),
        migrations.CreateModel(
            name='t_mydept',
            fields=[
                ('t_mydept_id', models.AutoField(db_column='t_mydept_id', editable=False, primary_key=True, serialize=False, verbose_name='自社組織ID')),
                ('mydept_name', models.CharField(db_column='mydept_name', max_length=150, verbose_name='自社組織名称')),
                ('jc_group_id', models.CharField(blank=True, db_column='jc_group_id', max_length=5, null=True, unique=True, verbose_name='ジョブカングループコード')),
                ('jc_parent_group_id', models.CharField(blank=True, db_column='jc_parent_group_id', max_length=5, null=True, verbose_name='ジョブカン親グループコード')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(db_column='upd_date', editable=False, verbose_name='更新日時')),
                ('upd_id', models.CharField(db_column='upd_id', editable=False, max_length=6, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('leader_t_staff_id', models.ForeignKey(db_column='leader_t_staff_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_staff', verbose_name='リーダ')),
            ],
            options={
                'verbose_name': '0300_自社組織テーブル',
                'verbose_name_plural': '0300_自社組織テーブル',
                'ordering': ['jc_group_id'],
            },
        ),
        migrations.CreateModel(
            name='t_manager',
            fields=[
                ('t_manager_id', models.AutoField(db_column='t_manager_id', editable=False, primary_key=True, serialize=False, verbose_name='担当者ID')),
                ('position', models.CharField(blank=True, db_column='position', max_length=100, null=True, verbose_name='担当者役職名')),
                ('fname', models.CharField(db_column='fname', max_length=90, verbose_name='担当者姓')),
                ('lname', models.CharField(db_column='lname', max_length=90, verbose_name='担当者名')),
                ('fname_k', models.CharField(blank=True, db_column='fname_k', max_length=90, null=True, verbose_name='担当者姓カナ')),
                ('lname_k', models.CharField(blank=True, db_column='lname_k', max_length=90, null=True, verbose_name='担当者名カナ')),
                ('fname_e', models.CharField(blank=True, db_column='fname_e', max_length=90, null=True, verbose_name='担当者姓英字')),
                ('lname_e', models.CharField(blank=True, db_column='lname_e', max_length=90, null=True, verbose_name='担当者名英字')),
                ('tel', models.CharField(blank=True, db_column='tel', max_length=15, null=True, verbose_name='TEL')),
                ('fax', models.CharField(blank=True, db_column='fax', max_length=15, null=True, verbose_name='FAX')),
                ('is_client', models.BooleanField(db_column='is_client', default=False, verbose_name='派遣先担当者フラグ')),
                ('is_dispatch', models.BooleanField(db_column='is_dispatch', default=False, verbose_name='派遣元担当者フラグ')),
                ('delete_flg', models.BooleanField(db_column='delete_flg', default=False, verbose_name='削除フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', limit_choices_to={'company_type': 'OT'}, on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID')),
                ('t_dept_id', models.ForeignKey(db_column='t_dept_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_dept', verbose_name='組織ID')),
            ],
            options={
                'verbose_name': '0700_担当者テーブル',
                'verbose_name_plural': '0700_担当者テーブル',
                'ordering': ['t_company_id', 't_dept_id', 'fname', 'lname'],
            },
        ),
        migrations.CreateModel(
            name='t_staff_hire',
            fields=[
                ('t_staff_hire_id', models.AutoField(db_column='t_staff_hire_id', editable=False, primary_key=True, serialize=False, verbose_name='社員雇用契約ID')),
                ('change_date', models.DateField(db_column='change_date', verbose_name='変更日')),
                ('hire_type', models.CharField(choices=[('0', '無期雇用'), ('1', '有期雇用')], db_column='hire_type', default='0', max_length=1, verbose_name='有期雇用・無期雇用')),
                ('term_date_from', models.DateField(blank=True, db_column='term_date_from', null=True, verbose_name='有期雇用_開始日')),
                ('term_date_to', models.DateField(blank=True, db_column='term_date_to', null=True, verbose_name='有期雇用_終了日')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, verbose_name='生存フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_company_id', models.ForeignKey(db_column='t_company_id', default='1', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_company', verbose_name='会社ID')),
                ('t_staff_id', models.ForeignKey(db_column='t_staff_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_staff', verbose_name='社員')),
            ],
            options={
                'verbose_name': '0500_社員雇用契約テーブル',
                'verbose_name_plural': '0500_社員雇用契約テーブル',
                'ordering': ['t_staff_id', '-change_date'],
                'unique_together': {('t_staff_id', 'change_date')},
            },
        ),
        migrations.CreateModel(
            name='t_staff_dept',
            fields=[
                ('t_staff_dept_id', models.AutoField(db_column='t_staff_dept_id', editable=False, primary_key=True, serialize=False, verbose_name='社員組織ID')),
                ('trans_date', models.DateField(db_column='trans_date', verbose_name='異動日')),
                ('position_id', models.CharField(choices=[('10', '社長'), ('20', '副社長'), ('30', '営業'), ('40', '事務'), ('50', '部長'), ('60', '課長'), ('70', '係長'), ('80', '社員')], db_column='position_id', default='80', max_length=2, verbose_name='役職コード')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, verbose_name='生存フラグ')),
                ('ent_date', models.DateTimeField(db_column='ent_date', editable=False, verbose_name='登録日時')),
                ('ent_id', models.CharField(db_column='ent_id', editable=False, max_length=6, verbose_name='登録者')),
                ('upd_date', models.DateTimeField(blank=True, db_column='upd_date', editable=False, null=True, verbose_name='更新日時')),
                ('upd_id', models.CharField(blank=True, db_column='upd_id', editable=False, max_length=6, null=True, verbose_name='更新者')),
                ('upd_cnt', models.IntegerField(db_column='upd_cnt', default=0, editable=False, verbose_name='更新回数')),
                ('t_mydept_id', models.ForeignKey(db_column='t_mydept_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_mydept', verbose_name='組織')),
                ('t_staff_id', models.ForeignKey(db_column='t_staff_id', on_delete=django.db.models.deletion.PROTECT, to='master_mainte.t_staff', verbose_name='社員')),
            ],
            options={
                'verbose_name': '0400_社員組織テーブル',
                'verbose_name_plural': '0400_社員組織テーブル',
                'ordering': ['t_staff_id', '-trans_date'],
                'unique_together': {('t_staff_id', 'trans_date')},
            },
        ),
    ]
