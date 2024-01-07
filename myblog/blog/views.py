from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import NotFound

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            # This tries to get the post, if not found, will raise Post.DoesNotExist
            return super().retrieve(request, *args, **kwargs)
        except Post.DoesNotExist:
            raise NotFound('A post with this ID does not exist.')  # Custom 404 message


#USER REGISTRATION VIEW
@api_view(['POST'])
def register_user(request):
    try:
        user = User.objects.create(
            username=request.data['username'],
            password=make_password(request.data['password']),
            email=request.data['email']
        )
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    except KeyError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)