from ..models import Rzeczy, Category
from .serializers import FindsSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView



@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': 'finds/',
        'Detail': 'finds/<int:pk>/',
        'UPDATE': 'update/<int:pk>/',
        'DELETE': 'delete/<int:pk>/',
    }
    return Response(api_urls)



# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class FindsViewSet(viewsets.ModelViewSet):
#     queryset = Rzeczy.objects.all()
#     serializer_class = FindsSerializer

    # def update(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(request.user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
        # find = Rzeczy.objects.get(pk=kwargs['pk'])
        # cateogry = request.data.pop('category')
        # serializer = FindsSerializer(find, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FindsList(generics.ListAPIView):
    queryset = Rzeczy.objects.all()
    serializer_class = FindsSerializer

class FindsDetail(generics.RetrieveAPIView):
    queryset = Rzeczy.objects.all()
    serializer_class = FindsSerializer


#
# @api_view(['GET'])
# def finds_list_view(request):
#
#     finds = Rzeczy.objects.all()
#     serializer = FindsSerializer(finds, many=True)
#     return Response(serializer.data)


# class FindsUpdateView(APIView):
#     def get(self, request, pk, format=None):
#         find = Rzeczy.objects.get(pk=pk)
#         serializer = FindsSerializer(find)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         find = Rzeczy.objects.get(pk=pk)
#         data = JSONParser().parse(request)
#         serializer = FindsSerializer(find, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         find = Rzeczy.objects.get(pk=pk)
#         find.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(["GET", 'PUT', 'DELETE'])
# def finds_update_view(request, pk):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     try:
#         find = Rzeczy.objects.get(pk=pk)
#     except Rzeczy.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = FindsSerializer(find)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = FindsSerializer(Rzeczy, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         find.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
