from django.db import models

# Create your models here.
'''from django.db import models
from django.conf import settings

class Account(models.Model):
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    company_name = models.CharField(max_length=200,blank=True, null=True)

    # Change later
    membership_level = models.CharField(max_length=200,blank=True, null=True)
    max_pages = models.CharField(max_length=200,blank=True, null=True)

    date_created = models.DateField(auto_now_add=True,blank=True, null=True)
    date_updated = models.DateField(auto_now=True,blank=True, null=True)'''

from django.db import models
from django.conf import settings

class Account(models.Model):
    # Basic User Information
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Account Status
    membership_level = models.IntegerField(default=0)
    account_status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Suspended', 'Suspended')], default='Active')
    max_pages = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    # Billing Information
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_state = models.CharField(max_length=100, blank=True, null=True)
    billing_country = models.CharField(max_length=100, blank=True, null=True)
    billing_postal_code = models.CharField(max_length=20, blank=True, null=True)
    credit_card_last4 = models.CharField(max_length=4, blank=True, null=True)
    subscription_plan = models.CharField(max_length=100, blank=True, null=True)
    subscription_status = models.CharField(max_length=50, blank=True, null=True)
    next_billing_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    last_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Usage Metrics
    last_login = models.DateTimeField(blank=True, null=True)
    total_logins = models.IntegerField(default=0)
    last_activity = models.DateTimeField(blank=True, null=True)
    total_pages_created = models.IntegerField(default=0)
    total_projects = models.IntegerField(default=0)
    total_files_uploaded = models.IntegerField(default=0)
    storage_used = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # in MB
    current_bandwidth_usage = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # in GB
    max_bandwidth_allowed = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # in GB
    
    # Engagement Metrics
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    newsletter_opt_in = models.BooleanField(default=True)
    total_support_tickets = models.IntegerField(default=0)
    total_feedback_submitted = models.IntegerField(default=0)
    average_support_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    average_time_on_site = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # in minutes
    last_marketing_email_opened = models.DateField(blank=True, null=True)
    last_product_update_read = models.DateField(blank=True, null=True)
    
    # Additional Custom Fields
    preferred_language = models.CharField(max_length=50, blank=True, null=True)
    referral_source = models.CharField(max_length=100, blank=True, null=True)
    account_manager = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'
