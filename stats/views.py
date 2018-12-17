from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from .models import Item_sale,Item_purchase
from .serializers import Item_saleSerializer,Item_purchaseSerializer

from datetime import datetime
import json

# FOR AUTHENTICATION AND PERMISSION
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ItemSaleList(APIView):
    # authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        

        all_item_sales = Item_sale.objects.all()
        serializer = Item_saleSerializer(all_item_sales , many=True)
        return HttpResponse(JSONRenderer().render(serializer.data))


class ItemPurchaseList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):

        all_item_purchases = Item_purchase.objects.all()
        serializer = Item_purchaseSerializer(all_item_purchases , many=True)
        return HttpResponse(JSONRenderer().render(serializer.data))

    

class ItemsDatewise(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request , year, month , day):

        date = str(year)+"-"+str(month)+"-"+str(day)
        today_item_sales = Item_sale.objects.filter(date=date)
        serializer = Item_saleSerializer(today_item_sales , many=True)
        return HttpResponse(JSONRenderer().render(serializer.data))

class AddSale(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        return HttpResponse("Not ! Allowed")

    def post(self,request):
        info = request.data
        
        if info.keys() == {'item_name','item_id','item_price','quantity_bought' , 'hospital'}:

            I = Item_sale(item_id=info['item_id'] , item_name=info['item_name'] , item_price=info['item_price'], quantity_bought=info['quantity_bought'] , hospital=info['hospital'])
            I.save()
            return Response(info , status=status.HTTP_201_CREATED)
        else:
            return Response({"details" : "Please Verify the input format"} , status=status.HTTP_400_BAD_REQUEST)


class AddPurchase(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        return HttpResponse("Not ! Allowed")

    def post(self,request):
        info = request.data
        
        if info.keys() == {'name','item_id','price','purchase_quantity' ,'kitchen_issue' ,'stock' ,'hospital' , 'credit'}:

            I = Item_purchase(item_id=info['item_id'] , name=info['name'] , price=info['price'], purchase_quantity=info['purchase_quantity'], hospital=info['hospital'], kitchen_issue=info['kitchen_issue'], stock=info['stock'] , credit=info['credit'])
            I.save()
            return Response(info , status=status.HTTP_201_CREATED)
        else:
            return Response({"details" : "Please Verify the input format"} , status=status.HTTP_400_BAD_REQUEST)

class SaleInDay(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        return Response({"details" :"Not ! Allowed"} , status=status.HTTP_404_NOT_FOUND)
    
    def post(self,request):
        info = request.data
        DT = datetime.now()
        date = str(DT.year)+"-"+str(DT.month)+"-"+str(DT.day)
        if info.keys() == {'hospital'}:
            sales = Item_sale.objects.filter(hospital=info['hospital'],date=date)
            # print(sales)
            total_sale = 0;
            for sale in sales:
                total_sale += (sale.quantity_bought*sale.item_price)
            # print(total_sale)
            
            return Response({'total_sale' : total_sale} , status=status.HTTP_200_OK)

        else:
            return Response({"details" : "Hospital Name Only !"} , status=status.HTTP_400_BAD_REQUEST)
        
