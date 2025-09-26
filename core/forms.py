from django import forms
from .models import Case, Hearing, Document

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'status']


class HearingForm(forms.ModelForm):
    class Meta:
        model = Hearing
        fields = ['case', 'hearing_date', 'judge', 'lawyer', 'status']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['case', 'file']
