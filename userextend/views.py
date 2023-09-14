import random
from datetime import datetime
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView
from userextend.forms import UserForm
from userextend.models import History


# Create your views here.
class UserCreationView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.username = (f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}'
                                 f'_{random.randint(100000, 999999)}')
            new_user.save()

            get_message = (f'Userul a fost adaugat cu success. Username: {new_user.username}, email:{new_user.email}, '
                           f'first_name: {new_user.first_name}, last_name: {new_user.last_name}')

            History.objects.create(message=get_message, created_at=datetime.now(), active=True)

            # subject = 'Adding a new account'
            # message = f'Congratulations! Your username is: {new_user.username}.'

            # send_mail(subject, message, 'george@popescu.ro', [new_user.email])
            # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            details_user = {
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': new_user.username
            }

            subject = 'Adding a new account'
            message = get_template('mail.html').render(details_user)

            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()

        return redirect('login')
