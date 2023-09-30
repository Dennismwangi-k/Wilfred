from django.shortcuts import render
from rest_framework.views import APIView
from order.models import Order
from user.serializers import WasteCollectorSerializer, WasteRecyclerSerializer
from user.tests import WasteCollectorModelTest
from product.models import Product
from .serializer import OrderSerializer, ProductSerializer
from Category.models import Category
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from delivery.models import Delivery
from rest_framework.response import Response
from rest_framework import status
from .serializer import DeliverySerializer
from message.models import Message
from .serializer import MessageSerializer
from .serializer import LocationSerializer
from location.models import Location
from .serializer import OrderItemSerializer
from orderItem.models import OrderItem
from user.models import WasteCollector
from user.models import WasteRecycler
from user.views import UserViewSet
from rest_framework import permissions




class ProductListView(APIView):
    def get(self, request):
        product= Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ProductDetailView(APIView):
    def get(self,request, id, format=None):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(
                {"error": f"Product with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        product=Product.objects.get(id=id)
        product.delete()
        return Response("product with id {id} succefully deleted",status=status.HTTP_204_NO_CONTENT)




class DeliveryListView(APIView):
    def get(self, request):
        delivery = Delivery.objects.all()
        serializer = DeliverySerializer(delivery, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            delivery = Delivery.objects.get(id=id)
        except Delivery.DoesNotExist:
            return Response(
                {"error": f"Delivery with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        serializer = DeliverySerializer(delivery, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        return Response(f"Delivery with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)

    # 
class MessageListView(APIView):
    def get(self, request):
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            message = Message.objects.get(id=id)
        except Message.DoesNotExist:
            return Response(
                {"error": f"Message with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DeliverySerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        message = Message.objects.get(id=id)
        serializer = MessageSerializer(message, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id, format=None):
        message = Message.objects.get(id=id)
        message.delete()
        return Response(f"Message with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)
    
class LocationListView(APIView):
    def get(self, request):
        message = Location.objects.all()
        serializer = LocationSerializer(message, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =LocationSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            location= Location.objects.get(id=id)
        except Location.DoesNotExist:
            return Response(
                {"error": f"Location with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        location = Location.objects.get(id=id)
        serializer = LocationSerializer(location, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id, format=None):
        location = Location.objects.get(id=id)
        location.delete()
        return Response(f"Location with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)
    
# 
class OrderItemListView(APIView):
    def get(self, request):
        order= OrderItem.objects.all()
        serializer = OrderItemSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




class OrderItemDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            order =OrderItem.objects.get(id=id)
        except OrderItem.DoesNotExist:
            return Response(
                {"error": f"Order with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = OrderItemSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
       order = OrderItem.objects.get(id=id)
       serializer = OrderItemSerializer(order, request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id, format=None):
        order = OrderItem.objects.get(id=id)
        order.delete()
        return Response(f"Order with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)
    
class OrderListView(APIView):
    def get(self, request):
        order= Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            order =Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(
                {"error": f"Order with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
       order = Order.objects.get(id=id)
       serializer = OrderSerializer(order, request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id, format=None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response(f"Order with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)
    

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CategoryDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response(
                {"error": f"Category with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id, format=None):
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):

        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        return Response(f"Delivery with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)
    
class WasteRecycler(APIView):
    def post(self, request):
        serializer = WasteRecyclerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'wasterecycler registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class WasteCollectorLoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        first_name = request.data.get('first_name')
        try:
            waste = WasteCollector.objects.get(phone_number=phone_number, first_name=first_name)
        except WasteCollectorSerializer.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer =WasteCollectorSerializer(WasteCollectorModelTest)
        return Response({'message': 'Waste_Collector login successful'}, status=status.HTTP_201_CREATED)
        
class WasteRecyclerRegistrationView(APIView):
    def post(self, request):
        serializer =   WasteRecyclerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Supplier registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class WasteRecylerLoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        first_name = request.data.get('first_name')
        try:
            WasteRecycler = WasteRecycler.objects.get(phone_number=phone_number, first_name=first_name)
        except Waste_Recycler.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = WasteCollectorSerializer(wasteRecycler)
        return Response({'message': 'waste_recycler Login successful'}, status=status.HTTP_201_CREATED)




def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return Response(f"Category with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response(f"Category with id {id} not found", status=status.HTTP_404_NOT_FOUND)

# category = Category.objects.get(id=id)
# category.delete()
# return Response(f"Category with id {id} successfully deleted", status=status.HTTP_204_NO_CONTENT)











