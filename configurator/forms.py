from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from abc import ABC, abstractmethod


class CommonComponentsAbstract:
    def save(self, commit=True):
        # Создаем или обновляем CPU
        instance = super().save(commit=False)

        # Проверяем, есть ли связанный объект Product
        if hasattr(instance, 'product') and instance.product is not None:
            # Обновляем существующий объект Product
            instance.product.type = self.cleaned_data['type']
            instance.product.price = self.cleaned_data['price']
            instance.product.save()
        else:
            # Создаем новый объект Product
            instance.product = Product.objects.create(
                type=self.cleaned_data['type'],
                price=self.cleaned_data['price']
            )

        if commit:
            instance.save()

        return instance


class AddCPUForm(CommonComponentsAbstract, forms.ModelForm):
    type = forms.CharField(max_length=100, initial="cpu", widget=forms.HiddenInput())
    price = forms.DecimalField(label="Цена", max_digits=10, decimal_places=2)

    class Meta:
        model = CPU
        fields = '__all__'
        exclude = ['product']


class AddGPUForm(CommonComponentsAbstract, forms.ModelForm):
    type = forms.CharField(max_length=100, initial="gpu", widget=forms.HiddenInput())
    price = forms.DecimalField(label="Цена", max_digits=10, decimal_places=2)

    class Meta:
        model = GPU
        fields = '__all__'
        exclude = ['product']


class AddRAMForm(CommonComponentsAbstract, forms.ModelForm):
    type = forms.CharField(max_length=100, initial="ram", widget=forms.HiddenInput())
    price = forms.DecimalField(label="Цена", max_digits=10, decimal_places=2)

    class Meta:
        model = RAM
        fields = '__all__'
        exclude = ['product']


class AddCaseForm(CommonComponentsAbstract, forms.ModelForm):
    type = forms.CharField(max_length=100, initial="case", widget=forms.HiddenInput())
    price = forms.DecimalField(label="Цена", max_digits=10, decimal_places=2)

    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['product']


class AddPSUForm(CommonComponentsAbstract, forms.ModelForm):
    type = forms.CharField(max_length=100, initial="psu", widget=forms.HiddenInput())
    price = forms.DecimalField(label="Цена", max_digits=10, decimal_places=2)

    class Meta:
        model = PSU
        fields = '__all__'
        exclude = ['product']


class AddCPUCoolerForm(CommonComponentsAbstract, forms.ModelForm):
    type = forms.CharField(max_length=100, initial="cpucooler", widget=forms.HiddenInput())
    price = forms.DecimalField(label="Цена", max_digits=10, decimal_places=2)

    class Meta:
        model = CPUCooler
        fields = '__all__'
        exclude = ['product']
