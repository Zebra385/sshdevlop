from .views import AccueilView
from django.urls import path, include
from .views import AccueilView, WorkView, Work01View, Work02View, Work03View

app_name = "workshop"

urlpatterns = [
    path('accueil/', AccueilView.as_view(), name="accueil"),
    path('work/', WorkView.as_view(), name="work"),
    path('work01/', Work01View.as_view(), name="work01"),
    path('work02/', Work02View.as_view(), name="work02"),
    path('work03/', Work03View.as_view(), name="work03"),
]
