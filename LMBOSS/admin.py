from django.contrib import admin
from .models import PhoneNum, SimCard, Distributors


# Register your models here.

class PhoneNumAdmin(admin.ModelAdmin):
    list_display = ('number', 'get_operator_display', 'level', 'insert_dt')


class DistributorsAdmin(admin.ModelAdmin):
    list_display = ('distributors_id', 'dis_level', 'dis_legal_representative', 'img_show')


admin.site.register(PhoneNum, PhoneNumAdmin)
admin.site.register(SimCard)
admin.site.register(Distributors, DistributorsAdmin)
