"""Django の forms.py に該当するファイル"""
from django import forms


class SampleForm(forms.Form):
    keyword = forms.CharField()
