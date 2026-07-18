# 🌐 Portfólio de Projetos (Django)

Este é um web app pessoal construído em Django que funciona como meu portfólio dinâmico. O sistema conta com uma galeria interativa para apresentar projetos, bio, perfil e habilidades. É o meu primeiro projeto principal utilizando Django para entender o fluxo de rotas, renderização de templates HTML dinâmicos e organização de arquivos estáticos.

## 🛠️ Tecnologias Utilizadas
* **Backend:** Python e Django (versão 6+)
* **Banco de Dados:** SQLite (futuramente para persistência de mensagens de contato ou novos projetos)
* **Frontend:** HTML e CSS incorporado

## 📁 Estrutura do Projeto
* `site_ia/` - Configurações principais do projeto Django.
* `principal/` - Aplicação Django que gerencia a página principal e a galeria de projetos.
* `principal/templates/` - Templates HTML (como o `galeria.html`).
* `manage.py` - Script de linha de comando para gerenciamento do Django.

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/israelwlg7/portfolio-django.git
cd portfolio-django
```

### 2. Criar e Ativar o Ambiente Virtual (venv)
```bash
# No Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar o Django
```bash
pip install django
```

### 4. Executar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```
Abra o navegador e acesse: `http://127.0.0.1:8000/`
