from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='index.html'

class Loginsuccess(TemplateView):
    template_name="loginsuccess.html"

class Thanks(TemplateView):
    template_name="thanks.html"
