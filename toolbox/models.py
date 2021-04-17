from django.db import models


class Client(models.Model):

    def get_model_name(self):
        name = str(self.__class__.__name__)
        return name

    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):

    def get_model_name(self):
        name = str(self.__class__.__name__)
        return name

    project = models.CharField(max_length=20)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.project} ({self.client})'


class Invoice(models.Model):

    def get_model_name(self):
        name = str(self.__class__.__name__)
        return name

    number = models.IntegerField(default='-')
    create_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        editable=False
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    amount = models.FloatField()
    currency = models.CharField(
        max_length=3,
        choices=[
            ('USD', 'USD'),
            ('EUR', 'EUR'),
            ('BYN', 'BYN')],
        default='USD'
    )

    def __str__(self):
        return f'{self.number}'


class Act(models.Model):

    def get_model_name(self):
        name = str(self.__class__.__name__)
        return name

    number = models.IntegerField(default='-')
    create_date = models.DateField(auto_now_add=True)
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        editable=False
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        editable=False
    )
    amount = models.FloatField(editable=False)
    currency = models.CharField(
        max_length=3,
        editable=False)

    def __str__(self):
        return f'{self.number}'
