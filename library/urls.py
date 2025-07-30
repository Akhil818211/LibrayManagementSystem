from django.urls import path
from . import views

urlpatterns = [
    path('', views.borrower_list, name='borrower_list'),
    path('add/', views.add_borrower, name='add_borrower'),
    path('update/<int:borrower_id>/', views.update_borrowed_date, name='update_borrowed_date'),
]
