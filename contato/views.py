from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from .forms import ContatoForm
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from core import settings

def contato(request):



    return render(request, 'contato/contato.html',  {'form': ContatoForm()})


def processa_contato(request):

    if request.method == 'POST':
        contato = ContatoForm(request.POST)

        if contato.is_valid():            
            try:
                # enviar_email(contato)
                enviar_email_com_template(contato)

                obj = contato
                obj.save()

                messages.success(request, 'Mensagem encaminhada com sucesso')
                return render(request, 'contato/contato.html', {'form': ContatoForm()})
            
            except BadHeaderError:
                return HttpResponse('Invalid header found')
        else:
            return render(request, 'contato/contato.html', {'form': contato})
            

    return render(request, 'contato/contato.html', {'form': ContatoForm()})





def enviar_email(contato):
    send_mail(
        contato.cleaned_data['assunto'],
        contato.cleaned_data['mensagem'],
        settings.EMAIL_HOST_USER,
        [contato.cleaned_data['email']],
        fail_silently=False,
    )

def enviar_email_com_template(contato):
    html_content = render_to_string('email_templates/confirmacao_mensagem.html',
                                
        {'nome': contato.cleaned_data['nome'], 
         'assunto':contato.cleaned_data['assunto']}                        
        )

  
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(
        contato.cleaned_data['assunto'], 
        text_content, 
        settings.EMAIL_HOST_USER, 
        [contato.cleaned_data['email']]
    )
    
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return True