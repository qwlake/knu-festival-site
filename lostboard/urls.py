from django.urls import path
from . import views
# 분실물 urls.py
app_name = 'foodtruck'
urlpatterns = [
    path('', views.lostboard, name="lostboard"),
]
