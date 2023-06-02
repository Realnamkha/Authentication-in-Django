from .models import Post,Profile
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
