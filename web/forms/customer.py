from django.forms import ModelForm, Form
from web import models


class CustomerForm(ModelForm):
    class Meta:
        models = models.Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.item():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
