from django.urls import path
from .views import DisplayActivityList, AddActivity, DisplayActivityDetails, DisplayProfileWall


# path list
urlpatterns= [
    path('', DisplayActivityList.as_view(), name = 'index'),
    path('profile/', DisplayProfileWall.as_view(), name = 'profile_wall'),
    path('add/', AddActivity.as_view(), name = 'add_activity'),
    path('<slug:pk>/', DisplayActivityDetails.as_view(), name = 'view_activity_details'),
]