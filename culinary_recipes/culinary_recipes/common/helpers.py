
from django.contrib import messages
from django.http import BadHeaderError, HttpResponse
from django.core.mail import send_mail


def send_contact_email(request, form):
    body = {
        'first_name': form.cleaned_data['first_name'],
        'last_name': form.cleaned_data['last_name'],
        'subject': form.cleaned_data['subject'],
        'email': form.cleaned_data['email_address'],
        'message': form.cleaned_data['message'],
    }
    messages.add_message(request, messages.INFO, 'Благодарим ви, че се свързахте с нас!')
    message = f"Message form {body['first_name']} {body['last_name']}\n" \
              f"From {body['email']}\n" \
              f"Message: \n" \
              f"{body['message']}"

    try:
        send_mail(body['subject'], message, 'no.reply.our.recipes@gmail.com',
                  ['no.reply.our.recipes@gmail.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
