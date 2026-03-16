from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):

        mappings = CourseCertificationMapping.objects.filter(is_active=True)

        serializer = CourseCertificationMappingSerializer(mappings, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, id):

        try:
            return CourseCertificationMapping.objects.get(id=id, is_active=True)
        except CourseCertificationMapping.DoesNotExist:
            return None


    def get(self, request, id):

        mapping = self.get_object(id)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = CourseCertificationMappingSerializer(mapping)

        return Response(serializer.data)


    def put(self, request, id):

        mapping = self.get_object(id)

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        mapping = self.get_object(id)

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        mapping = self.get_object(id)

        mapping.is_active = False
        mapping.save()

        return Response(status=204)