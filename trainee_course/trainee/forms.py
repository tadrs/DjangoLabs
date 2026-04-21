from django import forms
from trainee.models import Trainee
from course.models import Course

class TraineeFormModel(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'