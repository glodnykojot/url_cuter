from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path('', views.cuterView.as_view()),
    path('<slug:shortcut>', views.redirectView.as_view()),
] 
