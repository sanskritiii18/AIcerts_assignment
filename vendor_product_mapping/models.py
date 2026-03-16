from django.db import models
from core.models import BaseModel
from vendor.models import Vendor
from product.models import Product


class VendorProductMapping(BaseModel):
    vendor_parent_fk = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    product_child_fk = models.ForeignKey(Product, on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)

    class Meta:
        unique_together = ('vendor_parent_fk', 'product_child_fk')

    def __str__(self):
        return f"{self.vendor_parent_fk} -> {self.product_child_fk}"