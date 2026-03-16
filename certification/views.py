from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Certification
from .serializers import CertificationSerializer


class CertificationListCreateAPIView(APIView):

    def get(self, request):

        certifications = Certification.objects.filter(is_active=True)

        serializer = CertificationSerializer(certifications, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CertificationDetailAPIView(APIView):

    def get_object(self, id):

        try:
            return Certification.objects.get(id=id, is_active=True)
        except Certification.DoesNotExist:
            return None


    def get(self, request, id):

        certification = self.get_object(id)

        if not certification:
            return Response({"error": "Certification not found"}, status=404)

        serializer = CertificationSerializer(certification)

        return Response(serializer.data)


    def put(self, request, id):

        certification = self.get_object(id)

        serializer = CertificationSerializer(certification, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        certification = self.get_object(id)

        serializer = CertificationSerializer(certification, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        certification = self.get_object(id)

        certification.is_active = False
        certification.save()

        return Response(status=204)