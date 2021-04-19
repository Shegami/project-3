from django.test import TestCase
from toolbox.models import Invoice, Client, Project, Act
from datetime import date


class HomeTest(TestCase):
    def test_home(self):
        result = self.client.get('/')
        TestCase.assertEqual(self, result.status_code, 200)


class CreateClientTest(TestCase):
    def setUp(self):
        Client.objects.create(
            name='TEST_CLIENT'
            )
        Project.objects.create(
            project='TEST_PROJECT',
            client=Client.objects.get(pk=1)
        )
        Invoice.objects.create(
            number=1,
            client=Client.objects.get(pk=1),
            project=Project.objects.get(pk=1),
            amount=1010.13,
            currency='USD'
        )
        Act.objects.create(
            number=1,
            client=Client.objects.get(pk=1),
            project=Project.objects.get(pk=1),
            invoice=Invoice.objects.get(pk=1),
            amount=1010.13,
            currency='USD'
        )

    def test_create_models(self):
        client_model = Client.objects.get(pk=1)
        project_model = Project.objects.get(pk=1)
        invoice_model = Invoice.objects.get(pk=1)
        act_model = Act.objects.get(pk=1)
        self.assertEqual(client_model.name, 'TEST_CLIENT')
        self.assertEqual(project_model.project, 'TEST_PROJECT')
        self.assertEqual(project_model.client, Client.objects.get(pk=1))
        self.assertEqual(invoice_model.number, 1)
        self.assertEqual(invoice_model.client, Client.objects.get(pk=1))
        self.assertEqual(invoice_model.project, Project.objects.get(pk=1))
        self.assertEqual(invoice_model.create_date, date.today())
        self.assertEqual(invoice_model.amount, 1010.13)
        self.assertEqual(invoice_model.currency, 'USD')
        self.assertEqual(act_model.number, 1)
        self.assertEqual(act_model.client, Client.objects.get(pk=1))
        self.assertEqual(act_model.project, Project.objects.get(pk=1))
        self.assertEqual(act_model.create_date, date.today())
        self.assertEqual(act_model.invoice, Invoice.objects.get(pk=1))
        self.assertEqual(act_model.amount, 1010.13)
        self.assertEqual(act_model.currency, 'USD')
