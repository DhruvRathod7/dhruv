from django.db.models import Q
from rest_framework import serializers
from item.models import ItemModel


class ItemSerializers(serializers.ModelSerializer):
    item_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ItemModel
        fields = ['item_id', 'item_name', 'item_price', 'created_by', 'deleted']