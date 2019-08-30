from django.db import models
from django.contrib.auth import get_user_model



class t_company(models.Model):
    class Meta:
        verbose_name = "0100_会社テーブル"
        verbose_name_plural = "0100_会社テーブル"
        ordering = ['company_type', 'company_name_k']

    #選択肢
    COMPANY_TYPE_CHOICES = [
        ('NV', 'Nurinubi/Veritec'),
        ('OT', 'それ以外'),
        ]

    def __str__(self):
        return self.company_name

    def get_tel_fax(self):
        if self.tel and self.fax:
            return "TEL:  " + self.tel + "        FAX:  " + self.fax
        elif self.tel:
            return "TEL:  " + self.tel + "        FAX:  -"
        elif self.fax:
            return "TEL:  - " + "        FAX:  " + self.fax
        else:
            return "TEL: - FAX: -"

    def get_address1(self):
        if self.address1:
            return self.address1
        else:
            return ""

    def get_address2(self):
        if self.address2:
            return self.address2
        else:
            return ""

    def get_full_name(self):
        if self.fname and self.lname:
            return self.fname + " " + self.lname
        elif self.fname:
            return self.fname
        elif self.lname:
            return self.lname
        else:
            return ""


    t_company_id = models.AutoField(db_column="t_company_id", verbose_name="会社ID", primary_key=True, null=False, blank=False, editable=False, )
    company_type = models.CharField(db_column="company_type", verbose_name="会社区分", max_length=2, null=False, blank=False, default="OT", choices=COMPANY_TYPE_CHOICES, )
    company_name = models.CharField(db_column="company_name", verbose_name="会社名称", max_length=150, null=False, blank=False, )
    company_name_k = models.CharField(db_column="company_name_k", verbose_name="会社名称カナ", max_length=150, null=True, blank=True, help_text="「株式会社」などを除いた部分をカタカナで。区切りは「・」を使用。(例)SBC株式会社　-> エス・ビー・シー", )
    postcode = models.CharField(db_column="postcode", verbose_name="郵便番号", max_length=10, null=True, blank=True, )
    address1 = models.CharField(db_column="address1", verbose_name="住所１", max_length=250, null=True, blank=True, )
    address2 = models.CharField(db_column="address2", verbose_name="住所２", max_length=250, null=True, blank=True, )
    tel = models.CharField(db_column="tel", verbose_name="TEL", max_length=15, null=False, blank=False, )
    fax = models.CharField(db_column="fax", verbose_name="FAX", max_length=15, null=True, blank=True, )
    url = models.URLField(db_column="url", verbose_name="URL", max_length=200, null=True, blank=True, )
    position = models.CharField(db_column="position", verbose_name="代表者役職名", max_length=100, null=True, blank=True, )
    fname = models.CharField(db_column="fname", verbose_name="代表者姓", max_length=90, null=True, blank=True, )
    lname = models.CharField(db_column="lname", verbose_name="代表者名", max_length=90, null=True, blank=True, )
    fname_k = models.CharField(db_column="fname_k", verbose_name="代表者姓カナ", max_length=90, null=True, blank=True, )
    lname_k = models.CharField(db_column="lname_k", verbose_name="代表者名カナ", max_length=90, null=True, blank=True, )
    fname_e = models.CharField(db_column="fname_e", verbose_name="代表者姓英字", max_length=90, null=True, blank=True, )
    lname_e = models.CharField(db_column="lname_e", verbose_name="代表者名英字", max_length=90, null=True, blank=True, )
    mail = models.EmailField(db_column="mail", verbose_name="代表者メールアドレス", max_length=254, null=True, blank=True, )
    dispatch_no = models.CharField(db_column="dispatch_no", verbose_name="一般労働者派遣事業許可番号", max_length=30, null=True, blank=True, )
    dispatch_date = models.DateField(db_column="dispatch_date", verbose_name="一般労働者派遣事業許可日", null=True, blank=True, )
    placement_no = models.CharField(db_column="placement_no", verbose_name="有料職業紹介事業許可番号", max_length=30, null=True, blank=True, )
    placement_date = models.DateField(db_column="placement_date", verbose_name="有料職業紹介事業許可日", null=True, blank=True, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=False, blank=False, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=False, blank=False, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )


class t_staff(models.Model):
    class Meta:
        verbose_name = "0200_社員テーブル"
        verbose_name_plural = "0200_社員テーブル"
        ordering = ['staff_no']

    def __str__(self):
        return self.staff_no + " " + self.fname + " " + self.lname

    def get_full_name(self):
        #フルネーム漢字
        return self.fname + " " + self.lname

    def get_full_name_k(self):
        #フルネームカナ
        f = self.fname_k
        l = self.lname_k
        if f is not None and l is not None:
            return f + " " + l
        else:
            return ""

    def get_full_name_e(self):
        #フルネーム英字
        f = self.fname_e
        l = self.lname_e
        if f is not None and l is not None:
            return f + " " + l
        else:
            return ""

    get_full_name.short_description = '社員名'
    get_full_name_k.short_description = '社員名カナ'
    get_full_name_e.short_description = '社員名英字'

    #選択肢
    GENDER_CHOICES = [ ('M', '男性'), ('F', '女性 '), ]
    RETIRED_REASON_CHOICES = [ ('1', '自己都合'), ('2', '会社都合'), ('3', '定年退職'), ]

    t_staff_id = models.AutoField(db_column="t_staff_id", verbose_name="社員ID", primary_key=True, null=False, blank=False, editable=False, )
    staff_no = models.CharField(db_column="staff_no", verbose_name="社員番号", unique=True, max_length=6, null=True, blank=True, )
    t_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="t_company_id", verbose_name="会社ID", null=False, blank=False, )
    fname = models.CharField(db_column="fname", verbose_name="社員姓", max_length=90, null=False, blank=False, )
    lname = models.CharField(db_column="lname", verbose_name="社員名", max_length=90, null=False, blank=False, )
    fname_k = models.CharField(db_column="fname_k", verbose_name="社員姓カナ", max_length=90, null=True, blank=True, )
    lname_k = models.CharField(db_column="lname_k", verbose_name="社員名カナ", max_length=90, null=True, blank=True, )
    fname_e = models.CharField(db_column="fname_e", verbose_name="社員姓英字", max_length=30, null=True, blank=True, )
    lname_e = models.CharField(db_column="lname_e", verbose_name="社員名英字", max_length=30, null=True, blank=True, )
    oname = models.CharField(db_column="oname", verbose_name="旧姓", max_length=90, null=True, blank=True, )
    oname_k = models.CharField(db_column="oname_k", verbose_name="旧姓カナ", max_length=90, null=True, blank=True, )
    oname_e = models.CharField(db_column="oname_e", verbose_name="旧姓英字", max_length=30, null=True, blank=True, )
    mail = models.EmailField(db_column="mail", verbose_name="メールアドレス", max_length=254, null=False, blank=False, )
    authuser_id = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, db_column="authuser_id", verbose_name="NSYSユーザーID", null=False, blank=False, default=1)
    slack_id = models.CharField(db_column="slack_id", verbose_name="slackID", max_length=100, null=True, blank=True, )
    image_filename = models.FileField(upload_to='uploads/', db_column="image_filename", verbose_name="顔写真パス", null=False, blank=True, )
    gender = models.CharField(db_column="gender", verbose_name="性別", max_length=1, null=False, blank=False, choices=GENDER_CHOICES, )
    birth_date = models.DateField(db_column="birth_date", verbose_name="生年月日", null=False, blank=False, )
    joined_date = models.DateField(db_column="joined_date", verbose_name="入社日", null=False, blank=False, )
    paid_holidays_base_date = models.DateField(db_column="paid_holidays_base_date", verbose_name="有休付与基準日", null=False, blank=False, )
    retired_date = models.DateField(db_column="retired_date", verbose_name="退職日", null=True, blank=True, )
    retired_type = models.CharField(db_column="retired_type", verbose_name="退職種別", max_length=1, null=True, blank=True, )
    retired_reason = models.CharField(db_column="retired_reason", verbose_name="退職理由", max_length=1000, null=True, blank=True, choices=RETIRED_REASON_CHOICES, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )


class t_mydept(models.Model):

    class Meta:
        verbose_name = "0300_自社組織テーブル"
        verbose_name_plural = "0300_自社組織テーブル"
        ordering = ['jc_group_id']

    def __str__(self):
        return self.mydept_name

    t_mydept_id = models.AutoField(db_column="t_mydept_id", verbose_name="自社組織ID", primary_key=True, null=False, blank=False, editable=False, )
    mydept_name = models.CharField(db_column="mydept_name", verbose_name="自社組織名称", max_length=150, null=False, blank=False, )
    leader_t_staff_id = models.ForeignKey(t_staff, on_delete=models.PROTECT, db_column="leader_t_staff_id", verbose_name="リーダ", null=False, blank=False, )
    jc_group_id = models.CharField(db_column="jc_group_id", verbose_name="ジョブカングループコード", unique=True, max_length=5, null=True, blank=True, )
    jc_parent_group_id = models.CharField(db_column="jc_parent_group_id", verbose_name="ジョブカン親グループコード", max_length=5, null=True, blank=True, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=False, blank=False, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=False, blank=False, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )


class t_staff_dept(models.Model):

    class Meta:
        verbose_name = "0400_社員組織テーブル"
        verbose_name_plural = "0400_社員組織テーブル"
        ordering = ['t_staff_id', '-trans_date']
        unique_together = ('t_staff_id', 'trans_date')

    def __str__(self):
        return self.t_staff_id.get_full_name() + " " + str(self.trans_date.strftime("%Y/%m/%d"))

    #選択肢
    POSITION_ID_CHOICES = [
                    ('10', '社長'),('20', '副社長'),('30', '営業'),('40', '事務'),
                    ('50', '部長'),('60', '課長'),('70', '係長'),('80', '社員'), ]

    t_staff_dept_id = models.AutoField(db_column="t_staff_dept_id", verbose_name="社員組織ID", primary_key=True, null=False, blank=False, editable=False, )
    t_staff_id = models.ForeignKey(t_staff, on_delete=models.PROTECT, db_column="t_staff_id", verbose_name="社員", null=False, blank=False, )
    t_mydept_id = models.ForeignKey(t_mydept, on_delete=models.PROTECT, db_column="t_mydept_id", verbose_name="組織", null=False, blank=False, )
    trans_date = models.DateField(db_column="trans_date", verbose_name="異動日", null=False, blank=False, )
    position_id = models.CharField(db_column="position_id", verbose_name="役職コード", max_length=2, null=False, blank=False, default="80", choices=POSITION_ID_CHOICES, )
    is_active = models.BooleanField(db_column="is_active", verbose_name="生存フラグ", null=False, blank=False, default=True, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )


class t_staff_hire(models.Model):

    class Meta:
        verbose_name = "0500_社員雇用契約テーブル"
        verbose_name_plural = "0500_社員雇用契約テーブル"
        ordering = ['t_staff_id', '-change_date']
        unique_together = ('t_staff_id', 'change_date')

    def __str__(self):
        return self.t_staff_id.get_full_name() + " " + str(self.change_date.strftime("%Y/%m/%d"))

    #選択肢
    HIRE_TYPE_CHOICES = [ ('0', '無期雇用'),('1', '有期雇用'), ]

    t_staff_hire_id = models.AutoField(db_column="t_staff_hire_id", verbose_name="社員雇用契約ID", primary_key=True, null=False, blank=False, editable=False, )
    t_staff_id = models.ForeignKey(t_staff, on_delete=models.PROTECT, db_column="t_staff_id", verbose_name="社員", null=False, blank=False, )
    t_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="t_company_id", verbose_name="会社ID", null=False, blank=False, default="1", )
    change_date = models.DateField(db_column="change_date", verbose_name="変更日", null=False, blank=False, )
    hire_type = models.CharField(db_column="hire_type", verbose_name="有期雇用・無期雇用", max_length=1, null=False, blank=False, default="0", choices=HIRE_TYPE_CHOICES, )
    term_date_from = models.DateField(db_column="term_date_from", verbose_name="有期雇用_開始日", null=True, blank=True, )
    term_date_to = models.DateField(db_column="term_date_to", verbose_name="有期雇用_終了日", null=True, blank=True, )
    is_active = models.BooleanField(db_column="is_active", verbose_name="生存フラグ", null=False, blank=False, default=True, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )



class t_dept(models.Model):

    class Meta:
        verbose_name = "0600_組織テーブル"
        verbose_name_plural = "0600_組織テーブル"
        ordering = ['t_company_id', 'dept_name']

    def __str__(self):
        return  self.t_company_id.company_name + " " + self.dept_name

    t_dept_id = models.AutoField(db_column="t_dept_id", verbose_name="組織ID", primary_key=True, null=False, blank=False, editable=False, )
    t_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="t_company_id", verbose_name="会社ID", null=False, blank=False, limit_choices_to={'company_type': 'OT'},)
    dept_name = models.CharField(db_column="dept_name", verbose_name="組織名称", max_length=150, null=False, blank=False, )
    postcode = models.CharField(db_column="postcode", verbose_name="郵便番号", max_length=10, null=True, blank=True, )
    address1 = models.CharField(db_column="address1", verbose_name="住所１", max_length=250, null=True, blank=True, )
    address2 = models.CharField(db_column="address2", verbose_name="住所２", max_length=250, null=True, blank=True, )
    tel = models.CharField(db_column="tel", verbose_name="TEL", max_length=15, null=True, blank=True, )
    fax = models.CharField(db_column="fax", verbose_name="FAX", max_length=15, null=True, blank=True, )
    station = models.CharField(db_column="station", verbose_name="最寄駅", max_length=250, null=True, blank=True, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )



class t_manager(models.Model):

    class Meta:
        verbose_name = "0700_担当者テーブル"
        verbose_name_plural = "0700_担当者テーブル"
        ordering = ['t_company_id', 't_dept_id', 'fname', 'lname']

    def __str__(self):
        return self.t_company_id.company_name + " / " \
                + self.t_dept_id.dept_name + " / " \
                + self.fname + " " + self.lname

    def get_full_name(self):
        #フルネーム漢字
        return self.fname + " " + self.lname

    get_full_name.short_description = '担当者名'

    t_manager_id = models.AutoField(db_column="t_manager_id", verbose_name="担当者ID", primary_key=True, null=False, blank=False, editable=False, )
    t_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="t_company_id", verbose_name="会社ID", null=False, blank=False, limit_choices_to={'company_type': 'OT'},)
    t_dept_id = models.ForeignKey(t_dept, on_delete=models.PROTECT, db_column="t_dept_id", verbose_name="組織ID", null=False, blank=False, )
    position = models.CharField(db_column="position", verbose_name="担当者役職名", max_length=100, null=True, blank=True, )
    fname = models.CharField(db_column="fname", verbose_name="担当者姓", max_length=90, null=False, blank=False, )
    lname = models.CharField(db_column="lname", verbose_name="担当者名", max_length=90, null=False, blank=False, )
    fname_k = models.CharField(db_column="fname_k", verbose_name="担当者姓カナ", max_length=90, null=True, blank=True, )
    lname_k = models.CharField(db_column="lname_k", verbose_name="担当者名カナ", max_length=90, null=True, blank=True, )
    fname_e = models.CharField(db_column="fname_e", verbose_name="担当者姓英字", max_length=90, null=True, blank=True, )
    lname_e = models.CharField(db_column="lname_e", verbose_name="担当者名英字", max_length=90, null=True, blank=True, )
    tel = models.CharField(db_column="tel", verbose_name="TEL", max_length=15, null=True, blank=True, )
    fax = models.CharField(db_column="fax", verbose_name="FAX", max_length=15, null=True, blank=True, )
    is_client = models.BooleanField(db_column="is_client", verbose_name="派遣先担当者フラグ", null=False, blank=False, default=False, )
    is_dispatch = models.BooleanField(db_column="is_dispatch", verbose_name="派遣元担当者フラグ", null=False, blank=False, default=False, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )



class t_workplace(models.Model):

    class Meta:
        verbose_name = "0800_就業場所テーブル"
        verbose_name_plural = "0800_就業場所テーブル"
        ordering = ['t_company_id', 'workplace_name']

    def __str__(self):
        return self.t_company_id.company_name + " " + self.workplace_name

    def get_workplace_name(self):
        return self.workplace_name

    def get_workplace_address(self):
        return self.address1+ " " + self.address2

    t_workplace_id = models.AutoField(db_column="t_workplace_id", verbose_name="就業場所ID", primary_key=True, null=False, blank=False, editable=False, )
    t_company_id = models.ForeignKey(t_company, on_delete=models.PROTECT, db_column="t_company_id", verbose_name="会社ID", null=False, blank=False, )
    workplace_name = models.CharField(db_column="workplace_name", verbose_name="就業場所_名称", max_length=500, null=False, blank=False, )
    postcode = models.CharField(db_column="postcode", verbose_name="郵便番号", max_length=10, null=True, blank=True, )
    address1 = models.CharField(db_column="address1", verbose_name="住所１", max_length=250, null=False, blank=False, )
    address2 = models.CharField(db_column="address2", verbose_name="住所２", max_length=250, null=True, blank=True, )
    tel = models.CharField(db_column="tel", verbose_name="TEL", max_length=15, null=True, blank=True, )
    fax = models.CharField(db_column="fax", verbose_name="FAX", max_length=15, null=True, blank=True, )
    station = models.CharField(db_column="station", verbose_name="最寄駅", max_length=250, null=True, blank=True, )
    delete_flg = models.BooleanField(db_column="delete_flg", verbose_name="削除フラグ", null=False, blank=False, default=False, )
    ent_date = models.DateTimeField(db_column="ent_date", verbose_name="登録日時", null=False, blank=False, editable=False, )
    ent_id = models.CharField(db_column="ent_id", verbose_name="登録者", max_length=6, null=False, blank=False, editable=False, )
    upd_date = models.DateTimeField(db_column="upd_date", verbose_name="更新日時", null=True, blank=True, editable=False, )
    upd_id = models.CharField(db_column="upd_id", verbose_name="更新者", max_length=6, null=True, blank=True, editable=False, )
    upd_cnt = models.IntegerField(db_column="upd_cnt", verbose_name="更新回数", null=False, blank=False, default=0, editable=False, )
