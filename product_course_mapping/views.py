from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


class ProductCourseMappingListCreateAPIView(APIView):

    def get(self, request):

        mappings = ProductCourseMapping.objects.filter(is_active=True)

        serializer = ProductCourseMappingSerializer(mappings, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ProductCourseMappingDetailAPIView(APIView):

    def get_object(self, id):

        try:
            return ProductCourseMapping.objects.get(id=id, is_active=True)
        except ProductCourseMapping.DoesNotExist:
            return None


    def get(self, request, id):

        mapping = self.get_object(id)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = ProductCourseMappingSerializer(mapping)

        return Response(serializer.data)


    def put(self, request, id):

        mapping = self.get_object(id)

        serializer = ProductCourseMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        mapping = self.get_object(id)

        serializer = ProductCourseMappingSerializer(mapping, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        mapping = self.get_object(id)

        mapping.is_active = False
        mapping.save()

        return Response(status=204)