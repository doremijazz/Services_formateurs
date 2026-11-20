from django.shortcuts import render, redirect
from django.views import View

from Services.forms import RequestForm, RequestDateForm, RequestDateFormSet
from Services.models import Request


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
