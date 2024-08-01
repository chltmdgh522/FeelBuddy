from django import forms
from .models import AdminCharacter, UserCharacter
from django.conf import settings

class AdminCharacterForm(forms.ModelForm):
    class Meta:
        model = AdminCharacter
        fields = ['emotion']

    def save(self, commit=True):
        instance = super(AdminCharacterForm, self).save(commit=False)
        media_path = settings.MEDIA_URL + 'characters/'
        if instance.emotion == 'angry':
            instance.image = media_path + 'angry.png'
        elif instance.emotion == 'anxiety':
            instance.image = media_path + 'anxiety.png'
        elif instance.emotion == 'fear':
            instance.image = media_path + 'fear.png'
        elif instance.emotion == 'joy':
            instance.image = media_path + 'joy.png'
        elif instance.emotion == 'sad':
            instance.image = media_path + 'sad.png'

        if commit:
            instance.save()
        return instance

class UserCharacterForm(forms.ModelForm):
    class Meta:
        model = UserCharacter
        fields = ['name', 'introduce', 'adminCharacter']
        widgets = {'adminCharacter': forms.HiddenInput()}  # 필드를 숨김으로 설정

    def __init__(self, *args, **kwargs):
        super(UserCharacterForm, self).__init__(*args, **kwargs)
        self.fields['adminCharacter'].queryset = AdminCharacter.objects.all()
        self.fields['adminCharacter'].required = False  # 필수 항목이 아님
