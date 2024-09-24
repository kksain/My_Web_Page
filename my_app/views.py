from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from .models import Submission
from .forms import UserForm



def home(request):
    form = UserForm()
    return render(request, 'home.html', {'form': form})


def submit_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            submission = Submission(name=name, email=email)
            submission.save()
            return HttpResponse(f"Thank you {name}! Your email {email} has been successfully submitted.")
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'home.html', {'form': form})



def view_submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})
