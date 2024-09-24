from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from .models import Submission
from .forms import UserForm


def home(request):
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Do what you can, with what you have, where you are.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "The harder you work for something, the greater you'll feel when you achieve it."
    ]
    random_quote = random.choice(quotes)
    current_datetime = datetime.now()
    form = UserForm()
    context = {
        'form': form,
        'quote': random_quote,
        'current_datetime': current_datetime
    }
    return render(request, 'home.html', context)


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
