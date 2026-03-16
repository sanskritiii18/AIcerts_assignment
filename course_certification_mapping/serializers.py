from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping
        fields = "__all__"

    def validate(self, data):

        course = data.get("course_parent_fk")
        primary = data.get("primary_mapping")

        if primary:
            if CourseCertificationMapping.objects.filter(
                    course=course,
                    primary_mapping=True
            ).exists():

                raise serializers.ValidationError(
                    "This course already has a primary certification mapping."
                )

        return data