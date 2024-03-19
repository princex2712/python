from rest_framework import serializers
from .models import BooksAPIModel

class bookAPIModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAPIModel
        fields = "__all__"