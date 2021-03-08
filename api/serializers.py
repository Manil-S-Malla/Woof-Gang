from rest_framework import serializers
from .models import Gang


class GangSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gang
        fields = ('id', 'code', 'host', 'can_guests_pause', 'votes_to_skip', 'created_at')


