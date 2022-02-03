from App_Crud.models import Status
from .serializer import status_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
class StatusListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = status_serializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetailDeleteUpdateApi(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):

    queryset = Status.objects.all()
    serializer_class = status_serializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



#class StatusListCreateView(generics.ListCreateAPIView):
 #   queryset = Status.objects.all()
    #serializer_class = status_serializer



#class StatusDetailDeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):

   # queryset = Status.objects.all()
    #serializer_class = status_serializer
    #lookup_field = 'id'
