from rest_framework import serializers
from sendmail.models import Mails

class MailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mails
        fields=('id','subject','mailfrom','mailto','mailtext')