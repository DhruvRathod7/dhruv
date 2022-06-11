from django.db import models
from django.utils.timezone import now



class ItemModel(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100, default="")
    item_price = models.IntegerField(null=True)

    created_by = models.IntegerField(default=1, unique=False)
    deleted = models.IntegerField(default=0, unique=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"({self.item_id},{self.item_name})"

    class Meta:
        db_table = "item"
