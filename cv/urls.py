from .views import AccueilCvView
from django.urls import path, include

app_name = "cv"

urlpatterns = [
    path('parcourt/', AccueilCvView.as_view(), name="parcourt"),
   
]
