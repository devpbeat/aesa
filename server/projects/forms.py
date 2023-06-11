from .models import Project, ProjectPlains
from django import forms
from django.forms import ModelForm, inlineformset_factory
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Field
from crispy_forms.helper import FormHelper
from django.utils.translation import ugettext_lazy as _



class ProjectForm(ModelForm):
    name =  forms.CharField(
        label="Name",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    status = forms.ChoiceField(
        label="Status",
        required=True,
        choices=Project.STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    project_code = forms.CharField(
        label="Project Code",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class ProjectPlains(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectPlains, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                "Project Plains",
                Field("plain", css_class="for form-control"),
