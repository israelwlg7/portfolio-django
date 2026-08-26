from django.contrib import admin
from .models import Projeto, Certificado, MensagemContato

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destaque', 'ordem', 'criado_em')
    list_filter = ('categoria', 'destaque')
    search_fields = ('titulo', 'descricao', 'tecnologias')
    list_editable = ('destaque', 'ordem')

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'carga_horaria', 'categoria', 'destaque', 'ordem')
    list_filter = ('categoria', 'destaque', 'instituicao')
    search_fields = ('titulo', 'instituicao', 'codigo_verificacao')
    list_editable = ('destaque', 'ordem')

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'criado_em', 'lido')
    list_filter = ('lido', 'criado_em')
    search_fields = ('nome', 'email', 'assunto', 'mensagem')
    readonly_fields = ('nome', 'email', 'assunto', 'mensagem', 'criado_em')
