from django.db.models import Q
from rest_framework import serializers
from .models import CustomerModel


class CustomerSerializers(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomerModel
        fields = ['customer_id', 'customer_name', 'shop_no', 'mobile_no', 'email', 'created_by', 'deleted']