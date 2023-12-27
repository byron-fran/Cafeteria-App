from django.shortcuts import render, redirect
from .form import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    form_contact = ContactForm()
    if request.method == 'POST':
        form_contact = ContactForm(data=request.POST)
        if form_contact.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            # Enviamos el correo
            email_subject = "Mensaje de contacto"
            email_body = f"Nombre: {name}\nEmail: {email}\nMensaje: {message}"
            email = EmailMessage(email_subject, email_body, to=['your_email@example.com'], reply_to=[email])
            # Lo enviamos
            try:
                
                email.send()
            except:
                # Algo fallo
                return redirect(reverse('contact') +'?fail')   
            
            return redirect(reverse('contact') +'?ok')
            
    return render(request, ('contact.html'), {'form':  form_contact })



