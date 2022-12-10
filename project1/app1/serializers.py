from rest_framework import serializers
from .models import Data
from django.contrib.auth.models import User


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Data
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'


class SignUpSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only = True)

    password = serializers.CharField(
        write_only=True, max_length=12, min_length=6)   # this is very important

    class Meta:
        model = User
        # below fields are already provided to model class that why we are giving it here
        # we have to provide this fields only
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'email')
        read_only = ('id',)
        # write_only_fields = ('password',) ---> password also visible beacuse of this --> this is not required -->
        # if we want to do any field write_only --> for that --> password = serializers.CharField(write_only = True)

        # problem --> when we registed user last time -->
        # there login was not happening -- why --> the serializer create method override --> create_user call it.. here we will get validated data..

        # Now applying validations

        def validate_username(self, username):
            if len(username) < 6 or len(username) > 15:
                raise serializers.ValidationError(
                    'Username must be between 6 and 15 characters long')
            return username

        def validate_first_name(self, first_name):
            if first_name.istitle() != True:
                raise serializers.ValidationError(
                    'first name should be Capital')
            return first_name

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
