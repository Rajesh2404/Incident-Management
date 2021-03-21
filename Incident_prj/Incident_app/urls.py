from django.urls import path
from .views import IncidentList, IncidentDetail, IncidentCreate, IncidentDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from Incident_app import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', IncidentList.as_view(), name='incidents'),
    path('incident/<int:pk>', IncidentDetail.as_view(), name='incident'),
    path('incident-create', IncidentCreate.as_view(), name='incident-create'),
    path('incident-delete/<int:pk>/', IncidentDelete.as_view(), name='incident-delete'),
]
