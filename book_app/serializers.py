from rest_framework import serializers
from .models import *


#authprserializer:
class authorserializer(serializers.ModelSerializer):
    class Meta:
        model=authormodel
        fields='__all__'



#bookserializers:
class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=bookmodel
        fields='__all__'