from django.forms import ModelForm
from .models import ContactForm


class FeedbackForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
