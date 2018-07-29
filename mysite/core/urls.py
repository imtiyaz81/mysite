from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    url(r'^katkaticketsytem/', TemplateView.as_view(template_name='core/index2.html')),
    url(r'^login/', TemplateView.as_view(template_name='core/login.html')),
    url(r'^submit_req/', views.submit_req, name='submit_req'),
    url(r'^api/ticket', views.tech_resp, name='tech_resp'),
    url(r'^ticketupdate/', views.business_resp, name='business_resp'),
    url(r'^commentticket/', views.comment_resp, name='comment_resp'),
]