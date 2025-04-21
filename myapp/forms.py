from django import forms
from django.urls import reverse
from ajax_select.fields import AutoCompleteField


class TagForm(forms.Form):
    category = forms.CharField(
        label="Category",
        required=False,
        widget=forms.TextInput(attrs={
            "id": "id_category",
            "placeholder": "Enter category"
        })
    )
    user_id = forms.IntegerField(
        label="User ID",
        required=False,
        widget=forms.NumberInput(attrs={
            "id": "id_user_id",
            "placeholder": "Enter user ID"
        })
    )
    tags = AutoCompleteField('tags', required=False)
