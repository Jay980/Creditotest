from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_view, name='predict_view'),
    path('new_home/', views.new_home, name='new_home'),
    path('predict_new_view/', views.predict_new_view, name='predict_new_view'),
    path('upload_data/', views.upload_data, name='upload_data'),

]