from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sendmail.models import Mails
from sendmail.serializers import MailsSerializer

@api_view(['GET'])
def mail_list(request,format=None):
    '''
        查看自己信箱内的所有邮件
    '''
    if request.method=='GET':
        mails=Mails.objects.all()
        serializer=MailsSerializer(mails,many=True)
        return Response(serializer.data)


@api_view(['GET','DELETE'])
def mail_detail(request,pk,format=None):
    '''
        使用pk指定要获取某一封邮件
        查看其详情
    '''
    try:
        mail=Mails.objects.get(pk=pk)
    except Mails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=MailsSerializer(mail)
        return Response(serializer.data)
    elif request.method=='DELETE':
        mail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
