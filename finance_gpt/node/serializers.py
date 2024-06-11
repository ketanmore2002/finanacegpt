from rest_framework import serializers
from .models import *

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages
        fields = '__all__'




class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
