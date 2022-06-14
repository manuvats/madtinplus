from asyncio.windows_events import NULL
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from .utils import set_random_password


class Customer(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=50)
    phone = models.CharField(verbose_name = "Phone No.", max_length = 50, null=True)
    email = models.EmailField(verbose_name = "Email", max_length=100, null=True)
    org_name = models.CharField(verbose_name = "Organisation Name", max_length=100, null = True)
    #org_abbr = models.CharField(max_length=10, null = True)
    org_logo = models.ImageField(upload_to='logos', blank=True)
    subscription_start_date = models.DateField(verbose_name = "Subscription Start Date", auto_now_add = True)
    subscription_end_date = models.DateField(verbose_name = "Subscription End Date")
    #password = models.CharField(max_length=50, blank=True, null=True)
    
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.name

'''def pre_save_create_password(sender, instance, *args, **kwargs):
    if not instance.password:
        instance.password = set_random_password()'''


class Account(AbstractBaseUser):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    root_account = models.BooleanField(max_length=50, default=False)
    #id = models.BigAutoField(primary_key=True, null=False,)
    #account_id = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(verbose_name = "Name", max_length=50)
    phone = models.CharField(verbose_name = "Phone No.", max_length = 50, null=True)
    email = models.EmailField(verbose_name = "Email", max_length=100, null=True)  
    password = models.CharField(verbose_name = "Password", max_length=255, blank=True, null=True)
    account_type = models.CharField(max_length=50, choices=[
        ("survey", "SURVEY"), 
        ("sme", "SME"), 
        ("residents", "RESIDENTS")
        ])
    account_subscription_date = models.DateField(verbose_name = "Account Start Date", auto_now_add = True, null=True)
    account_expiry_date = models.DateField(verbose_name = "Account Expiry Date", null=True)
    last_login = models.DateTimeField(verbose_name="Last Login Time", null = True, auto_now=True)

    '''def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Account, self).save(*args, **kwargs)'''
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['customer', 'name', 'email', 'account_type']

    def __str__(self):
        return self.name 

'''def post_save_set_account_id(sender, instance, *args, **kwargs):
    if instance.account_id is None:
        instance.account_id = f'{instance.customer.id}_{instance.id}'
        instance.save()'''

#post_save.connect(post_save_set_account_id, sender=Account)
#pre_save.connect(pre_save_create_password, sender=Account)
