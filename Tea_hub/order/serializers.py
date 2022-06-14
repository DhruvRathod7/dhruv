from django.db.models import Q
from rest_framework import serializers
from .models import OrderModel
from seller.serializers import SellerSerializers
from customer.serializers import CustomerSerializers
from item.serializers import ItemSerializers
from item.models import ItemModel


class OrderSerializers(serializers.ModelSerializer):    
    def to_representation(self, instance):
        ret = super(OrderSerializers,self).to_representation(instance)

        if "seller" in ret:
            ret["seller_name"] = SellerSerializers(instance.seller).data["seller_name"]

        if "customer" in ret:
            ret["customer_name"] = CustomerSerializers(instance.customer).data["customer_name"]
        
        

        return ret


    order_id = serializers.IntegerField(read_only=True)
    order_date = serializers.DateField(format="%d-%m-%Y", allow_null=True)

    class Meta:
        model = OrderModel
        fields = "__all__"