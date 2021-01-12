from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView
from .models import TestingDataBase
from .serializer import PostSerializer
from .permissions import permission
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PostListView(ListAPIView):
    queryset = TestingDataBase.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (permission,IsAuthenticated) 
 


class PostDetailsView( RetrieveUpdateAPIView):
    queryset = TestingDataBase.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (permission,IsAuthenticated) 
   