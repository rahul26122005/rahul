#forms.py

from django import forms
from .models import Student
from .models import Myclass
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())


class UploadFileForm(forms.Form):
    file = forms.FileField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'student_class', 'section']


class MyclassForm(forms.ModelForm):
        class Meta:
            model = Myclass
            fields = ['student', 'status']

class MonthYearForm(forms.Form):
    month = forms.IntegerField(min_value=1, max_value=12, label='Month')
    year = forms.IntegerField(min_value=2000, max_value=2100, label='Year')
   
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']




"""
views.py
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page or any other page
    else:
        form = StudentForm()
    return JsonResponse(request, 'add_student.html', {'form': form})

forms.py
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'enrolled_class']
models.py
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, null=True)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
this are my codes change into following conditions
1) I want to add the students roll number and the enrolled class in the list or select the in the any other page or in excel
2) and also I want to add the year like 1st year, 2rd year, 3rd year , 4th year like wise  they want to select for each of the students this also select form the list 

"""

