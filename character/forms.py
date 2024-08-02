from django import forms
from .models import AdminCharacter, UserCharacter
from django.conf import settings


class UserCharacterForm(forms.ModelForm):
    class Meta:
        model = UserCharacter
        fields = ['name', 'introduce', 'adminCharacter']
        widgets = {'adminCharacter': forms.HiddenInput()}  # 필드를 숨김으로 설정

    def __init__(self, *args, **kwargs):
        super(UserCharacterForm, self).__init__(*args, **kwargs)
        self.fields['adminCharacter'].queryset = AdminCharacter.objects.all()
        self.fields['adminCharacter'].required = False  # 필수 항목이 아님


class UserCharacterNameForm(forms.ModelForm):
    class Meta:
        model = UserCharacter
        fields = ['name']  # 이름만 수정 가능
