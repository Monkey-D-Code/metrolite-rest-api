from django.urls import path
from . import views

app_name = 'stats'
urlpatterns = [

    path('view-sales/' , views.ItemSaleList.as_view()),
    path('view/<int:year>/<int:month>/<int:day>/', views.ItemsDatewise.as_view()),
    path('add-sale/' , views.AddSale.as_view()),
    path('view-purchases/',views.ItemPurchaseList.as_view()),
    path('add-purchase/' ,views.AddPurchase.as_view()),
    path('sale-in-day/' , views.SaleInDay.as_view()),
    path('purchase-detail/', views.ItemPurchaseDetail.as_view()),
    path('purchase-in-hospital/' , views.PurchaseInHospital.as_view()),
    path('sale-one-day/' , views.SaleOneDay.as_view()),
    path('purchase-one-day/' , views.PurchaseOneDay.as_view()),
]
