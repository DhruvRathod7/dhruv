from django.db.models import Q
from rest_framework import serializers
from .models import SellerModel


class SellerSerializers(serializers.ModelSerializer):
    seller_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SellerModel
        fields = ['seller_id', 'seller_name', 'mobile_no', 'email', 'created_by', 'deleted']