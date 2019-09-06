from .models import t_quotation
from django import forms
from datetime import date
import bootstrap_datepicker_plus as datetimepicker
from django.contrib.admin.widgets import AdminDateWidget

from bootstrap_datepicker_plus import DateTimePickerInput
from bootstrap_datepicker_plus import DatePickerInput

"""
class TQuotationCreationForm(CreationForm):
    class Meta(CreationForm):
        model = t_quotation
        fields = ('t_company_id', 'contract_date_from', 'contract_date_to', 'get_quotation_item_staff_name', 'get_link_to_quotation')


class  TQuotationChangeForm(ChangeForm):
    class Meta:
        model = t_quotation
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
"""

class SearchForm(forms.Form):

    t_company_id = forms.CharField(
        initial='',
        label='契約先社名',
        required = False, # 必須ではない
    )
    contract_date_from = forms.DateField(
        initial='',
        label='契約開始日b   ',
        required=False,  # 必須ではない
        input_formats=['%Y-%m-%d'],
        widget=DatePickerInput(format='%Y-%m-%d'),
    )
    """
    def clean_date(self):
        contract_date_from = self.cleaned_data['contract_date_from']
        #if date < datetime.date.today():
            #raise forms.ValidationError("The date cannot be in the past!")
        return contract_date_from
        """
