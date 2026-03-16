from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = "__all__"

    def validate(self, data):

        vendor = data.get("vendor_parent_fk")
        primary = data.get("primary_mapping")

        if primary:

            query = VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            )

            if self.instance:
                query = query.exclude(id=self.instance.id)

            if query.exists():
                raise serializers.ValidationError(
                    "This vendor already has a primary product mapping."
                )

        return data

