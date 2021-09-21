from django.urls import path
from . import views
import my_app

app_name = 'my_app'

urlpatterns = [
    path('',views.index,name='home'),
    path('search',views.new_search,name='new_search'),
]