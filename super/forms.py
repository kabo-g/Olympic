from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.db import transaction
from .models import User,LocalResident,Organiser
from . import models

class LocalResidentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name", "last_name", "email","username", "password1", "password2"]    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_localresident = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        localresident = LocalResident.objects.create(user=user)
        localresident.phone_number=self.cleaned_data.get('phone_number')
        localresident.location=self.cleaned_data.get('location')
        localresident.save()
        return user

class LocalResidentProfileForm(ModelForm):
    class Meta:
        model = LocalResident
        fields = "__all__"
        exclude = ["user"]


class OrganiserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name", "last_name", "email","username", "password1", "password2"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organiser = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        organiser = Organiser.objects.create(user=user)
        organiser.phone_number=self.cleaned_data.get('phone_number')
        organiser.designation=self.cleaned_data.get('designation')
        organiser.save()
        return user

# the olympics
class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"

class LecturerForm(forms.ModelForm):
    class Meta:
        model = models.Lecturer
        fields = "__all__"

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = "__all__"

class SportForm(forms.ModelForm):
    class Meta:
        model = models.Sport
        fields = "__all__"

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = models.Schedule
        fields = "__all__"

class VenueForm(forms.ModelForm):
    class Meta:
        model = models.Venue
        fields = "__all__"

class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = "__all__"