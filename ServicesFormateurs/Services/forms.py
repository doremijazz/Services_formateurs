from django.forms import ModelForm, formset_factory

from Services.models import Request, ServiceType, RequestDays, RequestDate
from django import forms

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            'type', 'days', 'trainer', 'type_service'
        ]
        widgets = {
            'type': forms.Select(choices=ServiceType.choices),
            'days': forms.Select(choices=RequestDays.choices),
            'trainer': forms.Select(),
            'type_service': forms.Select(choices=ServiceType.choices)
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

