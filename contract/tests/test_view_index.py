from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..views import TQuotationListView

from datetime import datetime

from ..views import index
from ..models import t_quotation, t_company


class IndexTests(TestCase):
    def setUp(self):
        #テストデータ準備
        c1 = t_company.objects.create(
                    company_type  = 'NV', company_name = 'Nurinubi', tel  = "03-1111-1111",
                    delete_flg = False, ent_date = datetime.now(), ent_id = 1, upd_date = datetime.now(), upd_id = 1, upd_cnt = 0)
        c2 = t_company.objects.create(
                    company_type  = 'OT', company_name = 'TestCompany', tel  = "03-2222-2222",
                    delete_flg = False, ent_date = datetime.now(), ent_id = 1, upd_date = datetime.now(), upd_id = 1, upd_cnt = 0)
        self.q1 = t_quotation.objects.create(
                    my_company_id        = c1,
                    t_company_id           = c2,
                    contract_date_from   = datetime.strptime('2019-07-01', '%Y-%m-%d'),
                    contract_date_to       = datetime.strptime('2019-07-31', '%Y-%m-%d'),
                    delete_flg                 = False,
                    ent_date                  = datetime.now(),
                    ent_id                      = 1,
                    upd_cnt                   = 0)

        #ログイン状態にする
        self.client = Client()
        self.client.force_login(User.objects.create_user('tester'))

        #ページを表示
        url = reverse('contract:index')
        self.response = self.client.get(url)

    def test_status_code(self):
        """getで戻り値200とcontext確認"""
        self.assertEquals(self.response.status_code, 200)
        self.assertTrue('quotation_list' in self.response.context)

    def test_url_resolves(self):
        """resolveで正しいfuncが呼ばれる事を確認"""
        view = resolve('/contract/')
        #self.assertEquals(view.func, index)
        self.assertEquals(view.func.view_class, TQuotationListView)

    def test_contains_link_to_quotation(self):
        """1レコード目へのリンクが表示されている事"""
        quotation_url = reverse('contract:quotation', kwargs={'t_quotation_id': self.q1.pk})
        self.assertContains(self.response, 'href="{0}"'.format(quotation_url))

    def test_contains_menu_link(self):
        """メニュー部にリンクが表示されている事"""
        master_mainte_index_url = reverse('master_mainte:index')
        contract_index_url = reverse('contract:index')
        self.assertContains(self.response, 'href="{0}"'.format(master_mainte_index_url))
        self.assertContains(self.response, 'href="{0}"'.format(contract_index_url))
