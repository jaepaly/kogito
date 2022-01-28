from django import forms
from .models import Application


class RegisterForm(forms.Form):
    email = forms.EmailField(label='이메일', error_messages={'invalid': '유효한 이메일 주소를 입력해주세요.'})
    password = forms.CharField(label='비밀번호', min_length=6, max_length=20, widget=forms.PasswordInput) #비밀번호 가려지는거
    password_confirm = forms.CharField(label='비밀번호 확인', min_length=6, max_length=20, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError({    #예외 발생
                    "password_confirm": ["2개의 비밀번호가 일치하지 않습니다."]
                })

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(label='이메일', error_messages={'invalid': '유효한 이메일 주소를 입력해주세요.'})
    password = forms.CharField(label='비밀번호', min_length=6, max_length=20, widget=forms.PasswordInput)

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['introduction', 'profile_image', 'nickname', 'job']
        labels = {
            'introduction': '자기소개',
            'profile_image': '프로필 사진',
            'nickname': '닉네임',
            'job': '역할'
        }