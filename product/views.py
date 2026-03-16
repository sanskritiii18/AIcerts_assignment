from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(APIView):

    def get(self, request):

        products = Product.objects.filter(is_active=True)

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ProductDetailAPIView(APIView):

    def get_object(self, id):

        try:
            return Product.objects.get(id=id, is_active=True)
        except Product.DoesNotExist:
            return None


    def get(self, request, id):

        product = self.get_object(id)

        if not product:
            return Response({"error": "Product not found"}, status=404)

        serializer = ProductSerializer(product)

        return Response(serializer.data)


    def put(self, request, id):

        product = self.get_object(id)

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        product = self.get_object(id)

        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        product = self.get_object(id)

        product.is_active = False
        product.save()

        return Response(status=204)