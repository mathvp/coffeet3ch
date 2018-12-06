from django.test import TestCase
from coffeet3ch.subscriptions.forms import SubscriptionForm
#Biblioteca que simula um navegador para possibilitar a realização de testes em nosso código

class SubscribeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/inscricao/') #busca a página localizada em 127.0.0.1:1000/inscricao, pelo lado do cliente

    def test_get(self):
        """O teste deve obter o formulário de inscrição e retornar o status code 200"""
        self.assertEqual(200, self.response.status_code) #verifica se o código de status retornado é igual a 200

    def test_template(self):
        """Devemos utilizar o template subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """O código HTML deverá conter marcações Django de entrada (input) de dados!"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """O HTML deve conter csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """O formulário deve ter uma assinatura no seu contexto"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_field(self):
        """O formulário deverá ter 4 campos"""
        form = self.response.context['form']
        self.assertSequenceEqual(['nome', 'titulo', 'email', 'resumo'], list(form.fields))
