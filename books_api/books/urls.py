from django.urls import path 
from . import views


app_name = "books"

urlpatterns = [
    path("", views.BookAPIListView.as_view(), name='books'),
    path('secret/', views.SecretDataView.as_view(), name='secret_data'),
]
