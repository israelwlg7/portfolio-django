import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_ia.settings')
django.setup()

from principal.models import Projeto, Certificado

print("Iniciando população do banco de dados...")

# Limpar dados antigos se existirem
Projeto.objects.all().delete()
Certificado.objects.all().delete()

# Inserir Projetos
projetos_data = [
    {
        "titulo": "Sistema de Estacionamento Web",
        "descricao": "Sistema completo de gestão de estacionamentos com mapa gráfico de vagas, controle de entrada/saída de veículos, cálculo de permanência e tarifas, módulo de pagamentos, registro de ocorrências e chat interno entre usuários e administração (Desenvolvido em equipe).",
        "tecnologias": "Python, Django, SQLite, HTML5, CSS3, JavaScript, Git",
        "categoria": "WEB",
        "link_github": "https://github.com/israelwlg7/sistema-estacionamento-web",
        "destaque": True,
        "ordem": 1
    },
    {
        "titulo": "Sistema de Cadastro de Usuários",
        "descricao": "Aplicação para gerenciamento completo de usuários, controle de permissões e autenticação segura com banco de dados SQLite e formulários estilizados.",
        "tecnologias": "Python, Django, SQLite, Autenticação, HTML5",
        "categoria": "WEB",
        "link_github": "https://github.com/israelwlg7/sistema-cadastro-django",
        "destaque": True,
        "ordem": 2
    },
    {
        "titulo": "Portfólio Interativo em Django",
        "descricao": "Web app dinâmico com design futurista Dark/Glassmorphism para apresentação de competências, projetos em destaque, galeria de certificações e formulário de contato integrado.",
        "tecnologias": "Python, Django, Glassmorphism, CSS3, JavaScript",
        "categoria": "WEB",
        "link_github": "https://github.com/israelwlg7/portfolio-django",
        "destaque": True,
        "ordem": 3
    },
    {
        "titulo": "Mercadinho & Controle de Estoque",
        "descricao": "Sistema web de gerenciamento comercial para registro de vendas, controle de entrada e saída de produtos e consulta de estoque em tempo real.",
        "tecnologias": "Python, Django, SQLite, ORM Django",
        "categoria": "WEB",
        "link_github": "https://github.com/israelwlg7",
        "destaque": False,
        "ordem": 4
    },
    {
        "titulo": "Gerenciador de Chamados & Suporte",
        "descricao": "Plataforma de suporte técnico para abertura de chamados, classificação por prioridade e acompanhamento de status de atendimento.",
        "tecnologias": "Python, Django, Bootstrap, SQLite",
        "categoria": "WEB",
        "link_github": "https://github.com/israelwlg7",
        "destaque": False,
        "ordem": 5
    },
    {
        "titulo": "Exercícios & Lógica em Python",
        "descricao": "Coleção de exercícios práticos cobrindo fundamentos de lógica de programação, estrutura de dados, orientação a objetos e interfaces gráficas em Tkinter.",
        "tecnologias": "Python, Tkinter, Lógica de Programação, POO",
        "categoria": "OUTRO",
        "link_github": "https://github.com/israelwlg7/exercicios-python",
        "destaque": False,
        "ordem": 6
    }
]

for p in projetos_data:
    Projeto.objects.create(**p)

print(f"{len(projetos_data)} projetos cadastrados com sucesso!")

# Inserir Certificados
certificados_data = [
    {
        "titulo": "AWS Academy Graduate - Cloud Web Application Builder",
        "instituicao": "AWS Academy",
        "carga_horaria": "12h",
        "categoria": "CLOUD",
        "codigo_verificacao": "hypFBK0G",
        "link_credencial": "https://www.credly.com/go/hypFBK0G",
        "ano": "05/2026",
        "destaque": True,
        "ordem": 1
    },
    {
        "titulo": "Formação em Programação Python (Algoritmos, GUI & Web)",
        "instituicao": "SENAC",
        "carga_horaria": "156h",
        "categoria": "PYTHON",
        "codigo_verificacao": "SENAC-AM",
        "ano": "08/2026",
        "destaque": True,
        "ordem": 2
    },
    {
        "titulo": "Python",
        "instituicao": "Santander Open Academy",
        "carga_horaria": "8h",
        "categoria": "PYTHON",
        "codigo_verificacao": "OA-2026-0826003113956",
        "ano": "08/2026",
        "destaque": True,
        "ordem": 3
    },
    {
        "titulo": "Linguagem de Programação Python - Básico",
        "instituicao": "Fundação Bradesco",
        "carga_horaria": "18h",
        "categoria": "PYTHON",
        "codigo_verificacao": "7CF29B0D-3372-422A-AFE1-DEE6EB4DDEE8",
        "ano": "08/2026",
        "destaque": True,
        "ordem": 4
    },
    {
        "titulo": "Crie um Site Simples usando HTML, CSS e JavaScript",
        "instituicao": "Fundação Bradesco",
        "carga_horaria": "2h",
        "categoria": "WEB",
        "codigo_verificacao": "62F27AE6-CF5D-4B5B-A6E6-1F04E4E2C9DE",
        "ano": "08/2026",
        "destaque": False,
        "ordem": 5
    },
    {
        "titulo": "Excel Instrumental",
        "instituicao": "SENAC",
        "carga_horaria": "20h",
        "categoria": "FERRAMENTAS",
        "codigo_verificacao": "Concluído",
        "ano": "06/2026",
        "destaque": False,
        "ordem": 6
    },
    {
        "titulo": "Word Instrumental",
        "instituicao": "SENAC",
        "carga_horaria": "20h",
        "categoria": "FERRAMENTAS",
        "codigo_verificacao": "Concluído",
        "ano": "06/2026",
        "destaque": False,
        "ordem": 7
    },
    {
        "titulo": "Windows Instrumental",
        "instituicao": "SENAC",
        "carga_horaria": "20h",
        "categoria": "FERRAMENTAS",
        "codigo_verificacao": "EB7F2636",
        "ano": "06/2024",
        "destaque": False,
        "ordem": 8
    }
]

for c in certificados_data:
    Certificado.objects.create(**c)

print(f"{len(certificados_data)} certificados cadastrados com sucesso!")
print("Carga de dados concluída!")
