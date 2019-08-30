from django.contrib import admin
from datetime import datetime
from .models import t_quotation, t_quotation_item


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


#Inline見積内訳テーブル
class TQuotationItemTable(admin.TabularInline):
    model = t_quotation_item
    extra = 1


# 見積テーブル
class TQuotation(admin.ModelAdmin):

    # 一覧項目
    list_display = ('t_company_id', 'contract_date_from', 'contract_date_to')
    # 検索項目
    search_fields = ['t_company_id__company_name__icontains']
    list_filter = ['t_company_id']

    #inlines
    inlines = [TQuotationItemTable]

    #inlineテーブルの更新
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in instances:
            # 編集不可項目の設定
            obj = set_not_editable_item(request, obj)
            obj.save()
        formset.save_m2m()

    #メインテーブルの更新
    def save_model(self, request, obj, form, change):
        """
        save_model関数のオーバライド
        """
        # 編集不可項目の設定
        obj = set_not_editable_item(request, obj)
        # 登録、更新
        super().save_model(request, obj, form, change)


admin.site.register(t_quotation, TQuotation)
