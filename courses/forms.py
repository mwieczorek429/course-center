from django import forms
from django.forms import fields
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput
from .models import Course, Module
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

ModuleFormSet = inlineformset_factory(Course, Module, fields=['title', 'description'], extra=1, can_delete=True)
