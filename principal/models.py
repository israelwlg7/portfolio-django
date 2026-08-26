from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    CATEGORIAS = (
        ('WEB', 'Web / Django'),
        ('DESKTOP', 'Desktop / GUI'),
        ('OUTRO', 'Lógica & Outros'),
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=200, help_text="Separe as tecnologias por vírgula (ex: Python, Django, SQLite)")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='WEB')
    link_github = models.URLField(blank=True, null=True)
    link_demo = models.URLField(blank=True, null=True)
    destaque = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', '-criado_em']

    def __str__(self):
        return self.titulo

    def get_tecnologias_list(self):
        return [t.strip() for t in self.tecnologias.split(',') if t.strip()]

class Certificado(models.Model):
    TIPO_CHOICES = (
        ('CLOUD', 'Cloud & DevOps'),
        ('PYTHON', 'Python & Programação'),
        ('WEB', 'Desenvolvimento Web'),
        ('FERRAMENTAS', 'Ferramentas & SO'),
    )
    titulo = models.CharField(max_length=120)
    instituicao = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20, choices=TIPO_CHOICES, default='PYTHON')
    codigo_verificacao = models.CharField(max_length=150, blank=True, null=True)
    link_credencial = models.URLField(blank=True, null=True)
    ano = models.CharField(max_length=20, default="2026")
    destaque = models.BooleanField(default=False)
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f"{self.titulo} - {self.instituicao}"

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f"Mensagem de {self.nome} ({self.email}) - {self.assunto}"
