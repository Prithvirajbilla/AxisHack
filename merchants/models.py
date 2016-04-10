from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Axis(models.Model):
    customer_id = models.CharField(max_length=15)
    group_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    display_name = models.CharField(max_length=60)
    business_type = models.CharField(max_length=3)
    owner1_name = models.CharField(max_length=30)
    owner1_pan = models.CharField(max_length=10)
    is_id_proof1 = models.BooleanField()
    owner1_mobile = models.IntegerField()
    owner1_landline = models.IntegerField()
    owner2_name = models.CharField(max_length=30)
    owner2_pan = models.CharField(max_length=10)
    is_id_proof2 = models.BooleanField()
    owner2_mobile = models.IntegerField()
    owner2_landline = models.IntegerField()
    business_pincode = models.IntegerField()
    business_address = models.CharField(max_length=50)
    business_address2 = models.CharField(max_length=50)
    business_city = models.CharField(max_length=30)
    business_state = models.CharField(max_length=2)
    business_phone = models.IntegerField()
    business_email = models.EmailField(max_length=256)
    business_website_domain = models.EmailField(max_length=256)
    business_website_redirect = models.CharField(max_length=1024)
    create_time = models.DateField(auto_now_add=True)

class AxisChannels(models.Model):
    lead_id = models.OneToOneField(Axis)
    epay = models.BooleanField()
    ibank = models.BooleanField()
    mpos = models.BooleanField()

class AxisEpay(models.Model):
    lead_id = models.OneToOneField(Axis)
    test_date = models.DateTimeField()
    live_date = models.DateTimeField()
    initial_tcount = models.IntegerField()
    expected_tcount = models.IntegerField()

class AxisIBank(models.Model):
    lead_id = models.OneToOneField(Axis)
    mid = models.CharField(max_length=10)
    card = models.CharField(max_length=20)
    sec_enabled = models.BooleanField()
    disp_format = models.IntegerField()
    web_access = models.BooleanField()
    provider = models.IntegerField()

class Financials(models.Model):
    lead_id = models.OneToOneField(Axis)
    mode = models.IntegerField()#Account type
    current = models.BooleanField()#Existing current account or new
    account_no = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
