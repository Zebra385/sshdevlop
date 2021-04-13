from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from contact.forms import ContactForm
from django.views.generic import TemplateView, View
from django.core.mail import send_mail
from django.contrib.auth import logout, login

# Create your views here.




class SendView(View):
    """ That class to get the accueil page"""
    form_class = ContactForm
    template_name = 'contact/contact.html'

    def get(self, request, *args, **kwargs):
               
        form = self.form_class()
        context = {'form': form, }
        return render(request, self.template_name, context)
   
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            sender_address = []
            # auth_user=CustomUser.objects.get(pk=user.id)
            your_name = form.cleaned_data['your_name']
            sender = form.cleaned_data['sender']
            sender_address.append(sender)
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message_complet = "Mme/M. {} dont l\'adresse email est : {} qui m'envoi à sshdevlop le message suivant :\n{}".format(your_name, sender, message)   
            message_expeditor = "Mme/M. {} dont l\'adresse email est : {} a envoyer à sshdevlop le message suivant :\n{}".format(your_name, sender, message)                             
            send_mail(
                subject,
                message_complet,
                'houche.zebra385@gmail.com',
                ['houche.zebra385@gmail.com',],
                                )
            subject_copy = "Copie de {}".format(subject)
            send_mail(
                subject_copy,
                message_expeditor,
                'houche.zebra385@gmail.com',
                sender_address,
                                )
            return HttpResponseRedirect(reverse('contact:confirm_message_send'))
        else:
            # for test
            print('form non valid')
            print(form.errors)
            context = {'form': form}
            return render(request,  self.template_name, context)

class ConfirmMessageSend(TemplateView):
    """ That class THAT a message was sended"""
    template_name = "contact/confirm_message_send.html"

  