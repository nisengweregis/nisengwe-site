from django.urls import path
from . import views

urlpatterns = [
    path("", views.opportunities_index, name="opportunities_index"),
    path("<int:pk>/", views.opportunities_detail, name="opportunities_detail"),
    path("<category>/", views.opportunities_category, name="opportunities_category"),
]