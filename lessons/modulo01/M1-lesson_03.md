# Aula 03 - Django: Templates e boas práticas
Vamos começar a realizar as primeiras mudanças no código Django. Abaixo segue a lista de ações que vamos realizar nessa aula:

1. Mudar a linguagem e fuso horário para as configurações do Brasil.
2. Criar o um app para o projeto.
3. Configurar a engrega de conteúdo HTTP no arquivo views.
4. Configurar as rotas no arquivo urls isolando o app do projeto.
5. Criar o Templates e nossa primeira página HTML.

---

## Execução

1. **Mudando o horário e linguagem do código**

O fuso horário e linguagem do código são definidos no arquivo settings.py na raiz do projeto. Vamos substituir os valores padrões por:
```
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

---

2. **Criando um App para o projeto**

O projeto que criamos é apenas a fundação para que sejam inseridos um ou varias applicações com diversas funcionalidades. Para criar um app dentro no nosso projeto use o comando abaixo:
```
(venv) $ python manage.py startapp galeria
```

---

3. **Configuração da função de entrega HTTP**

Para que o Django possa entregar algum conteúdo através do protocolo HTTP precisamos criar uma função dentro do arquivo de views, que por sua vez fica dentro do diretório do nosso App (galeria). A fim de realizar um teste, vou usar um módulo chamado HttpResponse do proprio Django:
```
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Alura Space</h1>')
```

4. **Configurando as rotas no arquivo urls**

Agora para que o Django possa entregar o conteúdo que criamos no views, é necessário informar uma rota para função. Insira o código no arquivo de urls que está presente na raiz do projeto:
```
from galeria.views import index

# 'path' deve ser inserido dentro da array de 'urlpatterns'
    path('', index)
```

Agora que validamos que as configurações estão corretas, devemos isolar as configurações de rotas para o App específicamente. No ínicio do projeto não é um problema usar apenas um arquivo para rotas, porém imagine em um caso real, um projeto sempre terá mais de uma funcionalidade, ou seja, diversos apps, portando esse arquivo de rotas pode se tornar muito extenso e dificil de se atualizar e gerenciar. Uma boa prática é separar um arquivo de rotas para cada app do projeto e depois importa-los no arquivo de rotas do projeto. </br>
Vamos realizar esta ação neste passo. Faça de acordo com os passos abaixo.

* Criando um arquivo de rotas para o App

Crie um arquivo urls (sempre no plural) dentro do diretório galeria:
```
(venv) $ vim galeria/urls.py
```

Dentro deste arquivo vamos importar o método path e também nossa função index, criando um urlpatterns e configurando a rota para a função (como foi feito anteriormente):
```
from django.urls import path 
from galeria.views import index

urlpatterns = [
    path('', index)
]
```

* Importando o arquivo de rotas do app no arquivo do projeto

Para o Django reconhecer o nosso arquivo de rotas novo, precisamos incluir esse arquivo rotas dentro urls.py que está localizado na raiz do projeto. Para isso vamos usar um metodo chamado include que é nativo do Django (não será mais necessária a linha de importação do views):
```
from django.urls import path, include

# 'path' deve ser inserido dentro da array de 'urlpatterns'
    path('', include('galeria.urls')),
```

---

5. **Criando a primeira página HTML**

Vamos concordar que concordar que criar uma página HTML dentro do arquivo views não parece ser uma tarefa adequada. Certamente o Django tem um diretório dedicado para criarmos e configurarmos as páginas HTML do nosso projeto.</br>
Para criar e configurar o HTML do nosso projeto vamos começcar adicionado o diretório no arquivo de settings.py na configuração de templates:
```
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

Após essa configuração precisamos criar o diretório no root do nosso projeto junto com a nossa index.html.</br>
Criando o diretório 'templates':
```
)venv) $ mkdir alura_space/templates
```

Criando nossa index.html:
```
)venv) $ vim alura_space/templates/index.html
```

Conteúdo da página:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alura Space</title>
</head>
<body>
    <h1>Alura Space</h1>
    <p>Isso é uma página HTML...</p>
</body>
</html>
```