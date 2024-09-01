from . import views
from django.urls import path

urlpatterns = [    
    path('req', views.viewfirst),
    path('ren', views.viewsecond)
]


