from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView
from .models import TestingDataBase
from .serializer import PostSerializer

# Create your views here.
class PostListView(ListAPIView):
    queryset = TestingDataBase.objects.all()
    serializer_class = PostSerializer
 


class PostDetailsView( RetrieveAPIView):
    queryset = TestingDataBase.objects.all()
    serializer_class = PostSerializer
   