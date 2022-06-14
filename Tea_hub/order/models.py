from django.db import models
from django.utils.timezone import now
from customer.models import CustomerModel
from seller.models import SellerModel



class OrderModel(models.Model):

    order_id = models.AutoField(primary_key=True)

    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE, null=True)
    
    order_date = models.DateField(default=now, null=True)
    
    created_by = models.IntegerField(default=1, unique=False)
    deleted = models.IntegerField(default=0, unique=False)
    created_at = models.DateField(default=now)


    class Meta:
        db_table = "order"