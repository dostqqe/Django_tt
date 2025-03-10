from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SessionLocal, Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product_list(request):
    session = SessionLocal()
    if request.method == 'GET':
        products = session.query(Product).all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.create(serializer.validated_data)
            session.add(product)
            session.commit()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    session = SessionLocal()
    product = session.query(Product).filter(Product.id == pk).first()

    if request.method == 'GET':
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            product = serializer.update(product, serializer.validated_data)
            session.commit()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if product is not None:
            session.delete(product)
            session.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
