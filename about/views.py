from django.shortcuts import render
from .forms import EmailForm
from django.shortcuts import render
from django.core.mail import send_mail


def landing(request):

    name = "Post"

    form = EmailForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        print(request.POST)

        print(form.cleaned_data)

        new_form = form.save()

    return render(request, 'about.html', locals())
