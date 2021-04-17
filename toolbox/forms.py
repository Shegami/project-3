from django import forms
from toolbox.models import Client, Project, Invoice, Act


class NewClientForm(forms.ModelForm):

    def get_form_name(self):
        name = str(self.__class__.__name__)
        return name

    class Meta:
        model = Client
        fields = '__all__'


class NewProjectForm(forms.ModelForm):

    def get_form_name(self):
        name = str(self.__class__.__name__)
        return name

    class Meta:
        model = Project
        fields = '__all__'


class NewInvoiceForm(forms.ModelForm):

    def get_form_name(self):
        name = str(self.__class__.__name__)
        return name

    class Meta:
        model = Invoice
        fields = '__all__'


class NewActForm(forms.ModelForm):

    def get_form_name(self):
        name = str(self.__class__.__name__)
        return name

    class Meta:
        model = Act
        fields = '__all__'
