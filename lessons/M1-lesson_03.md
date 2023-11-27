# Aula 03 - Django: Templates e boas práticas
Vamos começar a realizar as primeiras mudanças no código Django. Abaixo segue a lista de ações que vamos realizar nessa aula:

1. Mudar a linguagem e fuso horário para as configurações do Brasil.
2. Criar o um app para o projeto.
3. Configurar a engrega de conteúdo HTTP no arquivo views.
4. Configurar as rotas no arquivo urls isolando o app do projeto.
5. Criar o Templates e nossa primeira página HTML.

---

## Execução

1. Mudando o horário e linguagem do código

O fuso horário e linguagem do código são definidos no arquivo settings.py na raiz do projeto. Vamos substituir os valores padrões por:
```
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

---

2. Criando um App para o projeto

O projeto que criamos é apenas a fundação para que sejam inseridos um ou varias applicações com diversas funcionalidades. Para criar um app dentro no nosso projeto use o comando abaixo:
```
(venv) $ python manage.py startapp galeria
```

---

3. Configuração da função de entrega HTTP

Para que o Django possa entregar algum conteúdo através do protocolo HTTP precisamos criar uma função dentro do arquivo de views, que por sua vez fica dentro do diretório do nosso App (galeria). A fim de realizar um teste, vou usar um módulo chamado HttpResponse do proprio Django:
```
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Alura Space</h1>')
```

4. Configurando as rotas no arquivo urls

Agora para que o Django possa entregar o conteúdo que criamos no views, é necessário informar uma rota para função. Insira o código no arquivo de urls que está presente na raiz do projeto:
```
from galeria.views import index

# 'path' deve ser inserido dentro da array de 'urlpatterns'
    path('', index)
```