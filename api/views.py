from rest_framework import generics, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

from news.models import News
from news.serializers import NewsSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class NewsViewSet(viewsets.GenericViewSet, generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return NewsSerializer

    def get_queryset(self):
        return News.objects.all()
