from rest_framework.serializers import ModelSerializer

from calendartest.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'start_time', 'end_time', 'user',)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance