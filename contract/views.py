#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import t_quotation, t_manager
from datetime import datetime



WAREKI_START = {
   '令和': datetime(2019, 5, 1),
   '平成': datetime(1989, 1, 8),
   '昭和': datetime(1926, 12, 25)
}

@login_required
def index(request):
    quotation_list = t_quotation.objects.all()
    context = {'quotation_list': quotation_list}
    return render(request, 'contract/index.html', context)

### 見積書 ###
@login_required
def quotation(request, t_quotation_id):

    #メイン引数
    quotation = get_object_or_404(t_quotation, pk=t_quotation_id)

    #編集の必要な引数
    p_issue_date = convert_to_wareki(quotation.issue_date)
    p_my_address1 = quotation.my_company_id.get_address1()
    p_my_address2 = quotation.my_company_id.get_address2()
    p_my_company_name = quotation.my_company_id

    print(p_my_company_name)
    p_my_full_name = quotation.my_company_id.get_full_name()
    p_my_tel_fax = quotation.my_company_id.get_tel_fax()
    p_valid_date = convert_to_wareki(quotation.valid_date)
    l_outline = quotation.outline.splitlines()
    p_workplace = quotation.t_workplace_id.get_workplace_address()
    p_contract_date_from = convert_to_wareki(quotation.contract_date_from)
    p_contract_date_to = convert_to_wareki(quotation.contract_date_to)
    p_contract_exclude_tax = '{:,}'.format(int(quotation.contract_exclude_tax)) #整数にしてから、数値カンマ区切り
    p_rownum = len(quotation.t_quotation_item_set.all()) +2 +1  #見出し2行、下に余白1行
    p_manager_name = quotation.my_manager_id.get_full_name()
    p_tel_fax = quotation.my_company_id.get_tel_fax()
    l_notes_1 = quotation.notes_1.splitlines()

    #編集した引数をparm辞書に詰め直す
    parm = {'p_issue_date': p_issue_date,
                'p_my_address1': p_my_address1,
                'p_my_address2': p_my_address2,
                'p_my_full_name': p_my_full_name,
                'p_my_tel_fax': p_my_tel_fax,
                'p_valid_date': p_valid_date,
                'l_outline': l_outline,
                'p_workplace': p_workplace,
                'p_contract_date_from': p_contract_date_from,
                'p_contract_date_to': p_contract_date_to,
                'p_contract_exclude_tax': p_contract_exclude_tax,
                'p_rownum': p_rownum,
                'p_manager_name': p_manager_name,
                'p_tel_fax': p_tel_fax,
                'l_notes_1': l_notes_1}

    #render
    return render(request, 'contract/quotation.html', {'quotation': quotation, 'parm': parm})


### 契約書 ###
@login_required
def contract(request, t_quotation_id):
    return HttpResponse("You're at Contract on No. %s." % t_quotation_id)


### 派遣元管理台帳 ###
@login_required
def dispatch(request, t_quotation_id):
    return HttpResponse("You're at Dispatch on No. %s." % t_quotation_id)

def convert_to_wareki(dt):
    """西暦の年月日を和暦の年に変換する."""
    if not dt:
        return "-"

    y = dt.year
    m = dt.month
    d = dt.day
    try:
        y_m_d = datetime(y, m, d)
        if WAREKI_START['令和'] <= y_m_d:
            reiwa_year = WAREKI_START['令和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '令和'
        elif WAREKI_START['平成'] <= y_m_d:
            reiwa_year = WAREKI_START['平成'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '平成'
        elif WAREKI_START['昭和'] <= y_m_d:
            reiwa_year = WAREKI_START['昭和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '昭和'
        else:
            return '昭和以前'

        if year == 1:
            year = '元'

        return era_str + str(year) + '年' + str(m) + '月' + str(d) + '日'
    except ValueError as e:
        raise e
