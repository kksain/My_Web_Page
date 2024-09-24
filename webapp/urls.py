from django.contrib import admin
from django.urls import path

from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit', views.submit_form, name='submit_form'),
    path('submissions/', views.view_submissions, name='view_submissions'),
]
