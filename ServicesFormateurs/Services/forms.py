from django.forms import ModelForm, formset_factory

from Services.models import Request, ServiceType, RequestDays, RequestDate, Trainer
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

class TrainerForm(ModelForm):
    class Meta:
        model = Trainer

        fields = [
            'initials',
            'first_name',
            'last_name',
            'start_date'
        ]

        labels = {
            'initials': 'Initiales du formateur (nom et prénom)',
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
            'start_date': 'Date de la prise de poste',
        }

        widgets = {
            'initials': forms.TextInput(attrs={
                'style': 'text-transform: uppercase;',
                'maxlength': '5',
                'placeholder': 'Ex : BA pour BINET Anaïs'
            }),

            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ex : Anaïs'
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Ex : BINET'
            }),

            'start_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%d-%m-%Y'
            ),
        }
        
    def clean_initials(self):
        initials = self.cleaned_data['initials']
        return initials.upper()
