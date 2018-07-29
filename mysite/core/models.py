from django.db import models

# Create your models here.

class TicketSystem(models.Model):
    ClientTicketID = models.IntegerField(unique=True)
    xmlns_process = models.CharField(max_length=100)
    xmlns_header = models.CharField(max_length=100)
    xmlns_ticket = models.CharField(max_length=100)
    PartnerTicketID = models.CharField(max_length=20)
    Source = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Version = models.CharField(max_length=100)
    MessageDate = models.CharField(max_length=100)
    MessageID = models.CharField(max_length=100)
    ProcessType = models.CharField(max_length=100)
    ActionType = models.CharField(max_length=100)
    MessageType = models.CharField(max_length=100)
    IsTask = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    StatusText = models.CharField(max_length=100)
    Comment = models.CharField(max_length=100, null=True)