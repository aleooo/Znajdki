from ..models import Rzeczy
from .serializers import FindsSerializer, MapSerializer, CategorySerializer
from rest_framework import status
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def finds_list_view(request):
    finds = Rzeczy.objects.all()
    serializer = FindsSerializer(finds, many=True)
    return Response(serializer.data)


class FindsUpdateView(APIView):
    def get(self, request, pk, format=None):
        find = Rzeczy.objects.get(pk=pk)
        serializer = FindsSerializer(find)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     find = Rzeczy.objects.get(pk=pk)
    #     serializer = FindsSerializer(find, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        find = Rzeczy.objects.get(pk=pk)
        find.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

