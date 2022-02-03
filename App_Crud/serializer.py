from rest_framework import serializers
from App_Crud.models import Status
class status_serializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['pk', 'user', 'content', 'image']
