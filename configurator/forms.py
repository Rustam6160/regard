from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError



class AddCPUForm(forms.ModelForm):
    class Meta:
        model = CPU
        fields = '__all__'
class AddGPUForm(forms.ModelForm):
    class Meta:
        model = GPU
        fields = '__all__'
class AddRAMForm(forms.ModelForm):
    class Meta:
        model = RAM
        fields = '__all__'
class AddCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
class AddPSUForm(forms.ModelForm):
    class Meta:
        model = PSU
        fields = '__all__'
# class AddCPUCoolerForm(forms.ModelForm):
#     class Meta:
#         model = CPUCooler
#         fields = '__all__'     #не работает изза модели скорее всего
