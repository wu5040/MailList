from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sendmail import views

urlpatterns=[
    path('mails/',views.mail_list),
    path('mails/<int:pk>/',views.mail_detail),
    path('send_mail/',views.send_mail),
    path('create_group/',views.create_group),
    path('send_groupmail/',views.send_groupmail)
]

urlpatterns=format_suffix_patterns(urlpatterns)

