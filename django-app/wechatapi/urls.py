from django.conf.urls import url
from . import views



urlpatterns=[
    url(r'send/',views.send_msg,name='send_msg'),
    url(r'apis/',views.apis,name='apis'),
]