from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from calendartest.models import Event
from calendartest.serializers import EventSerializer


def event_page(request):
    return render(request, 'index.html', {'event': Event.objects.all()})


class EventAll(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventView(APIView):

    def get(self, request, *args, **kwargs):
        allEvents = Event.objects.all()
        ser = EventSerializer(allEvents, many=True)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        event = request.data.get('event')

        serializer = EventSerializer(data=event)
        if serializer.is_valid(raise_exception=True):
            event_saved = serializer.save()
        return Response({"success": "Event '{}' успешно создан".format(event_saved.name)})

    def put(self, request, pk):
        saved_event = get_object_or_404(Event.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = EventSerializer(instance=saved_event, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            event_saved = serializer.save()

        return Response({
            'Success': 'Event updated'
        })

    def delete(self, request, pk):
        event = get_object_or_404(Event.objects.all(), pk=pk)
        event.delete()
        return Response({
            'message':'Event has been deleted'
        }, status=204)