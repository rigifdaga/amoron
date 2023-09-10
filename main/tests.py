from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_has_my_name(self):
        response = Client().get('/main/')
        self.assertContains(response, '<p>Created by: Rifda Aulia Nurbahri</p>')

    def test_main_has_my_class(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Class: PBP D')
