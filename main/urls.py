from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('take-test/<int:test_id>', TakeTestView.as_view(), name='take-test'),
    path('test-stats/<int:test_id>', TestStatsView.as_view(), name='test-stats'),
]