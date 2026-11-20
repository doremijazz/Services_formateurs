from django.forms import ModelForm, formset_factory

from Services.models import Request, ServiceType, RequestDays, RequestDate
from django import forms

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            'type', 'days', 'trainer', 'type_service'
        ]
        labels = {
            'type': 'Type de demande',
            'days': 'Jour de la semaine',
            'trainer': 'Formateur',
            'type_service': 'Type de service',
        }

        widgets = {
            'type': forms.Select(choices=ServiceType.choices),
            'days': forms.Select(choices=RequestDays.choices),
            'trainer': forms.Select(),
            'type_service': forms.Select(choices=ServiceType.choices)
        }
        help_texts = {
            'type' : 'Est ce un indisponibilité ou un souhait ?',
            'days' : 'Selectionner un jour de la semaine ou remplissez les créneaux ci desous',
            'trainer' : 'Choisisez les intiales (nom et prénom) du formateur qui fait la demande',
        }

class RequestDateForm(ModelForm):
    class Meta:
        model = RequestDate
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

RequestDateFormSet = formset_factory(
    RequestDateForm,
    extra=6
)

