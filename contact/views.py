from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

# Create your views here.

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name =(form.cleaned_data['name'])
            email =(form.cleaned_data['email'])
            content =(form.cleaned_data['content'])

            html = render_to_string('contact/emails/contactforms.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('Sujet', 'Ceci est un message', 'noreply@test.com', ['megane.grego@gmail.com'], html_message=html)
            return redirect('contact')
    else: 
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {
        'form': form
    })