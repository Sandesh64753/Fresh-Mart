from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('create/' , views.product_create_view , name='product_create'),
    path('list/' , views.product_list_view , name='product_list'),
    path('add/',views.add_product, name = 'add_product'),
    path('login/',views.login_view,name='login_view'),
    path('signup_view/',views.signup_view,name='signup_view'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('update/<int:product_id>/' , views.product_update_view , name='product_update'),
    path('delete/<int:product_id>/' , views.product_delete_view , name='product_delete'),
    path('place-order/<int:product_id>/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),
]