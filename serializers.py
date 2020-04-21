from rest_framework import serializers
from ..models import Subject
class SubjectSerializer(serializers.ModelSerializer): 
class Meta: 
model = Subject
fields = ['transferfrom', 'tranferto', 'requestdate', 'transferdate', 'subscriberid']
