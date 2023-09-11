from django.urls import path
from .views import IndexView


# path list
urlpatterns= [
    path('', IndexView.as_view(), name= 'index')
]