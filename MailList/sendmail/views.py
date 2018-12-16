from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sendmail.models import Mails, RcptGroup
from sendmail.serializers import MailsSerializer, RcptGroupSerializer

import pika
import threading

from sendmail.functions import send_mail_fuc, mq_read_start, mq_write


credentials = pika.PlainCredentials('test', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='mail_balance', durable=True)  # 声明queue

mrs = threading.Thread(target=mq_read_start, args=[channel, ])
mrs.start()


@api_view(['GET'])
def mail_list(request, format=None):
    '''
        查看自己发件箱内的所有邮件
    '''
    if request.method == 'GET':
        mails = Mails.objects.filter(deleted=False)
        serializer = MailsSerializer(mails, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def mail_detail(request, pk, format=None):
    '''
        使用pk指定要查看某一封邮件
        查看其详情
    '''
    try:
        mail = Mails.objects.get(pk=pk, deleted=False)
    except Mails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MailsSerializer(mail)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        mail.deleted = True
        mail.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def send_mail(request):
    '''
        发送邮件
    '''
    if request.method == 'POST':
        serialzer = MailsSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            FROM = request.POST.get('mailfrom')
            TO = request.POST.get('mailto')
            
            SUBJECT = request.POST.get('subject')
            TEXT = request.POST.get('mailtext')

            mq_write(channel, FROM, [TO,], SUBJECT, TEXT)  # 写入RabbitMQ，并发送

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_group(request):
    if request.method == 'POST':
        serializer = RcptGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_groupmail(request):
    '''
        群发邮件
    '''
    if request.method == 'POST':
        serializer = MailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            FROM = request.POST.get('mailfrom')
            TO = request.POST.get('mailto')
            SUBJECT = request.POST.get('subject')
            TEXT = request.POST.get('mailtext')

            try:
                group_members = RcptGroup.objects.get(GroupName=TO)
            except RcptGroup.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = RcptGroupSerializer(group_members)
            members=serializer.data['GroupMembers']
            members_list=members.split(",")
            print(members_list)

            mq_write(channel, FROM, members_list, SUBJECT, TEXT)  # 写入RabbitMQ，并发送
            
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
