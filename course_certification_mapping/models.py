from django.db import models
from core.models import BaseModel
from course.models import Course
from certification.models import Certification


class CourseCertificationMapping(BaseModel):
    course_parent_fk = models.ForeignKey(Course, on_delete=models.CASCADE)

    certification_child_fk = models.ForeignKey(Certification, on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)

    class Meta:
        unique_together = ('course_parent_fk', 'certification_child_fk')

    def __str__(self):
        return f"{self.course_parent_fk} -> {self.certification_child_fk}"