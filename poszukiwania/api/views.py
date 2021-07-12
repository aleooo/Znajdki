from ..models import Rzeczy, Category
from .serializers import FindsSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView



class FindList(APIView):
    def get(self, request):
        finds = Rzeczy.objects.all()
        serializer = FindsSerializer(finds, many=True)
        return Response(serializer.data)



class FindDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'znajdki_detail.html'

    def get(self, request, pk):
        find = Rzeczy.objects.get(pk=pk)
        serializer = FindsSerializer(find)
        return Response(serializer.data)

    def put(self, request, pk):

        find = Rzeczy.objects.get(pk=pk)
        serializer = FindsSerializer(find, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('rest-framework:finds_detail', pk=pk)

        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': 'list/',
        'Detail': 'list/<int:pk>/',
    }
    return Response(api_urls)
