from django.db.models import Q
from rest_framework import serializers
from .models import OrderedItemsModel
from item.models import ItemModel
from order.serializers import OrderSerializers


class OrderedItemsSerializers(serializers.ModelSerializer): 

    def to_representation(self, instance):
        ret = super(OrderedItemsSerializers,self).to_representation(instance)

        if "order" in ret:
            ret["order_date"] = OrderSerializers(instance.order).data["order_date"]
            ret["customer"] = OrderSerializers(instance.order).data["customer"]
            ret["seller"] = OrderSerializers(instance.order).data["seller"]
            

        item_name_list = {}
        for item1 in ret["item"]:
            item_name = ItemModel.objects.get(pk=item1)
            item_name_list[item_name.item_id] = item_name.item_name
            ret['item'] = item_name_list

        # if len(item_name_list) == 0:
        #         raise serializers.ValidationError("item does not exist")
        
        return ret


    ordered_items_id = serializers.IntegerField(read_only=True)
    

    class Meta:
        model = OrderedItemsModel
        fields = ['ordered_items_id', 'item', 'total_amount', 'order', 'quantity', 'created_by', 'deleted']


