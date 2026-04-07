from django import forms
from django.db.models import Max, Min
from .models import People, Movies

class CharacterSearchForm(forms.Form):
    min_date = forms.DateField(label='Min date', widget=forms.SelectDateWidget())
    max_date = forms.DateField(label='Max date', widget=forms.SelectDateWidget())
    diameter = forms.IntegerField(required=True)
    gender = forms.ChoiceField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # min and max year 
        min_year = Movies.objects.aggregate(Min('release_date'))['release_date__min'].year
        max_year = Movies.objects.aggregate(Max('release_date'))['release_date__max'].year

        years = [str(x) for x in range(min_year - 1, max_year + 1)]

        self.fields['min_date'].widget.years = years
        self.fields['max_date'].widget.years = years

        # For gender
        genders = People.objects.values_list('gender', flat=True).distinct()
        self.fields['gender'].choices = [ (g, g) for g in genders if g ]
