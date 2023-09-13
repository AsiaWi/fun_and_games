from django.urls import path
from .views import IndexView, AddActivity


# path list
urlpatterns= [
    path('', IndexView.as_view(), name = 'index'),
    path('add/', AddActivity.as_view(), name = 'add_activity')
]