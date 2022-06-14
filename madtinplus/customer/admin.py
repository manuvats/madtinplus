from django.contrib import admin
from customer.models import Customer, Account

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'org_name', 'org_logo', 
                    'subscription_start_date', 'subscription_end_date')
    search_fields = ('customer_id', 'name', 'email', 'subscription_start_date', 'subscription_end_date')
    readonly_fields = ('subscription_start_date',)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'root_account', 'name', 'email', 'password', 'account_type', 
                    'account_subscription_date', 'account_expiry_date')
    search_fields = ('customer_id', 'name', 'email', 'account_subscription_date', 'account_expiry_date')
    readonly_fields = ('account_subscription_date', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Account, AccountAdmin)
# Register your models here.
