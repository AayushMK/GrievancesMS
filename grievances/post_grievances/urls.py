from django.urls import path
from . import views

urlpatterns = [
    path('post_g/', views.post_g, name='post_g'),
    path('submit/', views.submit, name='submit'),

]
