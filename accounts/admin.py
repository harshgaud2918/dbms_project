from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import*

admin.site.site_header='Estate Real'


# Register your models here.
admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Buyer)
admin.site.register(Owner)
admin.site.register(Tenant)
admin.site.register(Login)
admin.site.register(BuySellTransaction)
admin.site.register(User)
admin.site.register(RentTransaction)
admin.site.site_header='Estate Real'


