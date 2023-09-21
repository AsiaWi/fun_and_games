from django.urls import path
from .views import DisplayActivityList, AddActivity, DisplayActivityDetails, DisplayProfileWall, DeleteActivity, UpdateActivity

# path list
urlpatterns = [
    path('', DisplayActivityList.as_view(), name = 'index'),
    path('profile/', DisplayProfileWall.as_view(), name = 'profile_wall'),
    path('add/', AddActivity.as_view(), name = 'add_activity'),
    path('<int:pk>/', DisplayActivityDetails.as_view(), name = 'view_activity_details'),
    path('delete/<int:activity_id>/', DeleteActivity.as_view(), name = 'activity_confirm_delete'),
    path('edit/<int:activity_id>/', UpdateActivity.as_view(), name = 'edit_activity'),
]