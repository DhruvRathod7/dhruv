from django.db import models
from re import T
from django.utils.timezone import now
from customer.models import CustomerModel
from seller.models import SellerModel
from item.models import ItemModel


class OrderModel(models.Model):

    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE, null=True)
    

    order_date = models.DateField(default=now, null=True)
    
    created_by = models.IntegerField(default=1, unique=False)
    deleted = models.IntegerField(default=0, unique=False)
    created_at = models.DateField(default=now)

    def __str__(self):
        return f"({self.order_id})"


    class Meta:
        db_table = "order"
        


class OrderDetailModel(models.Model):

    order_detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    
    item = models.ForeignKey(ItemModel, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)

    created_by = models.IntegerField(default=1, unique=False)
    deleted = models.IntegerField(default=0, unique=False)
    created_at = models.DateField(default=now)

    def __str__(self):
        return f"({self.order_detail_id})"
    class Meta:
        db_table = "order_detail"
    

