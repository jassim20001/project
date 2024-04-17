from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Blog_ser(serializers.ModelSerializer):
    
    class Meta:
        model=Blogs
        fields = '__all__'
class Expert_ser(serializers.ModelSerializer):

    class Meta:
        model=ExpertDoctor
        fields = '__all__'
