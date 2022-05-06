from django import forms
from django.forms.widgets import NumberInput
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Title',
            }
        )
    )

    audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'my-audience form-control',
                'placeholder': 'Audience',
            }
        )
    )

    release_date = forms.DateField(
        widget=forms.NumberInput(
            attrs={
                'class': 'my-release_date form-control',
                'type': 'date',
            }
        )
    )
    
    GENRE_A = 'comedy'
    GENRE_B = 'romance'
    GENRE_C = 'action'
    GENRE_D = 'horror'
    GENRE_E = 'drama'
    GENRE_F = 'sf'
    GENRE_G = 'fantasy'
    GENRE_CHOICES = [
        (GENRE_A, '코미디'),
        (GENRE_B, '로맨스'),
        (GENRE_C, '액션'),
        (GENRE_D, '공포'),
        (GENRE_E, '드라마'),
        (GENRE_F, 'SF'),
        (GENRE_G, '판타지/모험')
    ]
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'my-genre form-control',
            }    
        )
    )

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'my-score form-control',
                'placeholder': 'Score',
                'step':'0.5',
                'min':'0',
                'max':'5'
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'