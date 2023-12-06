from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:pk>/', views.item_details, name='item_details'),
    path('buy/<int:pk>/', views.CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('index/', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks')
]
