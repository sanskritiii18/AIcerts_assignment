from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingListCreateAPIView(APIView):

    def get(self, request):

        mappings = VendorProductMapping.objects.filter(is_active=True)

        serializer = VendorProductMappingSerializer(mappings, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class VendorProductMappingDetailAPIView(APIView):

    def get_object(self, id):

        try:
            return VendorProductMapping.objects.get(id=id, is_active=True)

        except VendorProductMapping.DoesNotExist:
            return None


    def get(self, request, id):

        mapping = self.get_object(id)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = VendorProductMappingSerializer(mapping)

        return Response(serializer.data)


    def put(self, request, id):

        mapping = self.get_object(id)

        serializer = VendorProductMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        mapping = self.get_object(id)

        serializer = VendorProductMappingSerializer(mapping, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        mapping = self.get_object(id)

        mapping.is_active = False
        mapping.save()

        return Response(status=status.HTTP_204_NO_CONTENT)