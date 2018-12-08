from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sendmail import views

urlpatterns=[
    path('mails/',views.mail_list),
    path('mails/<int:pk>/',views.mail_detail),
]

urlpatterns=format_suffix_patterns(urlpatterns)

