from django import forms
from .models import *

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'

    def clean(self):
        cleaned_data = super(SportForm, self).clean()
        nomSport = cleaned_data.get('nomSport')
        """ case insensitive search """
        nbrSportWithSameName = Sport.objects.filter(nomSport__iexact=nomSport).count()
        """Permet de ne pas pouvoir insérer le sport FoOtBaLl si football existe déjà"""
        if nbrSportWithSameName > 0:
            raise forms.ValidationError(
                "Le nom du sport est sensible à la casse, un sport du même nom existe déjà."
            )
    
        return cleaned_data