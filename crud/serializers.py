from rest_framework import serializers
from .models import*

class drinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=drink
        fields = ['id','name','description']