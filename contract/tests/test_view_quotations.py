from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from ..models import t_quotation, t_company
from ..views import quotation

class LoginRequiredQuotationsTests(TestCase):
    def setUp(self):
        c1 = t_company.objects.create(
                    company_type  = 'NV', company_name = 'Nurinubi', tel  = "03-1111-1111",
                    delete_flg = False, ent_date = datetime.now(), ent_id = 1, upd_date = datetime.now(), upd_id = 1, upd_cnt = 0)
        c2 = t_company.objects.create(
                    company_type  = 'OT', company_name = 'TestCompany', tel  = "03-2222-2222",
                    delete_flg = False, ent_date = datetime.now(), ent_id = 1, upd_date = datetime.now(), upd_id = 1, upd_cnt = 0)
        q1 = t_quotation.objects.create(
                    my_company_id        = c1,
                    t_company_id           = c2,
                    contract_date_from   = datetime.strptime('2019-07-01', '%Y-%m-%d'),
                    contract_date_to       = datetime.strptime('2019-07-31', '%Y-%m-%d'),
                    delete_flg                 = False,
                    ent_date                  = datetime.now(),
                    ent_id                      = 1,
                    upd_cnt                   = 0)
        self.url = reverse('contract:quotation', kwargs={'t_quotation_id': q1.pk})
        self.response = self.client.get(self.url)

    #def test_home_status_code(self):
        """getで通常のアクセスを行う."""
        #self.assertEquals(self.response.status_code, 200)
        #self.assertQuerysetEqual(self.response.context['post_list'], [])

    def test_redirection(self):
        """ログインしていない場合にログインページにリダイレクトされることを確認"""
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
