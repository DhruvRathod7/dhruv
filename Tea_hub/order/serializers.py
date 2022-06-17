from rest_framework import serializers
from .models import OrderModel, OrderDetailModel
from item.models import ItemModel


class OrderSerializers(serializers.ModelSerializer):    
    def to_representation(self, instance):
        ret = super(OrderSerializers,self).to_representation(instance)

        if "seller" in ret:
            ret["seller_id"] = ret["seller"]
            del ret["seller"]

        if "customer" in ret:
            ret["customer_id"] = ret["customer"]
            del ret["customer"]


        order_detail = OrderDetailModel.objects.filter(order_id=instance.order_id)
        order_detail = OrderSerializers(order_detail, many=True)

        
        
        ret["item"] = order_detail.data
        return ret


    order_id = serializers.IntegerField(read_only=True)
    order_date = serializers.DateField(format="%d-%m-%Y", allow_null=True)

    class Meta:
        model = OrderModel
        fields = ['order_id', 'customer', 'seller', 'order_date', 'created_by', 'deleted']
        
class OrderDetailSerializers(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super(OrderDetailSerializers, self).to_representation(instance)

        if "rate" in ret:
            ret["item_price"] = ret["rate"]
            del ret["rate"]
        
        if "order_detail_id" in ret:
            ret["item_id"] = ret["order_detail_id"]
            del ret["order_detail_id"]

        if "item" in ret:
            item = ItemModel.objects.filter(pk=ret["item"]).first()
            if item:
                ret["item_name"] = item.item_name
        return ret

    def validate(self, data):
        data["total_amount"] = int(data["quantity"]) * int(data["rate"])
        

        return data

    order_detail_id = serializers.IntegerField(read_only=True)
    total_amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrderDetailModel
        fields = ['order_detail_id', 'order', 'item', 'rate', 'total_amount', 'quantity', 'created_by', 'deleted', 'created_at']


