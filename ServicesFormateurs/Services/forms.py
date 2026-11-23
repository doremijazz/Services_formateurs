from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm, formset_factory
from django.contrib.auth.models import User
import os
import secrets

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
            'start_date',
            "work_quota"
        ]

        labels = {
            'initials': 'Initiales du formateur (prénom et nom)',
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
            'start_date': 'Date de la prise de poste',
            "work_quota": "Quotité de travail (%)",
        }

        widgets = {
            'initials': forms.TextInput(attrs={
                'style': 'text-transform: uppercase;',
                'maxlength': '5',
                'placeholder': 'Ex: AB pour Anaïs BINET'
            }),

            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ex: Anaïs'
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Ex: BINET'
            }),

            'start_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%d-%m-%Y'
            ),
            'work_quota': forms.Select(
                choices=[
                    (100, '100 %'),
                    (90, '90 %'),
                    (80, '80 %'),
                    (75, '75 %'),
                    (60, '60 %'),
                    (50, '50 %'),
                ]
            ),
        }

    def clean_initials(self):
        initials = self.cleaned_data['initials']
        return initials.upper()

class InscriptionForm(UserCreationForm):
    """Formulaire de création d'un compte utilisateur."""

    direction_password = forms.CharField(
        label="Mot de passe direction (facultatif)",
        required=False,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Réservé à la direction",
            "autocomplete": "off"
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name"
        ]

    def clean_direction_password(self):
        password = self.cleaned_data.get("direction_password")

        if password:
            expected = os.environ.get("DIRECTION_PASSWORD")

            if not expected or not secrets.compare_digest(
                password, expected
            ):
                raise forms.ValidationError(
                    "Mot de passe direction incorrect."
                )

        return password

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)

        # Vérifier le mot de passe direction
        user.is_staff = bool(
            self.cleaned_data.get("direction_password")
        )

        if not commit:
            return user

        # Rechercher un formateur existant
        trainers = Trainer.objects.filter(
            first_name__iexact=user.first_name.strip(),
            last_name__iexact=user.last_name.strip()
        )

        # Un seul formateur correspondant, sans compte associé
        if trainers.count() == 1:
            trainer = trainers.first()

            if trainer.user_id is None:
                user.save()

                trainer.user = user
                trainer.save(update_fields=["user"])

                return user

        # Sinon, créer uniquement le compte utilisateur
        user.save()
        return user
