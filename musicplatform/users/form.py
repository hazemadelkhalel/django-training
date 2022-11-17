from .models import UserProfile
from django import forms
class UserProfileForm( forms.ModelForm ):
    bio = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = UserProfile
        fields=['bio']