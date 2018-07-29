#-*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
   ClientTicketID = forms.IntegerField()
   Summary = forms.CharField(max_length=250)
   Description = forms.CharField(max_length=300)