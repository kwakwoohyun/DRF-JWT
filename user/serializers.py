from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=30)
    user_pw = serializers.CharField(max_length=100)
    user_name = serializers.CharField(max_length=20)
    gender = serializers.CharField(max_length=3)
    mail_addr = serializers.CharField(max_length=30)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField
