
from django.shortcuts import render, redirect

# Create your views here.

from .forms import ContactForm
from django.http import HttpResponse


def contact(request):
    template = 'contact.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    context = {
            'form': form,
        }
    return render(request, template, context)


def successview(request):
    return HttpResponse('Success! Thank you for your message.')