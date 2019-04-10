#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from rbac import models


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name','email', 'password' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }