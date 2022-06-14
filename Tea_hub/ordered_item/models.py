from django.db import models
from django.utils.timezone import now
from item.models import ItemModel
from order.models import OrderModel





class OrderedItemsModel(models.Model):

    ordered_items_id = models.AutoField(primary_key=True)
    item = models.ManyToManyField(ItemModel,blank=True)  
    total_amount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, null=True)


    created_by = models.IntegerField(default=1, unique=False)
    deleted = models.IntegerField(default=0, unique=False)
    created_at = models.DateField(default=now)

    def __str__(self):
        return f"({self.ordered_items_id})"

    class Meta:
        db_table = "ordered_items"

class OrderedIemsItemModel(models.Model):
    ordereditemsmodel = models.ForeignKey(OrderedItemsModel, on_delete=models.DO_NOTHING)
    itemmodel = models.ForeignKey(ItemModel, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "ordereditems_item"
        managed = False