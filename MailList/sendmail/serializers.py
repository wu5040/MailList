from rest_framework import serializers
from sendmail.models import Mails,RcptGroup

class MailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mails
        fields=('id','subject','mailfrom','mailto','mailtext')

class RcptGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=RcptGroup
        fields=('id','GroupName','GroupMembers')