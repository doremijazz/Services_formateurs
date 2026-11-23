from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View

from Services.forms import RequestForm, RequestDateForm, RequestDateFormSet, TrainerForm, InscriptionForm
from Services.models import Request, Trainer


class IndexView(View):
    model = Request
    template_name = "services/index.html"
    context_object_name = "demandes"

def do_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        date_form = RequestDateFormSet(request.POST)

        if form.is_valid() and date_form.is_valid():
            requested_data = form.save(commit=False)
            if request.user.is_authenticated:
                requested_data.trainer = request.user
            requested_data.save()

            print("Demande crée : ", requested_data.pk)

            for date in date_form:
                if date.cleaned_data and not date.cleaned_data.get("DELETE", False):
                    data = date.save(commit=False)
                    data.request = requested_data.pk
                    data.save()
        return redirect("Services:index")
    else:
        form = RequestForm()
        date_form = RequestDateFormSet()
    return render(request, "Services/request_form.html", {"form": form, "date_form": date_form})

def is_direction(user):
    return user.is_authenticated and user.is_staff

# Afficher tous les formateurs
#@method_decorator(user_passes_test(is_direction), name="dispatch")
class TrainerListView(ListView):
    model = Trainer
    template_name = "Services/trainers.html"
    context_object_name = "trainers"

    def get_queryset(self):
        return Trainer.objects.all().order_by("last_name", "first_name")


# Ajouter un formateur (direction uniquement)
#@method_decorator(user_passes_test(is_direction), name="dispatch")
class TrainerCreateView(View):
    template_name = "Services/trainer_form.html"

    def get(self, request, *args, **kwargs):
        form = TrainerForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = TrainerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("Services:trainers")

        return render(request, self.template_name, {"form": form})

#@method_decorator(
    #user_passes_test(
        lambda user: user.is_authenticated and user.is_staff,
        login_url="/Services/connexion/"
    #),
    #name="dispatch"
#)
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = "Services/trainer_form.html"
    context_object_name = "trainer"
    success_url = reverse_lazy("Services:trainers")

class InscriptionView(View):
    template_name = "Services/inscription.html"

    def get(self, request, *args, **kwargs):
        form = InscriptionForm()

        return render(
            request,
            self.template_name,
            {"form": form}
        )

    def post(self, request, *args, **kwargs):
        form = InscriptionForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("Services:connexion")

        return render(
            request,
            self.template_name,
            {"form": form}
        )

def connexion(request):
    """Affiche le formulaire de connexion et authentifie un utilisateur.

    En cas de succès, ouvre la session et redirige vers l’accueil.
    """
    erreur = None
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Services:index")
        erreur = "Identifiants incorrects."
    return render(request, "Services/connexion.html", {"erreur": erreur})


def deconnexion(request):
    """Ferme la session de l’utilisateur courant.

    Redirige ensuite vers la page d’accueil.
    """
    logout(request)
    return redirect("services:index")