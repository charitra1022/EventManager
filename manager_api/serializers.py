from rest_framework import serializers

from .models import SampleModel

class SampleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SampleModel
        fields = ('title', 'description')
        
