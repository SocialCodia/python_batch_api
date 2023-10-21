# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addons(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    unique_identifier = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    activated = models.IntegerField()
    image = models.CharField(max_length=1000, blank=True, null=True)
    purchase_code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addons'


class Addresses(models.Model):
    user_id = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField()
    city_id = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    set_default = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addresses'


class AffiliateConfigs(models.Model):
    type = models.CharField(max_length=1000, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_configs'


class AffiliateOptions(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    percentage = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_options'


class AffiliatePayments(models.Model):
    affiliate_user_id = models.IntegerField()
    amount = models.FloatField()
    payment_method = models.CharField(max_length=255)
    payment_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_payments'


class AffiliateUsers(models.Model):
    paypal_email = models.CharField(max_length=255, blank=True, null=True)
    bank_information = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    informations = models.TextField(blank=True, null=True)
    balance = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_users'


class AffiliateWithdrawRequests(models.Model):
    user_id = models.IntegerField()
    amount = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_withdraw_requests'


class AppTranslations(models.Model):
    lang = models.CharField(max_length=10, blank=True, null=True)
    lang_key = models.CharField(max_length=255, blank=True, null=True)
    lang_value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_translations'


class AttributeCategory(models.Model):
    category_id = models.IntegerField()
    attribute_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attribute_category'


class AttributeTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attribute_translations'


class AttributeValues(models.Model):
    attribute_id = models.IntegerField()
    value = models.CharField(max_length=255)
    color_code = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attribute_values'


class Attributes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attributes'


class BlogCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_categories'


class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.IntegerField()
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    banner = models.IntegerField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_img = models.IntegerField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs'


class BrandTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brand_translations'


class Brands(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=200)
    logo = models.CharField(max_length=100, blank=True, null=True)
    top = models.IntegerField()
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brands'


class BusinessSettings(models.Model):
    type = models.CharField(max_length=30)
    value = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_settings'


class Carts(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    temp_user_id = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    variation = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(blank=True, null=True)
    shipping_type = models.CharField(max_length=30)
    pickup_point = models.IntegerField(blank=True, null=True)
    discount = models.FloatField()
    product_referral_code = models.CharField(max_length=255, blank=True, null=True)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    coupon_applied = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carts'


class Categories(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    order_level = models.IntegerField()
    commision_rate = models.FloatField()
    banner = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    featured = models.IntegerField()
    top = models.IntegerField()
    digital = models.IntegerField()
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category_translations'


class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    state_id = models.IntegerField()
    cost = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class CityTranslations(models.Model):
    city_id = models.IntegerField()
    name = models.CharField(max_length=255)
    lang = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city_translations'


class Colors(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colors'


class CombinedOrders(models.Model):
    user_id = models.IntegerField()
    shipping_address = models.TextField(blank=True, null=True)
    grand_total = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'combined_orders'


class CommissionHistories(models.Model):
    order_id = models.IntegerField()
    order_detail_id = models.IntegerField()
    seller_id = models.IntegerField()
    admin_commission = models.FloatField()
    seller_earning = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commission_histories'


class Conversations(models.Model):
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    title = models.CharField(max_length=1000, blank=True, null=True)
    sender_viewed = models.IntegerField()
    receiver_viewed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conversations'


class Countries(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class CouponUsages(models.Model):
    user_id = models.IntegerField()
    coupon_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupon_usages'


class Coupons(models.Model):
    user_id = models.IntegerField()
    type = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    details = models.TextField()
    discount = models.FloatField()
    discount_type = models.CharField(max_length=100)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupons'


class Currencies(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    exchange_rate = models.FloatField()
    status = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'currencies'


class CustomerPackagePayments(models.Model):
    user_id = models.IntegerField()
    customer_package_id = models.IntegerField()
    payment_method = models.CharField(max_length=255)
    payment_details = models.TextField()
    approval = models.IntegerField()
    offline_payment = models.IntegerField()
    reciept = models.CharField(max_length=150)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_package_payments'


class CustomerPackageTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_package_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_package_translations'


class CustomerPackages(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    product_upload = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_packages'


class CustomerProductTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_product_id = models.BigIntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_product_translations'


class CustomerProducts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    published = models.IntegerField()
    status = models.IntegerField()
    added_by = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    subcategory_id = models.IntegerField(blank=True, null=True)
    subsubcategory_id = models.IntegerField(blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    photos = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_img = models.CharField(max_length=150, blank=True, null=True)
    conditon = models.CharField(max_length=50, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    video_provider = models.CharField(max_length=100, blank=True, null=True)
    video_link = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_img = models.CharField(max_length=150, blank=True, null=True)
    pdf = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_products'


class Customers(models.Model):
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customers'


class DeliveryBoyCollections(models.Model):
    user_id = models.IntegerField()
    collection_amount = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delivery_boy_collections'


class DeliveryBoyPayments(models.Model):
    user_id = models.IntegerField()
    payment = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delivery_boy_payments'


class DeliveryBoys(models.Model):
    user_id = models.IntegerField()
    total_collection = models.FloatField()
    total_earning = models.FloatField()
    monthly_salary = models.FloatField(blank=True, null=True)
    order_commission = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delivery_boys'


class DeliveryHistories(models.Model):
    delivery_boy_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField()
    delivery_status = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=20)
    earning = models.FloatField()
    collection = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'delivery_histories'


class FirebaseNotifications(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    item_type = models.CharField(max_length=255)
    item_type_id = models.IntegerField()
    receiver_id = models.IntegerField()
    is_read = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'firebase_notifications'


class FlashDealProducts(models.Model):
    flash_deal_id = models.IntegerField()
    product_id = models.IntegerField()
    discount = models.FloatField(blank=True, null=True)
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flash_deal_products'


class FlashDealTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    flash_deal_id = models.BigIntegerField()
    title = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flash_deal_translations'


class FlashDeals(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.IntegerField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    featured = models.IntegerField()
    background_color = models.CharField(max_length=255, blank=True, null=True)
    text_color = models.CharField(max_length=255, blank=True, null=True)
    banner = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flash_deals'


class HomeCategories(models.Model):
    category_id = models.IntegerField()
    subsubcategories = models.CharField(max_length=1000, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'home_categories'


class Languages(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    app_lang_code = models.CharField(max_length=255, blank=True, null=True)
    rtl = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'languages'


class Messages(models.Model):
    conversation_id = models.IntegerField()
    user_id = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Notifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=191)
    notifiable_type = models.CharField(max_length=191)
    notifiable_id = models.PositiveBigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OrderDetails(models.Model):
    order_id = models.IntegerField()
    seller_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField()
    variation = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    tax = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.IntegerField(blank=True, null=True)
    payment_status = models.CharField(max_length=10)
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    shipping_type = models.CharField(max_length=255, blank=True, null=True)
    pickup_point_id = models.IntegerField(blank=True, null=True)
    product_referral_code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_details'


class Orders(models.Model):
    combined_order_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    guest_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    assign_delivery_boy = models.IntegerField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    shipping_type = models.CharField(max_length=50)
    pickup_point_id = models.IntegerField()
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    grand_total = models.FloatField(blank=True, null=True)
    coupon_discount = models.FloatField()
    code = models.TextField(blank=True, null=True)
    tracking_code = models.CharField(max_length=255, blank=True, null=True)
    date = models.IntegerField()
    viewed = models.IntegerField()
    delivery_viewed = models.IntegerField()
    cancel_request = models.IntegerField()
    cancel_request_at = models.DateTimeField(blank=True, null=True)
    payment_status_viewed = models.IntegerField(blank=True, null=True)
    commission_calculated = models.IntegerField()
    delivery_history_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'


class OtpConfigurations(models.Model):
    type = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'otp_configurations'


class PageTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    page_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'page_translations'


class Pages(models.Model):
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_description = models.CharField(max_length=1000, blank=True, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)
    meta_image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pages'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'



class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=191)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class PickupPointTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    pickup_point_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    address = models.TextField()
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pickup_point_translations'


class PickupPoints(models.Model):
    staff_id = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    pick_up_status = models.IntegerField(blank=True, null=True)
    cash_on_pickup_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pickup_points'


class ProductStocks(models.Model):
    product_id = models.IntegerField()
    variant = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_stocks'


class ProductTaxes(models.Model):
    product_id = models.IntegerField()
    tax_id = models.IntegerField()
    tax = models.FloatField()
    tax_type = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_taxes'


class ProductTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_translations'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_id = models.IntegerField()
    name = models.CharField(max_length=200)
    added_by = models.CharField(max_length=6)
    user_id = models.IntegerField()
    category_id = models.IntegerField()
    brand_id = models.IntegerField(blank=True, null=True)
    photos = models.CharField(max_length=2000, blank=True, null=True)
    thumbnail_img = models.CharField(max_length=100, blank=True, null=True)
    video_provider = models.CharField(max_length=20, blank=True, null=True)
    video_link = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_price = models.FloatField()
    purchase_price = models.FloatField(blank=True, null=True)
    variant_product = models.IntegerField()
    attributes = models.CharField(max_length=1000)
    choice_options = models.TextField(blank=True, null=True)
    colors = models.TextField(blank=True, null=True)
    variations = models.TextField(blank=True, null=True)
    todays_deal = models.IntegerField()
    published = models.IntegerField()
    approved = models.IntegerField()
    stock_visibility_state = models.CharField(max_length=10)
    cash_on_delivery = models.IntegerField()
    featured = models.IntegerField()
    seller_featured = models.IntegerField()
    current_stock = models.IntegerField()
    unit = models.CharField(max_length=20, blank=True, null=True)
    min_qty = models.IntegerField()
    low_stock_quantity = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    discount_type = models.CharField(max_length=10, blank=True, null=True)
    discount_start_date = models.IntegerField(blank=True, null=True)
    discount_end_date = models.IntegerField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    tax_type = models.CharField(max_length=10, blank=True, null=True)
    shipping_type = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, null=True)
    shipping_cost = models.TextField(blank=True, null=True)
    is_quantity_multiplied = models.IntegerField()
    est_shipping_days = models.IntegerField(blank=True, null=True)
    num_of_sale = models.IntegerField()
    meta_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_img = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.CharField(max_length=255, blank=True, null=True)
    slug = models.TextField()
    rating = models.FloatField()
    barcode = models.CharField(max_length=255, blank=True, null=True)
    digital = models.IntegerField()
    auction_product = models.IntegerField()
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    external_link = models.CharField(max_length=500, blank=True, null=True)
    external_link_btn = models.CharField(max_length=255, blank=True, null=True)
    wholesale_product = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'


class ProxypayPayments(models.Model):
    payment_type = models.CharField(max_length=20)
    reference_id = models.CharField(max_length=20)
    order_id = models.IntegerField(blank=True, null=True)
    package_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    amount = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'proxypay_payments'


class Reviews(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField()
    comment = models.TextField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'


class RoleTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'role_translations'


class Roles(models.Model):
    name = models.CharField(max_length=30)
    permissions = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'


class Searches(models.Model):
    query = models.CharField(max_length=1000)
    count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'searches'


class SellerWithdrawRequests(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    message = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    viewed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'seller_withdraw_requests'


class Sellers(models.Model):
    user_id = models.IntegerField(unique=True)
    rating = models.FloatField()
    num_of_reviews = models.IntegerField()
    num_of_sale = models.IntegerField()
    verification_status = models.IntegerField()
    verification_info = models.TextField(blank=True, null=True)
    cash_on_delivery_status = models.IntegerField()
    admin_to_pay = models.FloatField()
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_acc_name = models.CharField(max_length=200, blank=True, null=True)
    bank_acc_no = models.CharField(max_length=50, blank=True, null=True)
    bank_routing_no = models.IntegerField(blank=True, null=True)
    bank_payment_status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sellers'


class Shops(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    sliders = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    google = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    pick_up_point_id = models.TextField(blank=True, null=True)
    shipping_cost = models.FloatField()
    delivery_pickup_latitude = models.FloatField(blank=True, null=True)
    delivery_pickup_longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'


class Staff(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff'


class States(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class SubCategories(models.Model):
    name = models.CharField(max_length=50)
    category_id = models.IntegerField()
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_categories'


class SubCategoryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    sub_category_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sub_category_translations'


class SubSubCategories(models.Model):
    sub_category_id = models.IntegerField()
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sub_sub_categories'


class SubSubCategoryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    sub_sub_category_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sub_sub_category_translations'


class Subscribers(models.Model):
    email = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscribers'


class Taxes(models.Model):
    name = models.CharField(max_length=255)
    tax_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'taxes'


class TicketReplies(models.Model):
    ticket_id = models.IntegerField()
    user_id = models.IntegerField()
    reply = models.TextField()
    files = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_replies'


class Tickets(models.Model):
    code = models.IntegerField()
    user_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    files = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    status = models.CharField(max_length=10)
    viewed = models.IntegerField()
    client_viewed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tickets'


class Transactions(models.Model):
    user_id = models.IntegerField()
    gateway = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    additional_content = models.TextField(blank=True, null=True)
    mpesa_request = models.CharField(max_length=255, blank=True, null=True)
    mpesa_receipt = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transactions'


class Translations(models.Model):
    lang = models.CharField(max_length=10, blank=True, null=True)
    lang_key = models.TextField(blank=True, null=True)
    lang_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'translations'


class Uploads(models.Model):
    file_original_name = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    external_link = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploads'


class Users(models.Model):
    referred_by = models.IntegerField(blank=True, null=True)
    provider_id = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.CharField(max_length=20)
    name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    verification_code = models.TextField(blank=True, null=True)
    new_email_verificiation_code = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    device_token = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=256, blank=True, null=True)
    avatar_original = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    balance = models.FloatField()
    banned = models.IntegerField()
    referral_code = models.CharField(max_length=255, blank=True, null=True)
    customer_package_id = models.IntegerField(blank=True, null=True)
    remaining_uploads = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Wallets(models.Model):
    user_id = models.IntegerField()
    amount = models.FloatField()
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wallets'


class Wishlists(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wishlists'
