from django.urls import path
from .views import DisplayActivityList, AddActivity


# path list
urlpatterns= [
    path('', DisplayActivityList.as_view(), name = 'index'),
    path('add/', AddActivity.as_view(), name = 'add_activity')
]