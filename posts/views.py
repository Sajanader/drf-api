from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView
from .models import TestingDataBase
from .serializer import PostSerializer
from .permissions import permission

# Create your views here.
class PostListView(ListAPIView):
    queryset = TestingDataBase.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (permission,) 
 


class PostDetailsView( RetrieveUpdateAPIView):
    queryset = TestingDataBase.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (permission,) 
   