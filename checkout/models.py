from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class TransactionStatus(models.IntegerChoices):
    Pending = 0, _('Pending')
    Completed = 1, _('Completed')


class PaymentMethod(models.IntegerChoices):
    Stripe = 1, 'Stripe'
    Paypal = 2, 'Paypal'


class Transaction(models.Model):
    session = models.CharField(max_length=255)
    amount = models.FloatField()
    items = models.JSONField(default=dict)
    customer = models.JSONField(default=dict)
    status = models.IntegerField(
        choices=TransactionStatus.choices, default=TransactionStatus.Pending
    )
    payment_method = models.IntegerField(
        choices=PaymentMethod.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def customer_name(self):
        return self.customer['first_name'] + ' ' + self.customer['last_name']

    @property
    def customer_email(self):
        return self.customer['email']
    
    def __str__(self):
        return str(self.status).replace('0', _('Pending')).replace("1",_('Completed')) + ' - ' + str(self.amount) + ' - ' + self.customer_name
    
    class Meta:
        verbose_name_plural = _("Transactions")
        verbose_name = _("Transaction")