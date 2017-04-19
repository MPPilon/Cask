from rest_framework import serializers
from models import User, Job


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'address', 'city', 'region', 'country', 'postal')


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'creatorUser', 'workerUser', 'category', 'compensation', 'description')


class FullJobSerializer(serializers.ModelSerializer):
    creatorUser = UserSerializer()
    workerUser = UserSerializer()

    class Meta:
        model = Job
        fields = ('id', 'creatorUser', 'workerUser', 'category', 'compensation', 'description')
