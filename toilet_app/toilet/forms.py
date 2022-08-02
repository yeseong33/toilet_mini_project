from django import forms
from . import models

class SearchForm(forms.Form):

    max_distance = forms.IntegerField(required=True)
    toilet_gender = forms.CharField(max_length=5, required=False)
    isDisabledToilet = forms.BooleanField(required=False)
    isChildToilet = forms.BooleanField(required=False)

class CreateToiletForm(forms.ModelForm):
    class Meta:
        model = models.Toilet
        fields = (
            "name",
            "address",
            "gender",
            "isBisexual",
            "toiletNum",
            "urinalNum",
            "disabledToiletNum",
            "disabledUrinalNum",
            "childToiletNum",
            "childUrinalNum",
            "managementAgency",
            "phoneNumber",
            "openTime",
            "installationDate",
            "latitude",
            "longitude"
        )
    
    def save(self, *args, **kwargs):
        toilet = super().save(commit=False)
        return toilet