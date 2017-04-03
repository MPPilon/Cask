from rest_framework import serializers
from models import User, Job


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'address', 'city', 'region', 'country')


class JobSerializer(serializers.ModelSerializer):
    creatorUser = UserSerializer()
    workerUser = UserSerializer()

    class Meta:
        model = Job
        field = ('jobID', 'creatorUser', 'workerUser', 'category', 'compensation', 'description', 'photo')