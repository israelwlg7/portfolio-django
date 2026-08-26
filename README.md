# 🌐 Portfólio Profissional em Django - Israel Shalon

Um web app moderno, responsivo e dinâmico construído com **Python** e **Django**, apresentando perfil profissional, stack tecnológica, galeria interativa de projetos do GitHub, certificações (AWS Cloud, SENAC, Santander, Bradesco) e um formulário de contato integrado.

---

## ✨ Funcionalidades Principais

- 🎨 **Design System Dark & Glassmorphism**: Interface futurista com modo escuro, efeitos de vidro fosco (`backdrop-filter`), gradientes e animações CSS3.
- ⚡ **Efeito de Digitação Animada**: Transição dinâmica de cargos e competências na seção principal.
- 📂 **Galeria Interativa de Projetos**:
  - Filtro por categorias em tempo real (*Todos, Web & Django, Desktop / GUI, Lógica & Exercícios*).
  - Cards com badges de tecnologia e links diretos para os repositórios no GitHub.
- 📜 **Central de Certificações & Qualificações**:
  - Exibição de certificações verificadas com links diretos para badges (ex: **AWS Academy no Credly**), códigos de verificação e cargas horárias.
- 📬 **Formulário de Contato Persistido**:
  - Mensagens de visitantes são validadas e armazenadas no banco de dados SQLite com feedback visual imediato (*Alert Toast*).
- 🛠️ **Painel Administrativo Django**:
  - Gestão de projetos, certificados e visualização de mensagens recebidas pelo `/admin`.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.x, Django 6.x
- **Banco de Dados**: SQLite3 (com suporte a ORM Django)
- **Frontend**: HTML5 Semântico, CSS3 (Glassmorphism & Variables), JavaScript ES6+
- **Ícones & Tipografia**: FontAwesome 6, Google Fonts (*Plus Jakarta Sans* e *Fira Code*)

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/israelwlg7/portfolio-django.git
cd portfolio-django
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar o Django
```bash
pip install django
```

### 4. Executar as Migrações e Popular o Banco de Dados
```bash
python manage.py migrate
python seed_data.py
```

### 5. Iniciar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

Acesse o sistema em seu navegador em `http://127.0.0.1:8000/`.

---

## 👤 Autor

**Israel Shalon Oliveira Leitão**
- **GitHub**: [@israelwlg7](https://github.com/israelwlg7)
- **E-mail**: israelshalon02@gmail.com
- **Localização**: Manaus - AM
