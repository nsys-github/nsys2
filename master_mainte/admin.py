from django.contrib import admin
from datetime import datetime
from .models import t_company, t_staff, t_mydept, t_staff_dept, t_staff_hire, t_dept, t_manager, t_workplace


## 編集不可項目の設定
def set_not_editable_item(request, obj):
    if  (obj.ent_date is None):
        ## 登録日時、登録者
        obj.ent_date = datetime.now()
        obj.ent_id = request.user.id
        ## 更新日時、更新者
        obj.upd_date = obj.ent_date
        obj.upd_id = request.user.id
    else:
        ## 更新日時、更新者
        obj.upd_date = datetime.now()
        obj.upd_id = request.user.id
        ## 更新回数
        obj.upd_cnt += 1
    return obj

# 会社テーブル
class TCompanyAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('company_name', 'company_name_k', 'tel', 'url')
    # 検索項目
    search_fields = ['company_name','company_name_k']

    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)

"""
class TMyDeptInline(admin.TabularInline):
    model = t_mydept
    extra = 1
"""


# 社員テーブル
class TStaffAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('staff_no', 'get_full_name', 'get_full_name_k', 'mail', 'joined_date', 'retired_date')
    # 検索項目
    search_fields = ['fname','lname']
    # 社員組織を社員ページで編集する
    # view手作りする必要がありそう
    # inlines = [TMyDeptInline]

    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


# 自社組織テーブル
class TMyDeptAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('jc_group_id', 'mydept_name', 'leader_t_staff_id')

    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


# 社員組織テーブル
class TStaffDeptAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('t_staff_id', 'trans_date', 't_mydept_id', 'position_id', 'is_active')
    # 検索項目
    search_fields = ['t_staff_id']
    """
    複数検索ボックスを表示するヒントは
    ブックマークにあり
    search_fields = ['t_mydept_id']
    search_fields = ['delete_flg']
    """
    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


# 社員契約テーブル
class TStaffHireAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('t_staff_id', 'change_date', 't_company_id',
                        'hire_type', 'term_date_from', 'term_date_to', 'is_active')
    # 検索項目
    search_fields = ['t_staff_id']
    """
    複数検索ボックスを表示するヒントは
    ブックマークにあり
    search_fields = ['t_mydept_id']
    search_fields = ['delete_flg']
    """
    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


# 組織テーブル
class TDeptAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('t_company_id', 'dept_name', 'address1', 'address2')
    # 検索項目
    search_fields = ['dept_name']
    list_filter = ['t_company_id']

    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


# 担当者テーブル
class TManagerAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('__str__', 'position')
    # 検索項目
    search_fields = ['get_full_name']
    list_filter = ['t_company_id']

    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


# 就業場所テーブル
class TWorkplaceAdmin(admin.ModelAdmin):

    # 一覧項目
    list_display = ('__str__', 'address1', 'address2')
    # 検索項目
    search_fields = ['workplace_name']
    list_filter = ['t_company_id']

    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


admin.site.register(t_company, TCompanyAdmin)
admin.site.register(t_staff, TStaffAdmin)
admin.site.register(t_mydept, TMyDeptAdmin)
admin.site.register(t_staff_dept, TStaffDeptAdmin)
admin.site.register(t_staff_hire, TStaffHireAdmin)
admin.site.register(t_dept, TDeptAdmin)
admin.site.register(t_manager, TManagerAdmin)
admin.site.register(t_workplace, TWorkplaceAdmin)
