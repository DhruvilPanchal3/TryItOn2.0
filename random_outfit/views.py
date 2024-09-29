from django.shortcuts import render
from django.views import View
from .models import Outfit
from .forms import ColorFilterForm

class RandomView(View):
    template_name = 'random.html'

    def get(self, request):
        form = ColorFilterForm()
        outfits = Outfit.objects.all()
        return render(request, self.template_name, {'form': form, 'outfits': outfits})

    def post(self, request):
        form = ColorFilterForm(request.POST)
        outfits = Outfit.objects.all()
        if form.is_valid():
            color_name = form.cleaned_data.get('color_name')
            outfit_type = form.cleaned_data.get('outfit_type')
            color_one = form.cleaned_data.get('color_one')
            color_two = form.cleaned_data.get('color_two')

            if color_name:
                outfits = outfits.filter(main_color__iexact=color_name)
            if outfit_type:
                outfits = outfits.filter(outfit_type=outfit_type)
            if color_one:
                outfits = outfits.filter(color_one__iexact=color_one)
            if color_two:
                outfits = outfits.filter(color_two__iexact=color_two)

        return render(request, self.template_name, {'form': form, 'outfits': outfits})