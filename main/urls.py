from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('take-test/<int:test_id>', TakeTestView.as_view(), name='take-test'),
]