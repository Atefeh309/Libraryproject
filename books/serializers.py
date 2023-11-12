from rest_framework import serializers
from .models import UserProfile, book, reserve
from rest_framework import validators
from rest_framework.validators import ValidationError

class userserializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'family', 'age')
        model = UserProfile

    def validate_name(self,name):
        if len(name)<3:
            raise serializers.ValidationError('please Enter a true namE')
        return name


class bookserializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'writer', 'subject')
        model = book


class reserveserializers(serializers.ModelSerializer):
    book_name = bookserializers(read_only=True)
    transferee = userserializers(read_only=True)

    class Meta:
        fields = ('id', 'book_name', 'transferee')
        model = reserve
