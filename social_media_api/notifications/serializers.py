from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_str = serializers.StringRelatedField(source='target', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_str', 'timestamp', 'is_read']
