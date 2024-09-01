from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import TextInput, Select, DateInput, NumberInput

from ..models import User, UserInfo


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")  # 添加你的自訂字段


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo

        fields = ["nickname", "tel", "location", "birth"]
        # fields = "__all__"

        labels = {
            "nickname": "姓名",
            "tel": "手機",
            "location": "地區",
            "birth": "生日",
        }

        widgets = {
            "nickname": TextInput(attrs={"required": "required"}),
            "tel": TextInput(attrs={"pattern": r"\d{10,15}"}),
            "location": Select(),
            "birth": DateInput(),
        }