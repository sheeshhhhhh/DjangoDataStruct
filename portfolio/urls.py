from django.urls import path
from .views import portfolio_views

urlpatterns = [
    path('', portfolio_views, name='portfolio')
]