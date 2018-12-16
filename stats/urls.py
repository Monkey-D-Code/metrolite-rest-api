from django.urls import path
from . import views

app_name = 'stats'
urlpatterns = [

    path('view-sales/' , views.ItemSaleList.as_view()),
    path('view/<int:year>/<int:month>/<int:day>/', views.ItemsDatewise.as_view()),
    path('add-sale/' , views.AddSale.as_view()),
    path('view-purchases/',views.ItemPurchaseList.as_view()),
    path('add-purchase/' ,views.AddPurchase.as_view()),
]
