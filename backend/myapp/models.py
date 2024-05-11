from django.db import models


class InvitationCode(models.Model):
    code = models.CharField(verbose_name='邀请码', max_length=20, unique=True)
    expire = models.DateTimeField(verbose_name='过期时间')


    def __str__(self):
        return self.code