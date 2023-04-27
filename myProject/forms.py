from django import forms
from .models import Diploma

class DiplomaForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ('tipologia', 'nome', 'cognome', 'dataNascita', 'luogoNascita', 'dataConseguimento', 'votazione', 'codiceId', 'hash', 'txId')