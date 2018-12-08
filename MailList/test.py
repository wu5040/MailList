#请不要运行该文件，没用的
from sendmail.models import Mails
from sendmail.serializers import MailsSerializer

mail=Mails(  mailfrom='test@test.com',
                mailto='zyh_shdx@163.com',
                mailtext='this is a text.')
mail.save()