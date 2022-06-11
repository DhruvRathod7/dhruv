from django.db import models
from django.utils.timezone import now
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _



class SellerModel(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=100, default="")
    mobile_no = models.IntegerField(null=True)
    email = models.EmailField(_('email address'), unique=True)

    created_by = models.IntegerField(default=1, unique=False)
    deleted = models.IntegerField(default=0, unique=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"({self.seller_id},{self.seller_name})"

    class Meta:
        db_table = "seller"