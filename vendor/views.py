from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class VendorListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="List all vendors",
        responses={200: VendorSerializer(many=True)}
    )

    def get(self, request):

        vendors = Vendor.objects.filter(is_active=True)

        serializer = VendorSerializer(vendors, many=True)

        return Response(serializer.data)


    @swagger_auto_schema(
        operation_summary="Create a vendor",
        request_body=VendorSerializer,
        responses={201: VendorSerializer}
    )

    def post(self, request):

        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_summary="Retrieve a vendor",
        responses={200: VendorSerializer}
    )
    def get(self, request, id):

        vendor = self.get_object(id)

        if not vendor:
            return Response({"error": "Vendor not found"}, status=404)

        serializer = VendorSerializer(vendor)

        return Response(serializer.data)


    @swagger_auto_schema(
        operation_summary="Update vendor",
        request_body=VendorSerializer,
        responses={200: VendorSerializer}
    )
    def put(self, request, id):

        vendor = self.get_object(id)

        serializer = VendorSerializer(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    @swagger_auto_schema(
        operation_summary="Partially update vendor",
        request_body=VendorSerializer
    )
    def patch(self, request, id):

        vendor = self.get_object(id)

        serializer = VendorSerializer(vendor, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    @swagger_auto_schema(
        operation_summary="Delete vendor"
    )
    def delete(self, request, id):

        vendor = self.get_object(id)

        vendor.is_active = False
        vendor.save()

        return Response(status=204)