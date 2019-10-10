from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


# Create your models here.
class PhoneNum(models.Model):
    """
    号码表
    """
    OPERATOR_CHOICES = [
        ('TELE', '电信'),
        ('MOB', '移动'),
        ('UNI', '联通')
    ]
    number = models.CharField('电话号码', max_length=11, primary_key=True)
    status = models.SmallIntegerField('号码状态', default=1)
    level = models.SmallIntegerField('号码等级', default=9)
    operator = models.CharField('运营商', max_length=6, choices=OPERATOR_CHOICES)
    segment = models.CharField('号段', max_length=7)
    attribution = models.CharField('归属地', max_length=3)
    insert_dt = models.DateTimeField('导入时间', default=timezone.now)
    update_dt = models.DateTimeField('更新时间', auto_now=True)

    def get_operator_display(self):
        return self.get_operator_display()

    get_operator_display.short_description = '运营商'


class SimCard(models.Model):
    """
    SIM卡表
    """
    SIM_OPERATOR_CHOICES = [
        ('TELE', '电信'),
        ('MOB', '移动'),
        ('UNI', '联通')
    ]
    iccid = models.CharField('SIM卡卡号', max_length=20, primary_key=True)
    sim_status = models.BooleanField('卡状态', default=True)
    sim_operator = models.CharField('运营商', max_length=6, choices=SIM_OPERATOR_CHOICES)
    sim_cost = models.IntegerField('制卡单价')
    IMSI = models.CharField('IMSI号', max_length=15)
    PIN1 = models.CharField('PIN1', max_length=15)
    PUK1 = models.CharField('PUK1', max_length=15)
    PIN2 = models.CharField('PIN2', max_length=15)
    PUK2 = models.CharField('PUK2', max_length=15)
    insert_dt = models.DateTimeField('导入时间', default=timezone.now)
    update_dt = models.DateTimeField('更新时间', auto_now=True)


class Distributors(models.Model):
    distributors_id = models.IntegerField('渠道商代码', primary_key=True)
    dis_level = models.SmallIntegerField('渠道商级别', default=1)
    dis_balance = models.IntegerField('账户金额')
    dis_legal_representative = models.CharField('法定代表', max_length=100)
    dis_picture_url = models.ImageField('照片地址', upload_to='upload/distributors/')
    insert_dt = models.DateTimeField('导入时间', default=timezone.now)
    update_dt = models.DateTimeField('更新时间', auto_now=True)

    def img_show(self):
        return mark_safe(u'<img width=50px src="{0}" />'.format(self.dis_picture_url.url))

    img_show.short_description = '法人照片'
