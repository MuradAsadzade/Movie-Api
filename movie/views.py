from django.shortcuts import render,get_object_or_404
from .models import Studio,Genre,Movie
from rest_framework.response import Response
from rest_framework import status,generics,parsers,permissions
from rest_framework.decorators import api_view,parser_classes
from .serializers import StudioSerializer,GenreSerializer,MovieSerializer
from user.permissions import IsAdminOrReadOnly
from .permissions import DirectorPermission
from .paginator import GenrePaginator
from user.throttling import User5ForMinute,Anon5ForMinute
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
# @api_view(['GET','POST'])
# def studio_list(request):
#     studios=Studio.objects.all()
#     if request.method=='GET':
#         serializer=StudioSerializer(studios,many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=StudioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
        
# @api_view(['GET','PUT','DELETE'])
# def studio_detail(request,pk):
#     studio=get_object_or_404(Studio,pk=pk)
#     if request.method=='GET':
#         serializer=StudioSerializer(studio)
#         return Response(serializer.data)
#     elif request.method=='PUT':
#         serializer=StudioSerializer(instance=studio,data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#     elif request.method=='DELETE':
#         studio.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
class StudioListAV(generics.ListCreateAPIView):
    queryset=Studio.objects.all()
    serializer_class=StudioSerializer
    permission_classes=[DirectorPermission]

class StudioDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Studio.objects.all()
    serializer_class=StudioSerializer
    permission_classes=[DirectorPermission]
    
    

class GenreListAV(generics.ListCreateAPIView):
    def get_queryset(self):
        return Genre.objects.all()
    def get_serializer_class(self):
        return GenreSerializer
    pagination_class = GenrePaginator
    

class GenreDetailAV(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Genre.objects.all()
    def get_serializer_class(self):
        return GenreSerializer
    throttle_classes=[User5ForMinute,Anon5ForMinute]
    
    
class MovieListAV(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    ordering_fields  = "__all__"
    search_fields = ['username', 'email']


class MovieDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    
class UpdateMovieImageAV(generics.UpdateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    parser_classes=[parsers.MultiPartParser,parsers.FormParser]