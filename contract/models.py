from django.db import models
from django.contrib.auth import get_user_model

from master_mainte.models import t_company, t_dept, t_manager, t_workplace, t_staff


class t_contract_common(models.Model):

    class Meta:
        verbose_name = "契約共通テーブル"
        verbose_name_plural = "契約共通テーブル"
        ordering = ['-contract_date_from', 't_company_id']

        #抽象基底クラス(継承して使用する事)
        abstract = True

    #選択肢
    CONTRACT_TYPE_CHOICES = [ ('1', '新規'), ('2', '更新'), ]
    RECOMMISION_TYPE_CHOICES = [ ('0', '無し'), ('1', '有り'), ]
    TAX_TYPE_CHOICES = [ ('1', '税込'), ('2', '税別'), ]
    ROUNDING_TYPE_CHOICES = [ ('1', '四捨五入'), ('2', '切り捨て'), ('3', '切り上げ'), ]
    ACCEPTANCE_OR_RETENTION_CHOICES = [
                                                            ('1', '労働者派遣契約'),
                                                            ('2', '業務委託契約'),
                                                            ('3', '業務請負契約'),
                                                            ('4', '準委任契約'),
                                                            ('5', 'システム・エンジニアリング・サービス契約(SES)'),
                                                            ('9', 'その他'),
                                                            ]
    ADJUST_TYPE_CHOICES = [
                                            ('1', '不足時/超過時単価精算'),
                                            ('2', '均一単価精算'),
                                            ('3', '精算なし'),
                                            ('4', '不足時のみ精算'),
                                            ('5', '超過時のみ精算'),
                                            ]
    EXPENSES_PAYMENT_TYPE_CHOICES = [
                                                            ('1', '交通費精算有り(現場までの交通費は契約額に含む)'),
                                                            ('2', '交通費精算有り'),
                                                            ('3', '交通費精算なし'),
                                                            ]

    my_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="my_company_id", verbose_name="弊社ID", null=False, blank=False, default="1", related_name="%(app_label)s_%(class)s_related_my_company_id", )
    t_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="t_company_id", verbose_name="客先会社ID", null=False, blank=False, related_name="%(app_label)s_%(class)s_related_t_company_id", )
    contract_type = models.CharField(db_column="contract_type", verbose_name="契約区分", max_length=1, null=True, blank=True, default="1", choices=CONTRACT_TYPE_CHOICES, )
    acceptance_or_retention = models.CharField(db_column="acceptance_or_retention", verbose_name="新規更新区分", max_length=1, null=True, blank=True, default="1", choices=ACCEPTANCE_OR_RETENTION_CHOICES, )
    recommision_type = models.CharField(db_column="recommision_type", verbose_name="再委託_区分", max_length=1, null=True, blank=True, default="0", choices=RECOMMISION_TYPE_CHOICES, )
    recommision_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="recommision_company_id", verbose_name="再委託_会社ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_recommision_company_id", )
    recommision_text = models.TextField(db_column="recommision_text", verbose_name="再委託_内容", null=True, blank=True, )
    instructor_dept_id = models.ForeignKey(t_dept, on_delete=models.PROTECT, db_column="instructor_dept_id", verbose_name="指揮命令者_組織ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_instructor_dept_id", )
    instructor_id = models.ForeignKey(t_manager, on_delete=models.PROTECT, db_column="instructor_id", verbose_name="指揮命令者_担当者ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_instructor_id", )
    manager_dept_id = models.ForeignKey(t_dept, on_delete=models.PROTECT, db_column="manager_dept_id", verbose_name="契約先(派遣先)担当者_組織ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_manager_dept_id", )
    manager_id = models.ForeignKey(t_manager, on_delete=models.PROTECT, db_column="manager_id", verbose_name="契約先(派遣先)担当者_担当者ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_manager_id", )
    complaint_dept_id = models.ForeignKey(t_dept, on_delete=models.PROTECT, db_column="complaint_dept_id", verbose_name="派遣先苦情申出先_組織ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_complaint_dept_id", )
    complaint_manager_id = models.ForeignKey(t_manager, on_delete=models.PROTECT, db_column="complaint_manager_id", verbose_name="派遣先苦情申出先_担当者ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_complaint_manager_id", )
    my_manager_dept_id = models.ForeignKey(t_dept, on_delete=models.PROTECT, db_column="my_manager_dept_id", verbose_name="弊社担当者_組織ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_my_manager_dept_id", )
    my_manager_id = models.ForeignKey(t_manager, on_delete=models.PROTECT, db_column="my_manager_id", verbose_name="弊社担当者_担当者ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_my_manager_id", )
    my_manager_is_stay = models.BooleanField(db_column="my_manager_is_stay", verbose_name="弊社担当者_常駐区分", null=True, blank=True, default=False, )
    privacy_dept_id = models.ForeignKey(t_dept, on_delete=models.PROTECT, db_column="privacy_dept_id", verbose_name="個人情報管理責任者_組織ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_privacy_dept_id", )
    privacy_manager_id = models.ForeignKey(t_manager, on_delete=models.PROTECT, db_column="privacy_manager_id", verbose_name="個人情報管理責任者_担当者ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_privacy_manager_id", )
    my_complaint_dept_id = models.ForeignKey(t_dept, on_delete=models.PROTECT, db_column="my_complaint_dept_id", verbose_name="派遣元苦情申出先_組織ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_my_complaint_dept_id", )
    my_complaint_manager_id = models.ForeignKey(t_manager, on_delete=models.PROTECT, db_column="my_complaint_manager_id", verbose_name="派遣元苦情申出先_担当者ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_my_complaint_manager_id", )
    title = models.CharField(db_column="title", verbose_name="契約件名", max_length=600, null=True, blank=True, )
    outline = models.TextField(db_column="outline", verbose_name="業務内容", null=True, blank=True, )
    base_contract = models.CharField(db_column="base_contract", verbose_name="準拠する契約条件", max_length=500, null=True, blank=True, )
    law_terms = models.CharField(db_column="law_terms", verbose_name="該当法令", max_length=500, null=True, blank=True, )
    t_workplace_id = models.ForeignKey(t_workplace, on_delete=models.PROTECT, db_column="t_workplace_id", verbose_name="就業場所ID", null=True, blank=True, related_name="%(app_label)s_%(class)s_related_t_workplace_id", )
    contract_date_from = models.DateField(db_column="contract_date_from", verbose_name="契約期間_開始日", null=False, blank=False, )
    contract_date_to = models.DateField(db_column="contract_date_to", verbose_name="契約期間_終了日", null=False, blank=False, )
    man = models.DecimalField(db_column="man", verbose_name="契約人数", max_digits=7, decimal_places=3, null=True, blank=True, )
    man_month = models.DecimalField(db_column="man_month", verbose_name="工数合計(人月)", max_digits=7, decimal_places=3, null=True, blank=True, )
    tax_type = models.CharField(db_column="tax_type", verbose_name="税区分", max_length=1, null=True, blank=True, default="2", choices=TAX_TYPE_CHOICES, )
    tax_rate = models.DecimalField(db_column="tax_rate", verbose_name="税率", max_digits=4, decimal_places=3, null=True, blank=True, )
    contract_exclude_tax = models.DecimalField(db_column="contract_exclude_tax", verbose_name="契約額合計(税抜)", max_digits=13, decimal_places=3, null=True, blank=True, )
    contract_tax_amount = models.DecimalField(db_column="contract_tax_amount", verbose_name="契約額合計(税額)", max_digits=13, decimal_places=3, null=True, blank=True, )
    contract_amount = models.DecimalField(db_column="contract_amount", verbose_name="契約額合計(合計)", max_digits=13, decimal_places=3, null=True, blank=True, )
    base_hour_min = models.DecimalField(db_column="base_hour_min", verbose_name="基準時間下限(時間)", max_digits=3, decimal_places=0, null=True, blank=True, )
    base_hour_max = models.DecimalField(db_column="base_hour_max", verbose_name="基準時間上限(時間)", max_digits=3, decimal_places=0, null=True, blank=True, )
    base_hour_text = models.CharField(db_column="base_hour_text", verbose_name="基準時間_テキスト", max_length=500, null=True, blank=True, )
    adjust_type = models.CharField(db_column="adjust_type", verbose_name="精算区分", max_length=1, null=True, blank=True, default="1", choices=ADJUST_TYPE_CHOICES, )
    adjust_text = models.TextField(db_column="adjust_text", verbose_name="精算内容", null=True, blank=True, )
    expenses_payment_type = models.CharField(db_column="expenses_payment_type", verbose_name="交通費精算区分", max_length=1, null=True, blank=True, default="1", choices=EXPENSES_PAYMENT_TYPE_CHOICES, )
    expenses_payment_text = models.TextField(db_column="expenses_payment_text", verbose_name="交通費精算_テキスト", null=True, blank=True, )
    unit_minutes = models.DecimalField(db_column="unit_minutes", verbose_name="計算単位(分)", max_digits=3, decimal_places=0, null=True, blank=True, )
    rounding_type = models.CharField(db_column="rounding_type", verbose_name="端数処理方法", max_length=1, null=True, blank=True, default="2", choices=ROUNDING_TYPE_CHOICES, )
    rounding_digit = models.DecimalField(db_column="rounding_digit", verbose_name="端数処理桁", max_digits=2, decimal_places=0, null=True, blank=True, )
    closing_day = models.CharField(db_column="closing_day", verbose_name="締め日", max_length=500, null=True, blank=True, )
    payment_term = models.CharField(db_column="payment_term", verbose_name="支払サイト", max_length=500, null=True, blank=True, )
    check_condition = models.CharField(db_column="check_condition", verbose_name="検査条件", max_length=500, null=True, blank=True, )
    deliverables = models.CharField(db_column="deliverables", verbose_name="納入物", max_length=500, null=True, blank=True, )
    delivery_place = models.CharField(db_column="delivery_place", verbose_name="受渡場所", max_length=500, null=True, blank=True, )
    workday = models.CharField(db_column="workday", verbose_name="就業日", max_length=500, null=True, blank=True, )
    holiday = models.CharField(db_column="holiday", verbose_name="休日", max_length=500, null=True, blank=True, )
    overtime_work = models.TextField(db_column="overtime_work", verbose_name="時間外及び休日勤務", null=True, blank=True, )
    work_hours_from = models.TimeField(db_column="work_hours_from", verbose_name="就業時間_開始時間", null=True, blank=True, )
    work_hours_to = models.TimeField(db_column="work_hours_to", verbose_name="就業時間_終了時間", null=True, blank=True, )
    work_hours = models.DecimalField(db_column="work_hours", verbose_name="就業時間_合計(時)", max_digits=5, decimal_places=3, null=True, blank=True, )
    work_hours_text = models.CharField(db_column="work_hours_text", verbose_name="就業時間_テキスト", max_length=500, null=True, blank=True, )
    interval_hours_from = models.TimeField(db_column="interval_hours_from", verbose_name="休憩時間帯_開始時間", null=True, blank=True, )
    interval_hours_to = models.TimeField(db_column="interval_hours_to", verbose_name="休憩時間帯_終了時間", null=True, blank=True, )
    interval_hours = models.DecimalField(db_column="interval_hours", verbose_name="休憩時間_合計(時)", max_digits=5, decimal_places=3, null=True, blank=True, )
    interval_hours_text = models.CharField(db_column="interval_hours_text", verbose_name="休憩時間_テキスト", max_length=500, null=True, blank=True, )
    accord_text = models.TextField(db_column="accord_text", verbose_name="時間外労働協定_内容", null=True, blank=True, )
    accord_date_from = models.DateTimeField(db_column="accord_date_from", verbose_name="時間外労働協定_開始日", null=True, blank=True, )
    accord_date_to = models.DateTimeField(db_column="accord_date_to", verbose_name="時間外労働協定_終了日", null=True, blank=True, )
    is_over_60 = models.BooleanField(db_column="is_over_60", verbose_name="60歳以上フラグ", null=True, blank=True, default=False, )
    limits_only_no_term = models.BooleanField(db_column="limits_only_no_term", verbose_name="無期限定フラグ", null=True, blank=True, default=False, )
    with_hospital = models.BooleanField(db_column="with_hospital", verbose_name="診療所有無フラグ", null=True, blank=True, default=False, )
    with_locker = models.BooleanField(db_column="with_locker", verbose_name="ロッカー有無フラグ", null=True, blank=True, default=False, )
    with_resting_room = models.BooleanField(db_column="with_resting_room", verbose_name="休憩室有無フラグ", null=True, blank=True, default=False, )
    with_dressing_room = models.BooleanField(db_column="with_dressing_room", verbose_name="更衣室有無フラグ", null=True, blank=True, default=False, )
    with_kitchen = models.BooleanField(db_column="with_kitchen", verbose_name="給湯室有無フラグ", null=True, blank=True, default=False, )
    with_dining_room = models.BooleanField(db_column="with_dining_room", verbose_name="食堂有無フラグ", null=True, blank=True, default=False, )
    temp_to_perm_flg = models.BooleanField(db_column="temp_to_perm_flg", verbose_name="紹介予定派遣有無フラグ", null=True, blank=True, default=False, )
    temp_to_perm_text = models.TextField(db_column="temp_to_perm_text", verbose_name="紹介予定派遣_内容", null=True, blank=True, )
    special_accord_text = models.TextField(db_column="special_accord_text", verbose_name="特別協定_内容", null=True, blank=True, )
    special_accord_reason = models.TextField(db_column="special_accord_reason", verbose_name="特別協定_適用事情", null=True, blank=True, )
    holiday_work_text = models.TextField(db_column="holiday_work_text", verbose_name="休日労働_限度", null=True, blank=True, )
    prevent_disputes_text = models.TextField(db_column="prevent_disputes_text", verbose_name="紛争防止措置_内容", null=True, blank=True, )
    notes_1 = models.TextField(db_column="notes_1", verbose_name="備考1", null=True, blank=True, )
    notes_2 = models.TextField(db_column="notes_2", verbose_name="備考2", null=True, blank=True, )
    notes_3 = models.TextField(db_column="notes_3", verbose_name="備考3", null=True, blank=True, )
    notes_4 = models.TextField(db_column="notes_4", verbose_name="備考4", null=True, blank=True, )
    notes_5 = models.TextField(db_column="notes_5", verbose_name="備考5", null=True, blank=True, )
    contract_file_path = models.FileField(upload_to='uploads/', db_column="contract_file_path", verbose_name="契約書添付", null=True, blank=True, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )


class t_contract_item_common(models.Model):

    class Meta:
        verbose_name = "契約内訳共通テーブル"
        verbose_name_plural = "契約内訳共通テーブル"
        ordering = ['t_staff_id']

        #抽象基底クラス(継承して使用する事)
        abstract = True

    #選択肢
    TAX_TYPE_CHOICES = [ ('1', '税込'), ('2', '税別'), ]

    t_staff_id = models.ForeignKey(t_staff, on_delete=models.PROTECT, db_column="t_staff_id", verbose_name="社員ID", null=False, blank=False, )
    technical_level = models.CharField(db_column="technical_level", verbose_name="職種", max_length=20, null=True, blank=True, )
    man_month = models.DecimalField(db_column="man_month", verbose_name="工数(人月)", max_digits=7, decimal_places=3, null=True, blank=True, )
    tax_type = models.CharField(db_column="tax_type", verbose_name="税区分", max_length=1, null=True, blank=True, choices=TAX_TYPE_CHOICES, )
    tax_rate = models.DecimalField(db_column="tax_rate", verbose_name="税率", max_digits=4, decimal_places=3, null=True, blank=True, )
    unitprice_exclude_tax = models.DecimalField(db_column="unitprice_exclude_tax", verbose_name="契約単価(税抜)", max_digits=13, decimal_places=3, null=True, blank=True, )
    contract_exclude_tax = models.DecimalField(db_column="contract_exclude_tax", verbose_name="契約額(税抜)", max_digits=13, decimal_places=3, null=True, blank=True, )
    contract_tax_amount = models.DecimalField(db_column="contract_tax_amount", verbose_name="契約額(税額)", max_digits=13, decimal_places=3, null=True, blank=True, )
    contract_amount = models.DecimalField(db_column="contract_amount", verbose_name="契約額(合計)", max_digits=13, decimal_places=3, null=True, blank=True, )
    unit_prices_minus = models.DecimalField(db_column="unit_prices_minus", verbose_name="精算単価_不足時", max_digits=13, decimal_places=3, null=True, blank=True, )
    unit_prices_plus = models.DecimalField(db_column="unit_prices_plus", verbose_name="精算単価_超過時", max_digits=13, decimal_places=3, null=True, blank=True, )
    notes = models.TextField(db_column="notes", verbose_name="備考", null=True, blank=True, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )



#契約共通テーブル_継承テーブル
class t_quotation(t_contract_common):

    class Meta:
        verbose_name = "見積テーブル"
        verbose_name_plural = "見積テーブル"
        ordering = ['-contract_date_from', 't_company_id']

    def __str__(self):
        return self.t_company_id.company_name + " （" + str(self.contract_date_from.strftime("%Y/%m/%d")) + " - " + str(self.contract_date_to.strftime("%Y/%m/%d")) + ")"

    t_quotation_id = models.AutoField(db_column="t_quotation_id", verbose_name="見積ID", primary_key=True, null=False, blank=False, editable=False, )
    customer_quotation_no = models.CharField(db_column="customer_quotation_no", verbose_name="客先見積書番号", max_length=50, null=True, blank=True, )
    my_quotation_no = models.CharField(db_column="my_quotation_no", verbose_name="弊社見積書番号", max_length=50, null=True, blank=True, )
    issue_date = models.DateField(db_column="issue_date", verbose_name="発行日", null=True, blank=True, )
    valid_date = models.DateField(db_column="valid_date", verbose_name="見積有効期限", null=True, blank=True, )

#契約内訳共通テーブル_継承テーブル
class t_quotation_item(t_contract_item_common):

    class Meta:
        verbose_name = "見積内訳テーブル"
        verbose_name_plural = "見積内訳テーブル"
        ordering = ['t_staff_id']

#    def __str__(self):
#        return self.

    t_quotation_item_id = models.AutoField(db_column="t_quotation_item_id", verbose_name="見積内訳ID", primary_key=True, null=False, blank=False, editable=False, )
    t_quotation_id = models.ForeignKey(t_quotation, on_delete=models.PROTECT, db_column="t_quotation_id", verbose_name="見積ID", null=False, blank=False, )
