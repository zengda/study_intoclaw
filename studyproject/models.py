from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        (0, "未知"),
        (1, "男"),
        (2, "女"),
    ]

    STATE_CHOICES = [
        (0, "拉黑"),
        (1, "游客"),
        (2, "用户"),
    ]

    IS_DISTRIBUTOR_CHOICES = [
        (1, "普通用户"),
        (2, "审核中分销商"),
        (3, "审核通过分销商"),
        (4, "审核拒绝分销商"),
    ]

    id = models.AutoField(primary_key=True)
    nickName = models.CharField("用户名", max_length=150, blank=True)
    avatarUrl = models.CharField("头像", max_length=500, blank=True)
    trueName = models.CharField("真实姓名", max_length=150, blank=True)
    birthday = models.DateField("生日", null=True, blank=True)
    gender = models.IntegerField("性别", choices=GENDER_CHOICES, default=0)
    wxapp_openid = models.CharField("微信小程序openid", max_length=100, blank=True, db_index=True)
    wxh5_openid = models.CharField("微信公众号openid", max_length=100, blank=True, db_index=True)
    bdapp_openid = models.CharField("百度小程序openid", max_length=100, blank=True, db_index=True)
    is_h5 = models.BooleanField("H5用户", default=False)
    is_app = models.BooleanField("APP用户", default=False)
    is_pc = models.BooleanField("PC用户", default=False)
    phone = models.CharField("手机号", max_length=20, unique=True, blank=True, db_index=True)
    regtime = models.DateTimeField("注册时间", auto_now_add=True)
    last_time = models.DateTimeField("最后活跃时间", null=True, blank=True)
    state = models.IntegerField("用户状态", choices=STATE_CHOICES, default=2)
    note = models.TextField("备注", blank=True)
    pid = models.IntegerField("上级id", default=0)
    is_distributor = models.IntegerField("分销商状态", choices=IS_DISTRIBUTOR_CHOICES, default=1)
    uniacid = models.IntegerField("平台id", default=0)
    unionid = models.CharField("开放平台唯一标识", max_length=100, blank=True, db_index=True)
    is_user = models.IntegerField("是否有用户信息", default=0)
    lid = models.IntegerField("标签id", default=0)
    token = models.CharField("token", max_length=255, blank=True)
    bind_time = models.DateTimeField("与分销商绑定时间", null=True, blank=True)
    wxstore_openid = models.CharField("微信小店openid", max_length=100, blank=True, db_index=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "nickName"]

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = "用户"
