from ..forms import *
from django.shortcuts import render

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import redirect

def contact(request):

    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')

            contact_email = request.POST.get('contact_email', '')

            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')

            subject = request.POST.get('reason', '')

            context = Context({ 'contact_name': contact_name,
                                'contact_email': contact_email,
                                'form_content': form_content,
                                })

            content = template.render(context)

            email = EmailMessage(
                    subject + ' - ' + contact_name,
                    content,
                    'hermstadalex@gmail.com',
                    ['hermstadalex@gmail.com'],
                    headers = {'Reply-To': contact_email }
                    )

            email.send()

            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
        })


