from django.contrib import admin
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books'))
]