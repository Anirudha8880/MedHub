from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home_view),
    path('add-medicine/',add_medicine_view),
    path('show-medicine/',show_medicine_view),
    path('update-medicine/<i>/',update_medicine_view),
    path('delete-medicine/<i>/',delete_medicine_view),
    path('search/',search_medicine_view),

]