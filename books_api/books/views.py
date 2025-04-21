from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Book
from .serializers import BookSerializer



# from rest_framework.authtoken.models import Token
# def some_api(request):
#  token = Token.objects.create(user=request.user)
#  return Response({'token': token.key})


class SecretDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"Привет, {request.user.username}! Это секретные данные 👀"
        })

 
class BookAPIListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
