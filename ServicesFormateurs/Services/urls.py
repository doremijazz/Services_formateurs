from django.urls import path

from . import views

app_name = "Services"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('do_request', views.do_request, name='do_request'),
    path("trainers/", views.TrainerListView.as_view(), name="trainers"),
    path("trainers/add/", views.TrainerCreateView.as_view(), name="trainer_add"),
    path("trainers/<int:pk>/edit/", views.TrainerUpdateView.as_view(), name="trainer_edit"),
    path("inscription/", views.InscriptionView.as_view(), name="inscription"),
    path("connexion/", views.connexion, name="connexion"),
]
