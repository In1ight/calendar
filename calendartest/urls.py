from django.urls import path
from .views import EventView
app_name = "event"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('events/', EventView.as_view()),
    path('events/<int:pk>', EventView.as_view())
]