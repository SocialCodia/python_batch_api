# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    position = models.IntegerField()
    status = models.IntegerField()
    androidtoken = models.CharField(db_column='androidToken', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    webtoken = models.CharField(db_column='webToken', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin'


class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brands'


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class Creditors(models.Model):
    creditorid = models.AutoField(db_column='creditorId', primary_key=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='creditorName', max_length=50)  # Field name made lowercase.
    creditormobile = models.CharField(db_column='creditorMobile', max_length=15)  # Field name made lowercase.
    creditoraddress = models.CharField(db_column='creditorAddress', max_length=700)  # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'creditors'


class Creditpayments(models.Model):
    paymentid = models.AutoField(db_column='paymentId', primary_key=True)  # Field name made lowercase.
    paymentmode = models.CharField(db_column='paymentMode', max_length=100)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='paymentDate')  # Field name made lowercase.
    paymentamount = models.IntegerField(db_column='paymentAmount')  # Field name made lowercase.
    paymentreciever = models.IntegerField(db_column='paymentReciever')  # Field name made lowercase.
    creditid = models.IntegerField(db_column='creditId')  # Field name made lowercase.
    creditorid = models.IntegerField(db_column='creditorId')  # Field name made lowercase.
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'creditpayments'


class Credits(models.Model):
    creditid = models.AutoField(db_column='creditId', primary_key=True)  # Field name made lowercase.
    creditorid = models.IntegerField(db_column='creditorId')  # Field name made lowercase.
    salesid = models.CharField(db_column='salesId', max_length=500)  # Field name made lowercase.
    creditdescription = models.CharField(db_column='creditDescription', max_length=1000)  # Field name made lowercase.
    credittime = models.DateTimeField(db_column='creditTime')  # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'credits'


class Invoices(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=100)
    seller_id = models.IntegerField()
    invoice_date = models.DateField()
    invoice_url = models.CharField(max_length=600)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'invoices'


class Items(models.Model):
    pid = models.CharField(max_length=200)
    itemid = models.AutoField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=60)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='itemDescription', max_length=1000)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'items'


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'locations'


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_mode = models.CharField(max_length=100)
    payment_date = models.DateTimeField()
    payment_amount = models.IntegerField()
    payment_receiver = models.IntegerField()
    invoice_number = models.CharField(max_length=200)
    seller_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payments'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    item_id = models.IntegerField()
    size_id = models.IntegerField()
    brand_id = models.IntegerField()
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    location_id = models.IntegerField()
    product_manufacture = models.DateField()
    product_expire = models.DateField()
    barcode = models.CharField(db_column='barCode', max_length=200)  # Field name made lowercase.
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'


class ProductsRecord(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    item_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    size_id = models.IntegerField()
    brand_id = models.IntegerField()
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    location_id = models.IntegerField()
    product_manufacture = models.DateField()
    product_expire = models.DateField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products_record'


class Quantities(models.Model):
    quantity_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    product_id = models.IntegerField()
    size_id = models.IntegerField()
    brand_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quantities'


class Sellers(models.Model):
    sellerid = models.AutoField(db_column='sellerId', primary_key=True)  # Field name made lowercase.
    sellername = models.CharField(db_column='sellerName', max_length=50)  # Field name made lowercase.
    selleremail = models.CharField(db_column='sellerEmail', max_length=50)  # Field name made lowercase.
    sellercontact = models.CharField(db_column='sellerContact', max_length=12)  # Field name made lowercase.
    sellercontact1 = models.CharField(db_column='sellerContact1', max_length=12)  # Field name made lowercase.
    sellerimage = models.CharField(db_column='sellerImage', max_length=100)  # Field name made lowercase.
    selleraddress = models.CharField(db_column='sellerAddress', max_length=1000)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sellers'


class SellersSells(models.Model):
    sellers_sell_id = models.AutoField(primary_key=True)
    seller_id = models.IntegerField()
    invoice_number = models.CharField(max_length=100)
    product_id = models.IntegerField()
    sell_quantity = models.IntegerField()
    sell_discount = models.FloatField()
    sell_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellers_sells'


class Sells(models.Model):
    sell_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    sell_quantity = models.IntegerField()
    sell_discount = models.IntegerField()
    sell_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sells'


class Settings(models.Model):
    settingid = models.AutoField(db_column='settingId', primary_key=True)  # Field name made lowercase.
    productnoticecount = models.IntegerField(db_column='productNoticeCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'settings'


class Sizes(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=200)
    size_type = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sizes'


class StatusDemo(models.Model):
    productid = models.IntegerField(db_column='productId')  # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status_demo'
