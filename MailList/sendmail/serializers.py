from rest_framework import serializers
from sendmail.models import Mails,RcptMembers,RcptGroups,RcptGroups_Members

class MailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mails
        fields=('id','subject','mailfrom','mailto','mailtext')

class RcptGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model=RcptGroups
        fields=('id','GroupName')

class RcptMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model=RcptMembers
        fields=('id','name','gender','mailAddress')

class RcptGroups_MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model=RcptGroups_Members
        fields=('GroupName','MembersAddress')