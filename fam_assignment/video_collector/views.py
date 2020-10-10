from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .pagination import Pagination
from.serializers import VideoSerializer
from rest_framework.generics import GenericAPIView
# Create your views here.


class Videos(GenericAPIView):

    queryset = Video.objects.all().order_by('-published_at')
    pagination_class = Pagination
    serializer_class = VideoSerializer

    def get(self,request):

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

        return Response(data)


