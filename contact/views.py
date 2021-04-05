from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from contact.forms import ContactForm
from django.views.generic import TemplateView, View
from django.core.mail import send_mail
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from ssh_project.settings import EMAIL_HOST_PASSWORD
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
            
            # auth_user=CustomUser.objects.get(pk=user.id)
            your_name = form.cleaned_data['your_name']
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message_complet = "Mme/Monsieur {} dont l\'adresse email est : {} qui m'envoi à sshdevlop le message suivant :\n{}".format(your_name, sender, message)
            user = authenticate(username='zebra385', password=EMAIL_HOST_PASSWORD)
            send_mail(
                subject,
                message_complet,
                'houche.zebra385@gmail.com',
                ['houche.zebra385@gmail.com',],
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

  