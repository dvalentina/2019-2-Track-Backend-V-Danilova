from rest_framework import serializers

class СhatSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)