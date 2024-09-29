from django import forms

class ColorFilterForm(forms.Form):
    TYPE_CHOICES = [
        ('', 'Any'), 
        ('casual', 'Casual'),
        ('professional', 'Professional'),
    ]

    color_name = forms.CharField(required=False, max_length=20, label='Main Color')
    outfit_type = forms.ChoiceField(required=False, choices=TYPE_CHOICES, label='Outfit Type')
    color_one = forms.CharField(required=False, max_length=20, label='Color One')
    color_two = forms.CharField(required=False, max_length=20, label='Color Two')