# Aula 04 - Django: Templates e boas práticas
Nesta aula vamos configurar nosso template do Alura Space no nosso projeto e fazer com que o Django carregue todos os arquivos estáticos.</br>
Passos a serem executados:

1. Configuração dos estáticos no settings.py
2. Inclusão dos arquivos no diretório de static
3. Endereçamento dos estáticos pelo comando collectstatic
4. Embed de código Django no index.html e repetição do processo na página imagem.html
5. Criação da função de entrega HTTP da página imagem.html
6. Criação da rota para a imagem/

---

1. **Configurando os estáticos no settings do Django**

Para que o Django carregue os arquivos estáticos devemos informar para ele o path de onde os estáticos estarão, e também onde o Django deve mapear para acessa-los. Insira esse código no arquivo de settings.py:
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

---

2. **Criando e incluindo os arquivos estáticos no projeto**

Com o comando abaixo crie e mova os arquivos estáticos para o diretório que o Django acessará os arquivos:
```
(venv) $ mkdir setup/static
```

Agora copie as pastas 'assets' e 'styles' para dentro do dir 'static' criado (esses arquivos e encontram no zip diponível nesse repositório "alura_space-projeto_front.zip").

---

3. **Endereçando os estáticos**

Para endereçar os estáticos no Django utilize o comando:
```
(venv) $ python manage.py collectstatic
```
 
 Esse comando irá identificar todos os arquivos estáticos dento do setup/static e endereçar para um diretório static dentro da raiz (alura_space/), conforme definido no settings.py. A saída será algo como:
 ```
 173 static files copied to 'django-python-alura_space/alura_space/static'.
 ```

 ---

4. **Embedando o código Django no HTML**

Para o HTML entregar os arquivos estáticos, é necessário informar através de código Django o path de cada arquivo.</br>
No HTML convencional fariamos algo como:
```
    <link rel="stylesheet" href="/styles/style.css">
```

Já com Django é necessário adicionar primeiro o comando para carregar os estáticos, e onde houver o path de cada arquivo estático inserir uma sintaxe de string do static:
```
<!-- Adicionar o load static no inicio de todo arquivo HTML -->
{% load static %}

    <!-- Adicionar a sintaxe de string para o path de cada arquivo estático no arquivo HTML <TAG href="{% static 'path/file' %}"> -->
    <link rel="stylesheet" href="{% static '/styles/style.css' %}">
```

---

5. **Criando uma função para a página imagem/**

Vamos fazer um nova função para entregar a nossa página imagem/ no arquivo views:
```
def imagem(request):
    return render(request, 'galeria/imagem.html')
```

Essa função é exatamente igual a index, o propósito é o mesmo. Entregar uma página HTML dentro do path galeria/ através do método render.

6. **Criando a rota para a página imagem/**

Agora que criamos a função de entrega HTTP para a nova página, vamos criar a rota para o Django entregar essa página para nós:
```
# importe a nova função imagem
from galeria.views import index, imagem

# dentro do urlpatterns
    path('imagem/', imagem)
```

Agora podemos acessar e validar no URL: http://127.0.0.1:8000/imagem/, porém ainde precisamos corrigir uma coisa.
Se tentarmos acessar a página imagem/ através dos links HTML ou até mesmo voltar para a Home vamos receber um erro de 'Page not found'. Este problema será solucionado na aula 04 junto com melhorias de código com a metodologia DRY (Don't repeat yourself).