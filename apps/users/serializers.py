from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        telegram_id = validated_data.get('telegram_id', None)
        if telegram_id:
            validated_data.update({'telegram_id': str(telegram_id)})
        user = CustomUser.objects.create(**validated_data)
        return user

    def to_representation(self, instance):
        data = super(CustomUserSerializer, self).to_representation(instance)
        if data['telegram_id']:
            data.update({'telegram_id': int(data['telegram_id'])})
        return data
