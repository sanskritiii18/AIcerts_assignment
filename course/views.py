from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer


class CourseListCreateAPIView(APIView):

    def get(self, request):

        courses = Course.objects.filter(is_active=True)

        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):

    def get_object(self, id):

        try:
            return Course.objects.get(id=id, is_active=True)
        except Course.DoesNotExist:
            return None


    def get(self, request, id):

        course = self.get_object(id)

        if not course:
            return Response({"error": "Course not found"}, status=404)

        serializer = CourseSerializer(course)

        return Response(serializer.data)


    def put(self, request, id):

        course = self.get_object(id)

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        course = self.get_object(id)

        serializer = CourseSerializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        course = self.get_object(id)

        course.is_active = False
        course.save()

        return Response(status=status.HTTP_204_NO_CONTENT)