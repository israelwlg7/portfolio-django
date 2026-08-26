from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Projeto, Certificado, MensagemContato

def index(views_request):
    if views_request.method == 'POST':
        nome = views_request.POST.get('nome', '').strip()
        email = views_request.POST.get('email', '').strip()
        assunto = views_request.POST.get('assunto', '').strip()
        mensagem = views_request.POST.get('mensagem', '').strip()

        if nome and email and mensagem:
            MensagemContato.objects.create(
                nome=nome,
                email=email,
                assunto=assunto or "Contato via Portfólio Web",
                mensagem=mensagem
            )
            messages.success(views_request, "Sua mensagem foi enviada com sucesso! Em breve entrarei em contato.")
            return redirect('index')
        else:
            messages.error(views_request, "Por favor, preencha todos os campos obrigatórios.")

    projetos = Projeto.objects.all()
    certificados = Certificado.objects.all()

    # Stat counters
    total_projetos = projetos.count()
    total_certificados = certificados.count()
    horas_estudo = 156 + 20 + 20 + 20 + 12 + 18 + 8 + 2

    context = {
        'projetos': projetos,
        'certificados': certificados,
        'total_projetos': total_projetos,
        'total_certificados': total_certificados,
        'horas_estudo': horas_estudo,
    }
    return render(views_request, 'index.html', context)
