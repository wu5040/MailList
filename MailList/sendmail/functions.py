import smtplib
import threading
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


# 写入RabbitMQ
def mq_write(channel, FROM, TO, SUBJECT, TEXT):
    info_dict = {"FROM": FROM, "TO": TO, "SUBJECT": SUBJECT, "TEXT": TEXT}
    info_json = json.dumps(info_dict)
    channel.basic_publish(exchange='',
                          routing_key='mail_balance',
                          body=info_json)

sem = threading.Semaphore(100)

def send_async_email(FROM, TO, SUBJECT, TEXT):
    SERVER = 'localhost'
    msg = MIMEMultipart('alternative')

    # 包含了非ASCII字符，需要使用unicode
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = ', '.join(TO)
    part1 = MIMEText("hello",'plain','utf-8')
    part2 = MIMEText(TEXT, 'html', 'utf-8')
    msg.attach(part1)
    msg.attach(part2)
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()


def send_mail_fuc(FROM, TO, SUBJECT, TEXT):
    with sem:
        s = threading.Thread(target=send_async_email, args=[
                             FROM, TO, SUBJECT, TEXT])
        s.start()


def read_callback(ch, method, properties, body):
    info_dict = json.loads(body)
    FROM, TO, SUBJECT, TEXT = info_dict['FROM'], info_dict['TO'], info_dict['SUBJECT'], info_dict['TEXT']
    print(FROM, TO, SUBJECT, TEXT)
    send_mail_fuc(FROM, TO, SUBJECT, TEXT)


def mq_read_start(channel):
    channel.basic_consume(read_callback,
                          queue='mail_balance',
                          no_ack=True)
    channel.start_consuming()
