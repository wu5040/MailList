from django.db import models

# Create your models here.


class Mails(models.Model):
    '''
        邮件数据结构设计
        created     ---接收时间
        subject     ---主题
        mailfrom    ---发件人
        mailto      ---收件人
        mailtext    ---邮件正文内容
        deleted     ---标记删除
    '''
    created = models.DateTimeField(auto_now_add=True)
    # server = models.CharField(max_length=20, default="localhost")
    subject = models.CharField(max_length=20, default="subject")
    mailfrom = models.CharField(max_length=30, default="")
    mailto = models.CharField(max_length=30, default="")
    mailtext = models.TextField()
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class RcptMembers(models.Model):
    '''
        收件人信息
    '''
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=4)
    mailAddress = models.CharField(max_length=30)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class RcptGroups(models.Model):
    '''
        收件人群组
    '''
    # owner
    created = models.DateTimeField(auto_now_add=True)
    GroupName = models.CharField(max_length=50, default="新建分组")
    # GroupMembers=models.TextField()
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class RcptGroups_Members(models.Model):
    '''
        群组——成员关系
    '''
    GroupName = models.CharField(max_length=50, default="")
    MembersAddress = models.CharField(max_length=30, default="")

    class Meta:
        ordering = ('id',)
