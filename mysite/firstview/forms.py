from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    userID = forms.userID(required=True)

    class Meta:
        model = User
        fields = ("userID", "userpassword", "userPasswordConfirm")

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False)
        user.userID = self.cleaned_data["userID"]
        if commit:
            user.save()
        return user
