from django.contrib import admin
from datetime import datetime
from .models import t_quotation, t_quotation_item, t_manager
from django import forms

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


def tagform_factory(company_id):
    class TagForm(forms.ModelForm):
        my_manager_id = forms.ModelChoiceField(
            queryset=t_manager.objects.filter(t_company_id=company_id)
        )
    return TagForm


#Inline見積内訳テーブル
class TQuotationItemTable(admin.StackedInline):
    model = t_quotation_item
    extra = 1
    fields = (
                 't_staff_id',
                 'unitprice_exclude_tax',
                 'contract_exclude_tax',
                 'unit_prices_minus',
                 'unit_prices_plus',
     )
# 見積テーブル
class TQuotation(admin.ModelAdmin):

    # 一覧項目
    list_display = ('t_company_id', 'contract_date_from', 'contract_date_to', 'get_quotation_item_staff_name', 'get_link_to_quotation')
    # 検索項目
    search_fields = ['t_company_id__company_name__icontains', 'my_quotation_no',]
    list_filter = [ 't_company_id', 'contract_date_from', 't_quotation_item__t_staff_id','contract_type', 'my_company_id', ]
    # 編集画面項目
    fields = (
                 't_company_id',
                 'my_quotation_no',
                 'issue_date',
                 'my_company_id',
                 'valid_date',
                 'contract_type',
                 'title',
                 'outline',
                 't_workplace_id',
                 'contract_date_from',
                 'contract_date_to',
                 'base_hour_min',
                 'base_hour_max',
                 'contract_exclude_tax',
                 'adjust_type',
                 'deliverables',
                 'check_condition',
                 'my_manager_id',
                 'expenses_payment_type',
                 ('recommision_type', 'recommision_company_id'),
                 'notes_1',
     )

    save_as = True

    #inlines
    inlines = [TQuotationItemTable]

    """def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "my_manager_id":
            kwargs["queryset"] = t_quotation.objects.filter(t_company_id=self.my_company_id)
        return super(TQuotation, self).formfield_for_foreignkey(db_field, request, **kwargs)"""

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None and obj.my_company_id is not None:
            kwargs['form'] = tagform_factory(obj.my_company_id)
        return super(TQuotation, self).get_form(request, obj, **kwargs)

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
