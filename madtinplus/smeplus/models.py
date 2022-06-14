from django.db import models
from asyncio.windows_events import NULL
from django.db import models
from django.db.models.signals import post_save
from customer.models import Customer, Account


# Create your models here.
class Team(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #id = models.BigAutoField(primary_key=True, null=False,)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)  
    dob = models.DateField(null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    company_assigned = models.CharField(max_length=50, blank=True, null=True)
    tasks_count = models.IntegerField(null=True, default=0)
    current_task = models.CharField(max_length=50, blank=True, null=True)
    '''account_status = models.CharField(max_length=50, choices=[
        ("active", "Active"), 
        ("inactive", "Inactive"), 
        ("expired", "Expired")
        ])
    subscription_status = models.CharField(max_length=50, choices=[
        ("active", "Active"), 
        ("inactive", "Inactive"), 
        ("expired", "Expired")
        ])

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email']
'''
    def __str__(self):
        return self.name 

def post_save_set_member_id(sender, instance, *args, **kwargs):
    if instance.member_id is None:
        instance.member_id = f'{instance.account_id}_{instance.id}'
        instance.save()

post_save.connect(post_save_set_member_id, sender=Team)

class Clients(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #id = models.BigAutoField(primary_key=True, null=False,)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)  
    dob = models.DateField(null=True)
    company= models.CharField(max_length=50, blank=True, null=True)
    tasks_count = models.IntegerField(null=True, default=0)
    current_task = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name 
    
def post_save_set_client_id(sender, instance, *args, **kwargs):
    if instance.client_id is None:
        instance.client_id = f'{instance.account_id}_{instance.id}'
        instance.save()

post_save.connect(post_save_set_client_id, sender=Team)

class Leads(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #id = models.BigAutoField(primary_key=True, null=False,)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    lead_id = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)  
    dob = models.DateField(null=True)
    company= models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name 

def post_save_set_lead_id(sender, instance, *args, **kwargs):
    if instance.lead_id is None:
        instance.lead_id = f'{instance.account_id}_{instance.id}'
        instance.save()

post_save.connect(post_save_set_lead_id, sender=Team)
 
class Tasks(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateField()
    deadline = models.DateField()
    extensions = models.IntegerField()