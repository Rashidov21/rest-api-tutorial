from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'main'



# Подключите наш API, используя автоматическую маршрутизацию URL.
# Кроме того, мы включаем URL-адреса для входа в доступный для просмотра API.
urlpatterns = [
    path('get-list/', views.TaskViewSet.as_view(), name='tasks'),
]