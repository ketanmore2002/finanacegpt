from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

class NoteBook(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,editable=True,blank=True,null=True)
    date_field = models.DateField(auto_now_add=True,editable=True,blank=True,null=True)
    time_field = models.TimeField(auto_now_add=True,editable=True,blank=True,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='NoteBook', editable=True, blank=True, null=True)
    # def __str__(self):
    #     return str(self.user_id)+" NoteBook"

CHOICES = [
        ('SYSTEM', 'SYSTEM'),
        ('USER', 'USER'),
    ]
class messages(models.Model):
    note_book = models.ForeignKey(NoteBook, on_delete=models.CASCADE, related_name='messages',editable=True,blank=True,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', editable=True, blank=True, null=True)
    message = models.TextField(blank=True,null=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=True,blank=True,null=True)
    date_field = models.DateField(auto_now_add=True,editable=True,blank=True,null=True)
    time_field = models.TimeField(auto_now_add=True,editable=True,blank=True,null=True)
    type = models.CharField(max_length=20, choices=CHOICES,editable=True,blank=True,null=True)

    # def __str__(self):
    #     return str(self.user_id)+" messages"


CHOICES = [
        ('SELL', 'SELL'),
        ('BUY', 'BUY'),
    ]
class Transactions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Transactions', editable=True, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=True,blank=True,null=True)
    date_field = models.DateField(auto_now_add=True,editable=True,blank=True,null=True)
    time_field = models.TimeField(auto_now_add=True,editable=True,blank=True,null=True)
    type = models.CharField(max_length=20, choices=CHOICES)
    ticker = models.CharField(max_length=50,editable=True,blank=True,null=True)
    quantity = models.IntegerField(editable=True,blank=True,null=True) 
    price = models.DecimalField(decimal_places=5,max_digits=10,editable=True,blank=True,null=True)

    def __str__(self):
        return str(self.user_id)+" Transactions"


class stocks(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stocks', editable=True, blank=True, null=True)
    user_id = models.CharField(max_length=50,editable=True,blank=True,null=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=True,blank=True,null=True)
    date_field = models.DateField(auto_now_add=True,editable=True,blank=True,null=True)
    time_field = models.TimeField(auto_now_add=True,editable=True,blank=True,null=True)
    ticker = models.CharField(max_length=50,editable=True,blank=True,null=True)
    quantity = models.IntegerField(editable=True,blank=True,null=True)
    valuation = models.DecimalField(decimal_places=5,max_digits=10,editable=True,blank=True,null=True)

    def __str__(self):
        return str(self.user_id)+" stocks"

