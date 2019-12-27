from django.urls import path
from . import views

urlpatterns = [
    path("", views.consulting_index, name='consulting_index'),
    path("<int:pk>/", views.consulting_detail, name='consulting_detail'),

]

