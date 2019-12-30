from django.urls import path
from .views import contact, successview

urlpatterns = [
    path("", contact, name='contact'),
    path('success/', successview, name='success'),

]

