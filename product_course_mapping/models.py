from django.db import models
from core.models import BaseModel
from course.models import Course
from product.models import Product


class ProductCourseMapping(BaseModel):
    product_parent_fk = models.ForeignKey(Product, on_delete=models.CASCADE)

    course_child_fk = models.ForeignKey(Course, on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product_parent_fk', 'course_child_fk')

    def __str__(self):
        return f"{self.product_parent_fk} -> {self.course_child_fk}"