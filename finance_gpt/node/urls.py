from django.urls import path
from . import views

urlpatterns = [
    path('api/messages/create/', views.create_message, name='create_message'),
    path('api/messages/get/<int:user_id>/', views.get_messages_by_user_id, name='get_messages_by_user_id'),


    path('api/get/csrf/', views.get_csrf_token, name='get_csrf_token'),

    path('api/chat/', views.chat, name='chat'),


    path('api/get_live_stock_price/<str:ticker>/', views.get_stock_price, name='get_stock_price'),
    path('api/get_stock_past_performance/<str:ticker>/<str:days>/', views.get_stock_past_performace, name='get_stock_past_performace'),
    path('api/get_company_information/<str:ticker>/', views.get_company_information, name='get_company_information'),
    path('api/get_major_holders/<str:ticker>/', views.get_major_holders, name='get_major_holders'),

    path('api/trading/sell_stocks/<str:ticker>/<int:quantity>/', views.sell_stocks, name='sell_stocks'),
    path('api/trading/purchase_stocks/<str:ticker>/<int:quantity>/', views.purchase_stocks, name='purchase_stocks'),


]
